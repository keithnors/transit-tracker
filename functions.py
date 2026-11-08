import sqlite3

def connect_db():
    return sqlite3.connect("database/transit.db")

def search_route(route):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transit_records
        WHERE route LIKE ?
    """, ('%' + route + '%',))

    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("No routes found.")

    conn.close()


def search_vehicle(vehicle_name):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transit_records
        WHERE vehicle_name LIKE ?
    """, ('%' + vehicle_name + '%',))

    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("Vehicle not found.")

    conn.close()
    

def search_departure(departure_time):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transit_records
        WHERE departure_time = ?
    """, (departure_time,))

    records = cursor.fetchall()

    if records:
        for record in records:
            print(record)
    else:
        print("No departures found.")

    conn.close()


def sort_vehicle_name():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transit_records
        ORDER BY vehicle_name ASC
    """)

    records = cursor.fetchall()

    for record in records:
        print(record)

    conn.close()


def sort_passengers():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transit_records
        ORDER BY passengers DESC
    """)

    records = cursor.fetchall()

    for record in records:
        print(record)

    conn.close()


def bubble_sort_passengers():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transit_records")

    records = cursor.fetchall()

    n = len(records)

    for i in range(n):
        for j in range(0, n - i - 1):

            if records[j][5] > records[j + 1][5]:
                records[j], records[j + 1] = records[j + 1], records[j]

    for record in records:
        print(record)

    conn.close()

if __name__ == "__main__":
    print("Testing functions.py")
    #search_vehicle("Partas Express")
    #search_departure("8:00")
    #sort_vehicle_name()
    #sort_passengers()
    #bubble_sort_passengers()
    