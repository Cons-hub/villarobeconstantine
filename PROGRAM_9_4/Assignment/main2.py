from person import Person
from record_manager import RecordManager


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value == "":
            print("Input cannot be empty.")
        else:
            return value


def get_age():
    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("Age must be greater than 0.")
            else:
                return age

        except ValueError:
            print("Invalid input. Age must be a whole number.")


def add_record(manager):
    print("\n===== ADD RECORD =====")

    person_id = get_non_empty_input("Enter ID: ")

    name = get_non_empty_input("Enter name: ")

    age = get_age()

    address = get_non_empty_input("Enter address: ")

    contact_number = get_non_empty_input("Enter contact number: ")

    email = get_non_empty_input("Enter email: ")

    try:
        person = Person(
            person_id,
            name,
            age,
            address,
            contact_number,
            email
        )

        manager.add_record(person)

        print("\nRecord added successfully.")

    except ValueError as error:
        print(f"\nError: {error}")


def view_records(manager):
    manager.view_records()


def search_record(manager):
    print("\n===== SEARCH RECORD =====")

    person_id = get_non_empty_input("Enter ID to search: ")

    record = manager.search_record(person_id)

    if record:
        print("\nRecord found:")
        print("-------------------------------")
        record.display_info()
        print("-------------------------------")
    else:
        print("Record not found.")


def update_record(manager):
    print("\n===== UPDATE RECORD =====")

    person_id = get_non_empty_input("Enter ID to update: ")

    record = manager.search_record(person_id)

    if record is None:
        print("Record not found.")
        return

    print("\nEnter new information:")

    name = get_non_empty_input("Enter new name: ")

    age = get_age()

    address = get_non_empty_input("Enter new address: ")

    contact_number = get_non_empty_input(
        "Enter new contact number: "
    )

    email = get_non_empty_input("Enter new email: ")

    success = manager.update_record(
        person_id,
        name,
        age,
        address,
        contact_number,
        email
    )

    if success:
        print("\nRecord updated successfully.")
    else:
        print("\nFailed to update record.")


def delete_record(manager):
    print("\n===== DELETE RECORD =====")

    person_id = get_non_empty_input("Enter ID to delete: ")

    record = manager.search_record(person_id)

    if record is None:
        print("Record not found.")
        return

    print("\nRecord to be deleted:")
    record.display_info()

    while True:
        confirmation = input(
            "\nAre you sure you want to delete this record? (Y/N): "
        ).strip().lower()

        if confirmation == "y":
            manager.delete_record(person_id)
            print("Record deleted successfully.")
            break

        elif confirmation == "n":
            print("Delete operation cancelled.")
            break

        else:
            print("Invalid choice. Enter Y or N.")


def display_menu():
    print("\n===================================")
    print(" PERSONAL INFORMATION MANAGEMENT")
    print("===================================")
    print("1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("===================================")


def main():
    manager = RecordManager()

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_record(manager)

            elif choice == 2:
                view_records(manager)

            elif choice == 3:
                search_record(manager)

            elif choice == 4:
                update_record(manager)

            elif choice == 5:
                delete_record(manager)

            elif choice == 6:
                print("\nThank you for using the system.")
                print("Program terminated successfully.")
                break

            else:
                print("\nInvalid menu choice. Please select 1-6.")

        except ValueError:
            print("\nInvalid input. Please enter a number from 1-6.")


if __name__ == "__main__":
    main()