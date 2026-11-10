import sqlite3
import csv
import shutil

# Connect to database
def connect_db():
    return sqlite3.connect("database/transit.db")


# Create table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transit_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_name TEXT NOT NULL,
        route TEXT NOT NULL,
        departure_time TEXT,
        arrival_time TEXT,
        passengers INTEGER
    )
    """)

    conn.commit()
    conn.close()


# CREATE
def add_record(vehicle_name, route,
               departure_time, arrival_time,
               passengers):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO transit_records
    (vehicle_name, route,
     departure_time, arrival_time,
     passengers)
    VALUES (?, ?, ?, ?, ?)
    """,
    (vehicle_name, route,
     departure_time, arrival_time,
     passengers))

    conn.commit()
    conn.close()

    print("Record added!")


# READ
def view_records():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transit_records")

    records = cursor.fetchall()

    if not records:
        print("No records found.")

    for record in records:
        print(
            f"ID: {record[0]} | "
            f"Vehicle: {record[1]} | "
            f"Route: {record[2]} | "
            f"Departure: {record[3]} | "
            f"Arrival: {record[4]} | "
            f"Passengers: {record[5]}"
        )

    conn.close()


# UPDATE
def update_record(record_id,
                  vehicle_name,
                  route,
                  departure_time,
                  arrival_time,
                  passengers):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE transit_records
    SET vehicle_name = ?,
        route = ?,
        departure_time = ?,
        arrival_time = ?,
        passengers = ?
    WHERE id = ?
    """,
    (vehicle_name,
     route,
     departure_time,
     arrival_time,
     passengers,
     record_id))

    conn.commit()
    conn.close()

    print("Record updated!")


# DELETE
def delete_record(record_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM transit_records
    WHERE id = ?
    """, (record_id,))

    conn.commit()
    conn.close()

    print("Record deleted!")



def record_exists(record_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM transit_records WHERE id = ?",
        (record_id,)
    )

    record = cursor.fetchone()

    conn.close()

    return record is not None



def export_csv():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM transit_records
    """)

    records = cursor.fetchall()

    with open(
        "database/transit_records.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Vehicle Name",
            "Route",
            "Departure Time",
            "Arrival Time",
            "Passengers"
        ])

        writer.writerows(records)

    conn.close()

    print(
        "CSV exported successfully!"
    )

def backup_database():

    shutil.copy(
        "database/transit.db",
        "database/backup.db"
    )

    print(
        "Database backup created!"
    )



if __name__ == "__main__":
    create_table()
    
    backup_database()

    
#export_csv()
#view_records()
#delete_record(1)
#update_record(
#    1,
#    "Victory Liner",
#    "Cauayan-Tuguegarao",
#    "09:00",
#    "13:00",
#    40
#)

