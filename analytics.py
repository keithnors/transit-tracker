import sqlite3
import matplotlib.pyplot as plt

def connect_db():
    return sqlite3.connect("database/transit.db")


def vehicle_usage_chart():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT vehicle_name,
               COUNT(*)
        FROM transit_records
        GROUP BY vehicle_name
    """)

    results = cursor.fetchall()

    conn.close()

    vehicles = []
    trips = []

    for row in results:
        vehicles.append(row[0])
        trips.append(row[1])

    plt.figure(figsize=(8, 5))

    plt.bar(
        vehicles,
        trips,
        color="green"
    )

    plt.title("Vehicle Usage")
    plt.xlabel("Vehicle")
    plt.ylabel("Trips")

    plt.tight_layout()

    plt.savefig("charts/vehicle_chart.png")

    plt.show()

    print("Vehicle chart saved!")


def passenger_bar_chart():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT vehicle_name,
               SUM(passengers)
        FROM transit_records
        GROUP BY vehicle_name
    """)

    results = cursor.fetchall()

    conn.close()

    vehicles = []
    passengers = []

    for row in results:
        vehicles.append(row[0])
        passengers.append(row[1])

    plt.figure(figsize=(8, 5))
    bars = plt.bar(
    vehicles,
    passengers,
    color="royalblue"
)
    for bar in bars:

        height = bar.get_height()

    plt.text(
        bar.get_x() +
        bar.get_width()/2,

        height,

        str(height),

        ha='center'
    )

    plt.title("Passengers per Vehicle")
    plt.xlabel("Vehicle")
    plt.ylabel("Passengers")

    plt.tight_layout()

    plt.savefig("charts/passenger_chart.png")

    plt.show()

    print("Passenger chart saved!")


def route_comparison_chart():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT route,
           SUM(passengers)
    FROM transit_records
    GROUP BY route
    """)

    data = cursor.fetchall()

    conn.close()

    routes = [
        x[0]
        for x in data
    ]

    passengers = [
        x[1]
        for x in data
    ]

    plt.figure(
        figsize=(9, 5)
    )

    plt.barh(
        routes,
        passengers,
        color="green"
    )

    plt.xlabel("Passengers")

    plt.ylabel("Routes")

    plt.title(
        "Route Comparison"
    )

    plt.tight_layout()

    plt.savefig(
        "charts/route_comparison.png"
    )

    plt.show()

def route_pie_chart():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT route,
               SUM(passengers)
        FROM transit_records
        GROUP BY route
    """)

    results = cursor.fetchall()

    conn.close()

    routes = []
    values = []

    for row in results:
        routes.append(row[0])
        values.append(row[1])

    plt.figure(figsize=(7, 7))

    plt.pie(
        values,
        labels=routes,
        autopct="%1.1f%%"
    )

    centre_circle = plt.Circle(
    (0, 0),
    0.70,
    fc='white'
    )

    fig = plt.gcf()

    fig.gca().add_artist(
    centre_circle
    )
        
    plt.title("Route Distribution")

    plt.savefig("charts/route_chart.png")

    plt.show()

    print("Route chart saved!")

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

    results = cursor.fetchall()

    print(
        "\nTOP 5 BUSIEST ROUTES"
    )

    for i, route in enumerate(results, start=1):

        print(
            f"{i}. {route[0]} "
            f"({route[1]} passengers)"
        )

    conn.close()

def dashboard_summary():

    print("\n========== TRANSIT SUMMARY ==========")

    total_passengers()

    average_passengers()

    most_used_route()

    most_used_vehicle()

    peak_travel_hours()

    print("=====================================")


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
    print("8. Passenger Bar Chart")
    print("9. Route Comparison Chart")
    print("10. Route Pie Chart")
    print("11. Vehicle Usage Chart")
    print("12. Transit Summary")
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

    elif choice == "8":
        passenger_bar_chart()

    elif choice == "9":
        route_comparison_chart()

    elif choice == "10":
        route_pie_chart()

    elif choice == "11":
        vehicle_usage_chart()

    elif choice == "12":
        dashboard_summary()