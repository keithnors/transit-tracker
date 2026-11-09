from database import *
from functions import *
from analytics import *

from functions import bubble_sort_passengers, search_departure, search_route, search_vehicle, sort_passengers, sort_vehicle_name

def get_passenger_input():

    while True:

        try:
            passengers = int(
                input("Passengers: ")
            )

            if passengers <= 0:
                print(
                    "Passengers must be a positive integer."
                )

            else:
                return passengers

        except ValueError:
            print(
                "Please enter numbers only."
            )

def get_required_input(message):

    while True:

        value = input(message).strip()

        if value == "":
            print(
                "This field cannot be empty."
            )

        else:
            return value


def main_menu():

    create_table()

    while True:

        print("\n==============================")
        print("     TRANSIT TRACKER")
        print("==============================")

        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Search Records")
        print("6. Sort Records")
        print("7. Analytics")
        print("8. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_menu()

        elif choice == "2":
            view_records()

        elif choice == "3":
            update_menu()

        elif choice == "4":
            delete_menu()

        elif choice == "5":
            search_menu()

        elif choice == "6":
            sort_menu()

        elif choice == "7":
            analytics_menu()

        elif choice == "8":
            print("Thank you for using Transit Tracker!")
            break

        else:
            print("Invalid Choice.")


def add_menu():

    vehicle_name = input("Vehicle Name: ")
    route = input("Route: ")
    departure_time = input("Departure Time: ")
    arrival_time = input("Arrival Time: ")

    passengers = int(
        input("Passengers: ")
    )

    add_record(
        vehicle_name,
        route,
        departure_time,
        arrival_time,
        passengers
    )

def update_menu():

    record_id = int(
    input("Record ID: ")
    )

    if not record_exists(record_id):
        print("Record ID does not exist.")
        return
    vehicle_name = input(
        "Vehicle Name: "
    )

    route = input(
        "Route: "
    )

    departure_time = input(
        "Departure Time: "
    )

    arrival_time = input(
        "Arrival Time: "
    )

    passengers = int(
        input("Passengers: ")
    )

    update_record(
        record_id,
        vehicle_name,
        route,
        departure_time,
        arrival_time,
        passengers
    )

def delete_record(record_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM transit_records
        WHERE id = ?
        """,
        (record_id,)
    )

    if cursor.rowcount == 0:
        print("No matching record found.")
    else:
        print("Record deleted!")

    conn.commit()
    conn.close()

def delete_menu():

    record_id = int(
        input("Record ID to Delete: ")
    )

    if not record_exists(record_id):
        print("Record ID does not exist.")
        return

    confirm = input(
        "Are you sure? (Y/N): "
    ).upper()

    if confirm == "Y":
        delete_record(record_id)
    else:
        print("Delete cancelled.")

def search_menu():

    while True:

        print("\n===== SEARCH MENU =====")
        print("1. Search Route")
        print("2. Search Vehicle")
        print("3. Search Departure")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":

            route = input(
                "Enter Route: "
            )

            search_route(route)

        elif choice == "2":

            vehicle = input(
                "Enter Vehicle Name: "
            )

            search_vehicle(vehicle)

        elif choice == "3":

            departure = input(
                "Enter Departure Time: "
            )

            search_departure(departure)

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

def sort_menu():

    while True:

        print("\n===== SORT MENU =====")
        print("1. Sort Vehicle Name")
        print("2. Sort Passenger Count")
        print("3. Bubble Sort")
        print("4. Back")

        choice = input("Choose: ")

        if choice == "1":

            sort_vehicle_name()

        elif choice == "2":

            sort_passengers()

        elif choice == "3":

            bubble_sort_passengers()

        elif choice == "4":
            break

        else:
            print("Invalid Choice")

def analytics_menu():

    while True:

        print("\n===== ANALYTICS =====")

        print("1. Total Passengers")
        print("2. Average Passengers")
        print("3. Most Used Route")
        print("4. Most Used Vehicle")
        print("5. Route Statistics")
        print("6. Back")

        choice = input("Choose: ")

        if choice == "1":

            total_passengers()

        elif choice == "2":

            average_passengers()

        elif choice == "3":

            most_used_route()

        elif choice == "4":

            most_used_vehicle()

        elif choice == "5":

            route_statistics()

        elif choice == "6":
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main_menu()