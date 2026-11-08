from database import (
    create_table,
    add_record,
    view_records,
    update_record,
    delete_record
)
from functions import bubble_sort_passengers, search_departure, search_route, search_vehicle, sort_passengers, sort_vehicle_name

def menu():

    create_table()

    while True:
        print("\n===== TRANSIT TRACKER =====")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Search Records")
        print("6. Sort Records")
        print("7. Exit")

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

        elif choice == "7":

            print("Goodbye!")
            break

        elif choice == "5":
            print("\nSEARCH MENU")
            print("1. Search Route")
            print("2. Search Vehicle")
            print("3. Search Departure")

            search_choice = input("Choose: ")

            if search_choice == "1":
                route = input("Enter Route: ")
                search_route(route)

            elif search_choice == "2":
                vehicle = input("Enter Vehicle Name: ")
                search_vehicle(vehicle)

            elif search_choice == "3":
                departure = input("Enter Departure Time: ")
                search_departure(departure)

            else:
                print("Invalid search choice!")

        elif choice == "6":
            print("\nSORT MENU")
            print("1. Vehicle Name")
            print("2. Passenger Count (SQL)")
            print("3. Passenger Count (Bubble Sort)")

            sort_choice = input("Choose: ")

            if sort_choice == "1":
                sort_vehicle_name()

            elif sort_choice == "2":
                sort_passengers()

            elif sort_choice == "3":
                bubble_sort_passengers()

            else:
                print("Invalid sort choice!")

        else:
            print("Invalid choice!")


menu()
