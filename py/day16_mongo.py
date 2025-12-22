from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId # MongoDB way of creating unique IDs
from dotenv import load_dotenv # Load environment variables from .env file
import os

# todo - Create a MongoDB database with collections for users and posts.
# ! Make sure to push this code to github after completion.
# * Implement CRUD operations for users and posts.
# ? Should this file being run as the best file of all time>
# // Finished implementing CRUD operations for users and posts.

load_dotenv() # Load environment variables from .env file

mongo_uri = os.getenv("MONGODB_ATLAS_CLUSTER_URI")

class DatabaseManager:

    # Mainly for creating and improving MongoDB
    def __init__(self, db_name='example_db', connection_string=mongo_uri):
        self.client = MongoClient(connection_string) # Create connection to MongoDB database
        self.db = self.client[db_name] # ! access the database
        self.users_collection = self.db.users
        self.posts_collection = self.db.posts
        self.init_database() # set up indeces for faster queries

    def init_database(self):
        """Initialize database with collections and indexes."""
        # Create unique index on email for users
        self.users_collection.create_index("email", unique=True)
        # Create index on user_id for posts for better query performance
        self.posts_collection.create_index("user_id")

    # Functions for CRUD operations
    def create_user(self, name, email, age):
        """Create a new user in the database."""
        try:
            user_doc = {
            "name": name,
            "email": email,
            "age": age,
            "created_at": datetime.now()
            }
            result = self.users_collection.insert_one(user_doc) #attempts to insert into users collection
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
    
    def create_post(self, user_id, title, content):
        """Create a new post"""
        try:
            # Convert string user_id to ObjectId if it is a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_id = ObjectId(user_id)
                print(f"Your user id would be: {user_id}")
            else:
                user_object_id = user_id

            post_doc = {
                "user_id": user_object_id,
                "title": title,
                "content": content,
                "created_at": datetime.now()
            }
            result = self.posts_collection.insert_one(post_doc)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Error creating post: {e}")
            return None
        
    def get_all_users(self):
        """Retrieve all users from the database."""
        try:
            users = list(self.users_collection.find())
            for user in users:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string for easier handling
            return users
        except Exception as e:
            print(f"Error retrieving users: {e}")
            return []
        
    def get_user_posts(self, user_id):
        """Retrieve all posts for a specific user."""
        try:
            # Convert string user_id to ObjectId if it is a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_id = ObjectId(user_id)
            else:
                user_object_id = user_id
        
            posts = list(self.posts_collection.find({"user_id": user_object_id}).sort("created_at",-1))
        
            #Convert ObjectId to string for display purposes
            for post in posts:
                post['_id'] = str(post['_id'])
                post['user_id'] = str(post['user_id'])

            return posts        
        except Exception as e:
            print(f"Error retrieving posts: {e}")
            return []

    def update_user(self, user_id, name=None, email=None, age=None):
        """Update user information."""
        try:
            update_fields = {}
            if name:
                update_fields['name'] = name
            if email:
                update_fields['email'] = email
            if age is not None:
                update_fields['age'] = age

            if not update_fields:
                print("No fields to update.")
                return False

            # Convert string user_id to ObjectId if it is a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            result = self.users_collection.update_one(
                {"_id": user_object_id},
                {"$set": update_fields}
            )
            return result.modified_count > 0
        
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        
    def delete_user(self, user_id):
        """Delete a user and their posts from the database."""
        try:
            # Convert string user_id to ObjectId if it is a valid ObjectId
            if ObjectId.is_valid(user_id):
                user_object_id = ObjectId(user_id)
            else:
                user_object_id = user_id

            # Delete user's posts first
            self.posts_collection.delete_many({"user_id": user_object_id})

            # Delete the user
            result = self.users_collection.delete_one({"_id": user_object_id})
            return result.deleted_count > 0
        
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
    def close_connection(self):
        """Close the database connection."""
        self.client.close()

    
def display_menu():
    """Display the main menu options."""
    print("\nMenu:")
    print("\n" + "-" * 20)
    print("Database Manager Menu:")
    print("1. Create User")
    print("2. View All Users")
    print("3. Create Post")
    print("4. View User Posts")
    print("5. Update User")
    print("6. Delete User")
    print("7. Exit")
    print("-" * 20 + "\n")

def main():
    """Main interactive CLI Function"""
    try:
        db = DatabaseManager()
        print("Connected to MongoDB successfully.")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        print("Make sure MongoDB is runnning on localhost:27017 or check your connection string.")
        return
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print("\n---Create new user---")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()

            try:
                age = int(input("Enter age: ").strip())
                user_id = db.create_user(name, email, age)
                if user_id:
                    print(f"User created successfully with ID: {user_id}")
                else:
                    print("Failed to create user.")
            except ValueError:
                print("Invalid age. Please enter a number.")

        elif choice == '2':
            print("\n---All Users---")
            users = db.get_all_users()
            if users:
                for user in users:
                    print(f"ID: {user['_id']}, Name: {user['name']}, Email: {user['email']}, Age: {user['age']}, Created At: {user['created_at']}")
            else:
                print("No users found.")

        elif choice == '3':
            print("\n---Create new post---")
            user_id = input("Enter user ID: ").strip()
            title = input("Enter post title: ").strip()
            content = input("Enter post content: ").strip()
            post_id = db.create_post(user_id, title, content)
            if post_id:
                print(f"Post created successfully with ID: {post_id}")
            else:
                print("Failed to create post.")

        elif choice == '4':
            print("\n---View User Posts---")
            user_id = input("Enter user ID: ").strip()
            posts = db.get_user_posts(user_id)
            if posts:
                for post in posts:
                    print(f"ID: {post['_id']}")
                    print(f"Title: {post['title']}")
                    print(f"Content: {post['content']}")
                    print(f"Created At: {post['created_at']}")
                    print("-" * 20)
            else:
                print("No posts found for this user.")

        elif choice == '5':
            print("\n---Update User---")
            user_id = input("Enter user ID to update: ").strip()
            name = input("Enter new name (leave blank to keep unchanged): ").strip()
            email = input("Enter new email (leave blank to keep unchanged): ").strip()
            age_input = input("Enter new age (leave blank to keep unchanged): ").strip()

            age = None
            if age_input:
                try:
                    age = int(age_input)
                except ValueError:
                    print("Invalid age. Please enter a number.")
                    continue

            success = db.update_user(user_id, name=name if name else None,
                                     email=email if email else None,
                                     age=age)
            if success:
                print("User updated successfully.")
            else:
                print("Failed to update user. Make sure the user ID is correct.")

        elif choice == '6':
            print("\n---Delete User---")
            user_id = input("Enter user ID to delete: ").strip()
            confirm = input("Are you sure you want to delete this user and all their posts? (y/n): ").strip().lower()
            if confirm == 'y':
                success = db.delete_user(user_id)
                if success:
                    print("User and their posts deleted successfully.")
                else:
                    print("Failed to delete user. Make sure the user ID is correct.")
            else:
                print("Deletion cancelled.")

        elif choice == '7':
            print("Exiting the program.")
            db.close_connection()
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()