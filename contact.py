import os

# Define the file where contacts will be stored
CONTACT_FILE = "contacts.txt"

def initialize_contact_file():
    """
    Ensures the contact file exists. If not, it creates an empty one.
    """
    if not os.path.exists(CONTACT_FILE):
        try:
            with open(CONTACT_FILE, 'w') as f:
                f.write("") # Create an empty file
            print(f"'{CONTACT_FILE}' created successfully.")
        except IOError as e:
            print(f"Error creating file '{CONTACT_FILE}': {e}")

def add_contact():
    """
    Prompts the user for contact details (name, phone, email) and adds them to the file.
    """
    print("\n--- Add New Contact ---")
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty. Contact not added.")
        return

    # Format the contact details for storage
    contact_entry = f"{name},{phone},{email}\n"

    try:
        with open(CONTACT_FILE, 'a') as f:
            f.write(contact_entry)
        print(f"Contact '{name}' added successfully!")
    except IOError as e:
        print(f"Error adding contact to file: {e}")

def view_contacts():
    """
    Reads and displays all contacts from the file.
    """
    print("\n--- All Contacts ---")
    try:
        with open(CONTACT_FILE, 'r') as f:
            contacts = f.readlines()

        if not contacts:
            print("No contacts found.")
            return

        print(f"{'Name':<20}{'Phone':<15}{'Email':<30}")
        print("-" * 65)
        for i, contact in enumerate(contacts):
            parts = contact.strip().split(',')
            name = parts[0] if len(parts) > 0 else "N/A"
            phone = parts[1] if len(parts) > 1 else "N/A"
            email = parts[2] if len(parts) > 2 else "N/A"
            print(f"{name:<20}{phone:<15}{email:<30}")
        print("-" * 65)

    except FileNotFoundError:
        print("Contact file not found. Please add some contacts first.")
    except IOError as e:
        print(f"Error reading contacts from file: {e}")

def search_contact():
    """
    Prompts the user for a search term and displays matching contacts.
    Searches by name or phone number.
    """
    print("\n--- Search Contact ---")
    search_term = input("Enter name or phone number to search: ").strip().lower()

    if not search_term:
        print("Search term cannot be empty.")
        return

    found_contacts = []
    try:
        with open(CONTACT_FILE, 'r') as f:
            contacts = f.readlines()

        for contact in contacts:
            # Check if the search term is in the name or phone number (case-insensitive)
            if search_term in contact.lower():
                found_contacts.append(contact)

        if not found_contacts:
            print(f"No contacts found matching '{search_term}'.")
            return

        print(f"\n--- Search Results for '{search_term}' ---")
        print(f"{'Name':<20}{'Phone':<15}{'Email':<30}")
        print("-" * 65)
        for contact in found_contacts:
            parts = contact.strip().split(',')
            name = parts[0] if len(parts) > 0 else "N/A"
            phone = parts[1] if len(parts) > 1 else "N/A"
            email = parts[2] if len(parts) > 2 else "N/A"
            print(f"{name:<20}{phone:<15}{email:<30}")
        print("-" * 65)

    except FileNotFoundError:
        print("Contact file not found. Please add some contacts first.")
    except IOError as e:
        print(f"Error searching contacts in file: {e}")

def main_menu():
    """
    Displays the main menu and handles user choices.
    """
    initialize_contact_file() # Ensure file exists when application starts

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main_menu()
