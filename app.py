from donations_pkg.homepage import show_homepage, donate, show_donation
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
total_donations = []
authorized_user = ""
while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print("Logged in as:", authorized_user)


    option = input("Choose an option: ")
    if option == "1":
        username = (input("\nEnter Username: ")).lower()
        password = (input("Enter password: ")).lower()
        authorized_user = login(database, username, password)
    elif option == "2":
        while True:
            username = (input("\nEnter Username: ")).lower()
            if len(username) > 10:
                print("Username CANNOT be more than 10 characters.")
            else:
                break
        while True:
            password = (input("Enter password: ")).lower()
            if len(password) < 5:
                print("Password CANNOT be less than 5 characters.")
            else:
                break
        authorized_user = register(database, username)
        if authorized_user != "":
            database["username"] = "password"
    elif option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation = donate(authorized_user, total_donations)
            donations.append(donation)
    elif option == "4":
        show_donation(donations, total_donations)
        print()
    elif option == "5":
        print("")
        print("Goodbye..")
        quit()
    elif option != "1" or "2" or "3" or "4" or "5":
        print("\nIncorrect entry. Please type 1, 2, 3 or 4")
