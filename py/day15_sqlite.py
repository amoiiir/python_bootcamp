import sqlite3

class DatabaseManager:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.init_database()

    def init_database(self):
        """Initialize database with tables"""
        with sqlite3.connect(self.db_name) as conn:
            # Point to the database
            cursor = conn.cursor()

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    age INTEGER,
                    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP               
                )
            ''')

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS posts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    title TEXT NOT NULL,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)      
                )
            ''')

    def create_user(self, name, email, age):
        """ Create a new user"""
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (name, email, age) 
                    VALUES (?, ?, ?)
                ''', (name, email, age))
                return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error creating user: {e}")
            return None
        
    def create_post(self, user_id, title, content):
        """Create a new post for a user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO posts (user_id, title, content) 
                VALUES (?, ?, ?)
            ''', (user_id, title, content))
            return cursor.lastrowid

    def get_all_users(self):
        """Retrieve all users"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()
    
    def get_a_user(self, user_id):
        """Retrieve a user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()
    
    def get_user_posts(self, user_id):
        """Get posts by user"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT p.id, p.title, p.content, p.created
                FROM posts p
                WHERE p.user_id = ?
                ORDER BY p.created DESC
            ''', (user_id,))
            return cursor.fetchall()
        
    def get_post(self, post_id):
        """Return a single post row (id, user_id, title, content, created) or None."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, user_id, title, content, created FROM posts WHERE id = ?', (post_id,))
            return cursor.fetchone()
        
    def update_user(self, name, email, age, user_id):
        """Update user information"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users
                SET
                    name = ?,
                    email = ?,
                    age = ?
                WHERE id = ?     
            ''', (name, email, age, user_id))
            return cursor.rowcount > 0
        
    def update_post(self, title, content, user_id):
        """Update post"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE posts
                SET
                    title = ?,
                    content = ?
                WHERE id = ?
            ''', (title, content, user_id))
            return cursor.rowcount > 0
    
    def delete_user(self, user_id):
        """Delete user and their posts"""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM posts WHERE user_id = ?', (user_id,))
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            return cursor.rowcount > 0
        
def display_menu():
    """Display the main menu"""
    print("=== SQLite Database Manager ===")
    print("1. Create User")
    print("2. View All Users")
    print("3. Create post")
    print("4. View User Posts")
    print("5. Delete User")
    print("6. Update user")
    print("7. Update posts")
    print("8. Exit")
        

def main():
    """Main interactive function CLI Function"""
    db = DatabaseManager()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- Create New User ---")
            name = input("Name: ").strip()
            email = input("Email: ").strip()

            try:
                age = int(input("Age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"User created with ID: {user_id}")
                else:
                    print("Failed to create user.")

            except ValueError:
                print("Invalid age. Please enter a number.")

        elif choice == '2':
            print("\n--- View All Users ---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user[0]} | Name: {user[1]} | Email: {user[2]} | Age: {user[3]} | Created At: {user[4]}")
            else:
                print("No users found.")

        elif choice == '3':
            print("\n---- Create New Post ---")
            try:
                user_id = int(input("User ID:").strip())
                title = input("Title: ").strip()
                content = input("Content: ").strip()
                post_id = db.create_post(user_id, title, content)
                if post_id:
                    print(f"Post created successfully with ID: {post_id}")
                else:
                    print("Failed to create post.")
            except ValueError:
                print("Invalid User ID. Please enter a number.")

        elif choice == '4':
            print("\n---View User Posts ---")
            try:
                user_id = int(input("User ID: ").strip())
                posts = db.get_user_posts(user_id)
                if posts:
                    for post in posts:
                        print(f"\nPost ID: {post[0]}")
                        print(f"Title: {post[1]}")
                        print(f"Content: {post[2]}")
                        print(f"Created At: {post[3]}")
                        print("-" * 20)
                else:
                    print("No posts found for this user.")
            except ValueError:
                print("Invalid User ID. Please enter a number.")

        elif choice == '5':
            print("\n--- Delete User ---")
            try: 
                user_id = int(input("Enter User ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete user {user_id} and all their posts? (y/n): ").strip().lower()
                if confirm == 'y':
                    if db.delete_user(user_id):
                        print("User and their posts deleted successfully.")
                    else:
                        print("User not found.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Invalid User ID. Please enter a number.")

        elif choice == "6":
            print("\n--- Update User ---")
            try:
                user_id = int(input("Enter user ID to update:").strip())
            except ValueError:
                print("Invalid User ID. Please enter a number.")
                print("\nPress Enter to continue ...")
                continue
            
            #Check if user already exist or not
            user = db.get_a_user(user_id)
            if not user:
                print("User not found.")
                input("\nPress Enter to continue...")
                continue

            #Show current values and prompt for new ones (Enter to keep current)
            print(f"Current name: {user[1]}\nCurrent email: {user[2]}\nCurrent age: {user[3]}")

            new_name = input(f"New name(press Enter to keep '{user[1]}'): ").strip() or user[1]
            new_email = input(f"New email(press Enter to keep '{user[2]}'): ").strip() or user[2]

            age_input = input(f"New age (press Enter to keep '{user[3]}'): ").strip()
            try:
                new_age = int(age_input) if age_input != "" else user[3]
            except ValueError:
                print("Invalid age input. Update Cancelled.")
                input("\nPress Enter to continue...")
                continue

            #Perform update
            if db.update_user(new_name, new_email, new_age, user_id):
                print("User updated successfully.")
            else: 
                print("Updated failed.")

        elif choice == "7":
            print("\n--- Update post ---")            

            try:
                post_id = int(input("Enter post ID: "))
            except ValueError:
                print("Input is not a number. Please enter a valid number")
                input("\nPress Enter to continue ...")
                continue

            post = db.get_post(post_id)
            print(post)

            if not post:
                print("Post does not exist with that ID.")
                input("\nPress Enter to continue...")
                continue
            
            new_title = input(f"Enter a new title(Press Enter to remain old title: '{post[2]}'): ") or post[2]
            new_content = input(f"Enter a new content(Press Enter to remain old content: '{post[3]}'): ") or post[3]

            if db.update_post(new_title, new_content, post_id):
                print("Update successful.")
            else:
                print("Update failed.")
        
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()

