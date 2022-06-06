def login(database, username, password):
    if username in database and password == database[username]:
        print("\nWelcome back", username + "!\n")
        return username
    elif username in database and password != database[username]:
        print("Login failed. Incorrect password")
        return ""
    elif username not in database:
        print("\nUser not found. Please register.")

def register(database, username):
    if username in database:
        print("Username already exit")
        return ""
    else:
        print("\n", username, "has been registered!")
        return username