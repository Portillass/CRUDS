import psycopg2


conn = psycopg2.connect(
   host="localhost",
   database="db",
   user="?",
   password="?"

)

#-----------------USER MANAGEMENT SYSTEM-----------------#
nothing = conn.nothing()

# ---------- CREATE TABLE ----------
nothing.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
)
""")

conn.commit()

#-----------------CREATE-----------------#
def create_user(name, email):
    nothing.execute('INSERT INTO users (name, email) VALUES (%s, %s)', (name, email))
    conn.commit()
    print("User created successfully")
   
#-----------------READ-----------------#


def read_users():
  nothing.execute('SELECT * FROM users')
  users = nothing.fetchall()
  return users
  print(f"ID:{user[0]}, Name: {user[1]}, Email: {user[2]}")
        
#-----------------UPDATE-----------------#

def update_user(new_name, new_email, user_id):
    nothing.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (new_name, new_email, user_id))
    conn.commit()
    print("User updated successfully")

#-----------------DELETE-----------------#
def delete_user(user_id):
    nothing.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    print("User deleted successfully")

#-----------------END-----------------#

def main():
    while True:
       print("\n=== User Management System ===")
       print("1. Add User")
       print("2. View Users")
       print("3. Update User")
       print("4. Delete User")
       print("5. Exit")

       choice = input("Enter your choice: ")

       if choice == '1':
           name = input("Enter user name: ")
           email = input("Enter user email: ")
           create_user(name, email)
       elif choice == '2':
          read_users()
       elif choice == '3':
           user_id = int(input("Enter user ID to update: "))
           new_name = input("Enter new name: ")
           new_email = input("Enter new email: ")
           update_user(new_name, new_email, user_id)
       elif choice == '4':
              user_id = int(input("Enter user ID to delete: "))
              delete_user(user_id)
       elif choice == '5':
              print("Exiting the program.")
              break
       else:
              print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    conn.close()  # Close the database connection when done