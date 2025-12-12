import streamlit as st
from datetime import datetime
import json
import requests
import pandas as pd

# Configure the page
st.set_page_config(
    page_title="MongoDB Database Manager",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Base URL
API_BASE_URL = "http://localhost:8000"

def check_api_connection():
    """Check if the API server is running"""
    try: 
        response = requests.get(f"{API_BASE_URL}/")
        return response.status_code == 200
    except:
        return False
    
def create_user(name, email, age):
    """Create a new user via database API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/",
            json={"name": name, "email": email, "age": age}
        )
        return response.json(), response.status_code == 201
    except Exception as e:
        return {"error": str(e)}, False
    
def get_all_users():
    """Fetch all users from the database via API"""
    try:
        response = requests.get(f"{API_BASE_URL}/users/")
        if response.status_code == 200:
            return response.json(), True
        return [{"error": "Failed to fetch users"}], False
    except Exception as e:
        return [], False
    
def get_user_posts(user_id):
    """Fetch posts for a specific user via API"""
    try:
        response = requests.get(f"{API_BASE_URL}/users/{user_id}/posts/")
        if response.status_code == 200:
            return response.json(), True
        return [{"error": "Failed to fetch posts"}], False
    except Exception as e:
        return [], False
    
def create_post(user_id, title, content):
    """Create a new post for a user via database API"""
    try:
        response = requests.post(
            f"{API_BASE_URL}/users/{user_id}/posts/",
            json={"user_id": user_id, "title": title, "content": content}
        )
        return response.json(), response.status_code == 201
    except Exception as e:
        return {"error": str(e)}, False

def get_all_posts():
    """Fetch all posts from the database via API"""
    try:
        response = requests.get(f"{API_BASE_URL}/posts/")
        if response.status_code == 200:
            return response.json(), True
        return [{"error": "Failed to fetch posts"}], False
    except Exception as e:
        return [], False
    
def delete_user(user_id):
    """Delete a user via database API"""
    try:
        response = requests.delete(f"{API_BASE_URL}/users/{user_id}/")
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False
    
def delete_post(post_id):
    """Delete a post via database API"""
    try:
        response = requests.delete(f"{API_BASE_URL}/posts/{post_id}/")
        return response.json(), response.status_code == 200
    except Exception as e:
        return {"error": str(e)}, False
    
# def update_user(user_id, name, email, age):
#     """Update user details via database API"""
#     try:
#         response = requests.put(
#             f"{API_BASE_URL}/users/{user_id}/",
#             json={"name": name, "email": email, "age": age}
#         )
#         return response.json(), response.status_code == 200
#     except Exception as e:
#         return {"error": str(e)}, False

def main():
    st.title("🗄️ MongoDB Database Manager")
    st.markdown("---")

    # Check API connection
    if not check_api_connection():
        st.error("Cannot connect to the API server. Please ensure it is running.")
        st.info("Run: 'python fastapi filename.py' to start the server.")
        return

    st.success("Connected to the API server successfully!")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Users", "Posts", "Dashboard"]
    )

    if page == "Users":
        users_page()
    elif page == "Posts":
        posts_page()
    elif page == "Dashboard":
        dashboard_page()

def users_page():
    st.header("User Management")

    # Display success message if it exists in session state
    if 'success_message' in st.session_state:
        st.success(st.session_state.success_message)
        del st.session_state.success_message

    # Create tabs for different user operations
    tab1, tab2, tab3 = st.tabs(["Create User", "View Users", "Delete User"])

    with tab1:
        st.subheader("Create New User")
        with st.form("create_user_form"):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("Name")
                email = st.text_input("Email")
            with col2:
                age = st.number_input("Age", min_value=1, max_value=120, step=25)

            submitted = st.form_submit_button("Create User", type="primary")

            if submitted:
                if name and email:
                    result, success = create_user(name, email, age)
                    if success:
                        st.success(f"User created successfully! ID: {result.get('user_id')}")
                        st.rerun()
                    else:
                        st.error(f"Error: {result.get('error', 'Unknown error')}")
                else:
                    st.warning("Please fill in all required fields.")

    with tab2:
        st.subheader("All Users")
        users, success = get_all_users()
        if success and users:
            df = pd.DataFrame(users)
            df['created_at'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m-%d %H:%M:%S')

            # Display users in a nice table
            st.dataframe(
                df[['id', 'name', 'email', 'age', 'created_at']],
                use_container_width=True,
                hide_index=True
            )

            #Show user count
            st.info(f"Total Users: {len(users)}")

        else:
            st.error("No users found or failed to fetch users.")

    with tab3:
        st.subheader("Delete User")
        users, success = get_all_users()
        if success and users:
            user_options = {f"{user['name']} (ID: {user['id']})": user['id'] for user in users}
            selected_user_display = st.selectbox("Select User to Delete", list(user_options.keys()))

            if selected_user_display:
                selected_user_id = user_options[selected_user_display]
                selected_user = next((user for user in users if user['id'] == selected_user_id), None)

                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Update User**")
                    # with st.form("update_user_form"):
                    #     new_name = st.text_input("Name", value=selected_user['name'])
                    #     new_email = st.text_input("Email", value=selected_user['email'])
                    #     new_age = st.number_input("Age", min_value=1, max_value=120, step=25, value=selected_user['age'])


                        # if st.form_submit_button("Update User", type="primary"):
                        #     result, success = update_user(selected_user_id, new_name, new_email, new_age)
                        #     if success:
                        #         st.success(f"User '{new_name}' updated successfully!")
                        #         st.rerun()
                        #     else:
                        #         st.error(f"Error: {result.get('error', 'Unknown error')}")

                with col2:
                    st.write("**Delete User**")
                    st.warning(f"Are you sure you want to delete user '{selected_user['name']}'? This action cannot be undone.")
                    if st.button("Delete User", type="secondary"):
                        result, success = delete_user(selected_user_id)
                        if success:
                            st.success(f"User '{selected_user['name']}' deleted successfully!")
                            st.rerun()
                        else:
                            st.error(f"Error: {result.get('error', 'Unknown error')}")

def posts_page():
    st.header("Post Management")

    # Create tabs for different post operations
    tab1, tab2, tab3 = st.tabs(["Create Post", "View Posts", "Manage Post"])

 

    with tab1:
        st.subheader("Create Post")
        
        # get users for dropdown
        users, user_success = get_all_users()

        # User selection
        if user_success and users:
            with st.form("create_post_form"):
                user_options = {f"{user['name']} (ID: {user['email']})": user['id'] for user in users}
                selected_user_display = st.selectbox("Select User", list(user_options.keys()))
                
                title = st.text_input("Post Title")
                content = st.text_area("Post Content")

                submitted = st.form_submit_button("Create Post", type="primary")

                if submitted:
                    if selected_user_display and title and content:
                        user_id = user_options[selected_user_display]
                        result, success = create_post(user_id, title, content)
                        if success:
                            st.success(f"Post '{title}' created successfully! ID: {result.get('id')}")
                            st.rerun()
                        else:
                            st.error(f"Error: {result.get('detail', 'Unknown error')}")
                    else:
                        st.warning("Please fill in all required fields.")
        else:
            st.error("No users found. Please create a user first.")

    with tab2:
        st.subheader("All Posts")
        posts, success = get_all_posts()
        if success and posts:
            for posts in posts:
                with st.expander(f"{posts['title']} (ID: {posts['id'][:8]}...)"):
                    col1, col2 = st.columns([3, 1])
                    with col1:
                        st.write(f"**Content:** {posts['content']}")
                        st.write(f"**Created: {pd.to_datetime(posts['created_at']).strftime('%Y-%m-%d %H:%M:%S')}**")
                    with col2:
                        st.write(f"**User ID:** {posts['user_id']}")
                        if st.button(f"Delete Post {posts['id']}", key=f"delete_post_{posts['id']}", type="secondary"):
                            result, success = delete_post(posts['id'])
                            if success:
                                st.success(f"Post '{posts['title']}' deleted successfully!")
                                st.rerun()
                            else:
                                st.error(f"Error: {result.get('error', 'Unknown error')}")
            st.info(f"Total Posts: {len(posts)}")
        else:
            st.error("No posts found or failed to fetch posts.")

    with tab3:
        st.subheader("Post by User")

        users, user_sucess = get_all_users()

        if user_sucess and users:
            user_options = {f"{user['name']} (ID: {user['email']})": user['id'] for user in users}
            selected_user_display = st.selectbox("Select User", list(user_options.keys()))

            if selected_user_display:
                user_id = user_options[selected_user_display]
                posts, success = get_user_posts(user_id)

                if success and posts:
                    st.write(f"Posts by {selected_user_display}:")
                    for post in posts:
                        with st.expander(f"{post['title']} (ID: {post['id'][:8]}...)"):
                            st.write(f"**Content:** {post['content']}")
                            st.write(f"**Created: {pd.to_datetime(post['created_at']).strftime('%Y-%m-%d %H:%M:%S')}**")

                else:
                    st.info(f"No posts found for {selected_user_display}.")

def dashboard_page():
    st.header("Dashboard")
    st.markdown("Overview of Users and Posts")

    users, user_success = get_all_users()
    posts, post_success = get_all_posts()

    if user_success and post_success:
        # Metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Users", len(users))

        with col2:
            st.metric("Total Posts", len(posts))
        
        with col3:
            avg_age = sum(user['age'] for user in users) / len(users) if users else 0
            st.metric("Average User Age", f"{avg_age:.2f}")

        with col4:
            posts_per_user = len(posts) / len(users) if users else 0
            st.metric("Avg Posts per User", f"{posts_per_user:.2f}")
        
        st.markdown("---")

    # charts
    if users:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("User Age Distribution")
            age_series = pd.Series([user['age'] for user in users])
            st.bar_chart(age_series.value_counts().sort_index())

        with col2:
            st.subheader("Recent Activity")

            if posts:
                #Post by date
                posts_df = pd.DataFrame(posts)
                posts_df['date'] = pd.to_datetime(posts_df['created_at']).dt.date
                daily_posts = posts_df.groupby('date').size()
                st.line_chart(daily_posts)

        # Recent posts
        st.subheader("Recent Posts")
        if posts:
            recent_posts = sorted(posts, key=lambda x: x['created_at'], reverse=True)[:5]
            for post in recent_posts:
                st.write(f"**{post['title']}** by User ID: {post['user_id']}")
                st.write(f"{post['content']}")
                st.write(f"*Created at: {pd.to_datetime(post['created_at']).strftime('%Y-%m-%d %H:%M:%S')}*")
                st.markdown("---")

    else:
        st.info("No data available to display.")

if __name__ == "__main__":
    main()



            

    