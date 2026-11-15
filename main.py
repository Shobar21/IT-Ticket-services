
# Import libraries
import random
import json
from datetime import datetime

# JSON file to store tickets
FILE_NAME = "tickets.json"


# Load tickets from JSON file
def loadTickets():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("JSON file is empty or invalid. Starting with empty tickets.")
        return []


# Empty list or load previous tickets
tickets = loadTickets()


# Save tickets to JSON file
def saveTickets():
    with open(FILE_NAME, "w") as file:
        json.dump(tickets, file, indent=4)


# Generate unique ticket ID
def generateTicketID():
    if len(tickets) >= 99:
        return None

    while True:
        ticket_id = random.randint(1, 99)

        if not any(ticket["id"] == ticket_id for ticket in tickets):
            return ticket_id


# Submit a new ticket
def submitTickets():
    print("\n--- Submit a Ticket ---")

    print("Available Issues: Network Downtime, Slow Performance, Configuration Change")

    issue = input("Enter issue type: ").lower().strip()

    description = input("Write a short description of the problem: ").strip()

    # Validate issue type
    if issue not in [
        "network downtime",
        "slow performance",
        "configuration change"
    ]:
        print("Wrong issue type entered! Please enter a correct issue type.")
        return

    # Set priority and status
    if issue == "network downtime":
        priority = "High"
        status = "Closed"

    elif issue == "slow performance":
        priority = "Medium"
        status = "In Progress"

    elif issue == "configuration change":
        priority = "Low"
        status = "Open"

    # Generate ticket ID
    ticket_id = generateTicketID()

    if ticket_id is None:
        print("All ticket IDs are used!")
        return

    # Create ticket object
    ticket = {
        "id": ticket_id,
        "Issue": issue,
        "Description": description,
        "Priority": priority,
        "Status": status,
        "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Add ticket to list
    tickets.append(ticket)

    # Save tickets permanently
    saveTickets()

    print("\nTicket submitted successfully!")
    print("Your Ticket ID is:", ticket["id"])


# Check ticket function
def checkTickets():
    print("\n--- Check Ticket ---")

    try:
        ticket_id = int(input("Enter your Ticket ID: "))

    except ValueError:
        print("Please enter a valid ID.")
        return

    found = False

    for ticket in tickets:

        if ticket["id"] == ticket_id:

            print("\n--- Ticket Information ---")
            print("Ticket ID:", ticket["id"])
            print("Issue:", ticket["Issue"])
            print("Description:", ticket["Description"])
            print("Priority:", ticket["Priority"])
            print("Status:", ticket["Status"])
            print("Time:", ticket["Time"])

            found = True
            break

    if not found:
        print("Ticket not found!")


# View all open tickets
def viewOpenTickets():
    print("\n--- View Open Tickets ---")

    open_list = False

    for ticket in tickets:

        if ticket["Status"] == "Open":

            print("\nTicket ID:", ticket["id"])
            print("Issue:", ticket["Issue"])
            print("Description:", ticket["Description"])
            print("Priority:", ticket["Priority"])
            print("Status:", ticket["Status"])
            print("Time:", ticket["Time"])

            open_list = True

    if not open_list:
        print("There are no open tickets.")


# Main Menu
def Menu():
    while True:

        print("\n--- Network Support Desk System ---")
        print("1. Submit a New Ticket")
        print("2. Check Ticket Status")
        print("3. View Open Tickets")
        print("4. Exit")

        choice = input("Choose (1 to 4): ").strip()

        if choice == "1":
            submitTickets()

        elif choice == "2":
            checkTickets()

        elif choice == "3":
            viewOpenTickets()

        elif choice == "4":
            print("Thanks for using the Network Support Desk System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run program
if __name__ == "__main__":
    Menu()
