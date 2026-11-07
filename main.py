from database import (
    create_table,
    add_record,
    view_records,
    update_record,
    delete_record
)

def menu():

    create_table()

    while True:
        print("\n===== TRANSIT TRACKER =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            vehicle_name = input("Vehicle Name: ")
            route = input("Route: ")
            departure_time = input("Departure Time: ")
            arrival_time = input("Arrival Time: ")
            passengers = int(input("Passengers: "))

            add_record(
                vehicle_name,
                route,
                departure_time,
                arrival_time,
                passengers
            )

        elif choice == "2":

            print("\n--- Records ---")
            view_records()

        elif choice == "3":

            record_id = int(input("Record ID to update: "))

            vehicle_name = input("New Vehicle Name: ")
            route = input("New Route: ")
            departure_time = input("New Departure Time: ")
            arrival_time = input("New Arrival Time: ")
            passengers = int(input("New Passenger Count: "))

            update_record(
                record_id,
                vehicle_name,
                route,
                departure_time,
                arrival_time,
                passengers
            )

        elif choice == "4":

            record_id = int(input("Record ID to delete: "))
            delete_record(record_id)

        elif choice == "5":

            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

menu()