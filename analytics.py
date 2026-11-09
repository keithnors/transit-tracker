import sqlite3

def connect_db():
    return sqlite3.connect("database/transit.db")

def total_passengers():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(passengers)
        FROM transit_records
    """)

    total = cursor.fetchone()[0]

    if total is None:
        total = 0

    print(f"Total Passengers: {total}")

    conn.close()

def average_passengers():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(passengers)
        FROM transit_records
    """)

    average = cursor.fetchone()[0]

    if average is None:
        average = 0

    print(f"Average Passengers: {average:.2f}")

    conn.close()

def most_used_route():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT route,
               SUM(passengers) AS total_passengers
        FROM transit_records
        GROUP BY route
        ORDER BY total_passengers DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    if result:
        print(f"Most Used Route: {result[0]}")
        print(f"Total Passengers: {result[1]}")
    else:
        print("No records found.")

    conn.close()

def most_used_vehicle():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT vehicle_name,
               SUM(passengers)
        FROM transit_records
        GROUP BY vehicle_name
        ORDER BY SUM(passengers) DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    if result:
        print(f"Most Used Vehicle: {result[0]}")
        print(f"Passengers Served: {result[1]}")

    else:
        print("No records found.")

    conn.close()


def route_statistics():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT route,
               COUNT(*),
               SUM(passengers),
               AVG(passengers)
        FROM transit_records
        GROUP BY route
    """)

    results = cursor.fetchall()

    if not results:
        print("No route data found.")

    for route in results:

        print("\n-----------------------")
        print(f"Route: {route[0]}")
        print(f"Trips: {route[1]}")
        print(f"Total Passengers: {route[2]}")
        print(f"Average Passengers: {route[3]:.2f}")

    conn.close()


def peak_travel_hours():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT departure_time,
               COUNT(*)
        FROM transit_records
        GROUP BY departure_time
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)

    result = cursor.fetchone()

    if result:
        print(f"Peak Travel Hour: {result[0]}")
        print(f"Number of Trips: {result[1]}")
    else:
        print("No records found.")

    conn.close()


def top_5_routes():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT route,
               SUM(passengers)
        FROM transit_records
        GROUP BY route
        ORDER BY SUM(passengers) DESC
        LIMIT 5
    """)

    routes = cursor.fetchall()

    print("\nTOP 5 BUSIEST ROUTES")

    for index, route in enumerate(routes, start=1):
        print(
            f"{index}. {route[0]} "
            f"({route[1]} passengers)"
        )

    conn.close()



####TESTING LANG PO ITO HINDI ITO YONG MAIN.py

if __name__ == "__main__":

    print("\nANALYTICS TEST MENU")
    print("1. Total Passengers")
    print("2. Average Passengers")
    print("3. Most Used Route")
    print("4. Most Used Vehicle")
    print("5. Route Statistics")
    print("6. Peak Travel Hours")
    print("7. Top 5 Routes")

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
        peak_travel_hours()

    elif choice == "7":
        top_5_routes()

