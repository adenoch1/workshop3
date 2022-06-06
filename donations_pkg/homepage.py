def show_homepage():
    print("       === DonateMe Homepage ===         ")
    print("-----------------------------------------")
    print("| 1.   Login         | 2. Register       |")
    print("-----------------------------------------")
    print("| 3.   Donate        | 4. Show Donation  |")
    print("-----------------------------------------")
    print("|                  5. Exit               |")
    print("-----------------------------------------")

def donate(username, total_donations):
    donation_amt = float(input("\nEnter amount to donate: "))
    donation = username + " donated " + str(donation_amt)
    total_donations.append(donation_amt)
    print("Thank you for your donation!")
    return donation

def show_donation(donation, total_donations):
    print("\n----All Donations----")
    if donation == []:
        print("\nCurrently, there are no donations.")
    else:
        for amount in donation:
            print(amount)
        sum = 0
        for number in total_donations:
            sum += number
        print("Total = ", sum)

        