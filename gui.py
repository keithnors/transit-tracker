import customtkinter as ctk
from database import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")




app = ctk.CTk()

app.title("Transit Tracker Dashboard")
app.geometry("1000x500")

# Sidebar
sidebar = ctk.CTkFrame(
    app,
    width=250
)

sidebar.pack(
    side="left",
    fill="y"
)

title = ctk.CTkLabel(
    sidebar,
    text="Transit Tracker",
    font=("Aptos", 24, "bold")
)

title.pack(
    pady=25
)

# Main Content
content = ctk.CTkFrame(app)

content.pack(
    side="right",
    fill="both",
    expand=True
)

stats_frame = ctk.CTkFrame(content)

stats_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

card1 = ctk.CTkLabel(
    stats_frame,
    text="Total Records\n0",
    font=("Aptos", 18)
)

card1.pack(
    side="left",
    padx=20
)

stats_frame = ctk.CTkFrame(content)

stats_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

card2 = ctk.CTkLabel(
    stats_frame,
    text="Total Passengers\n0",
    font=("Aptos", 18)
)

card2.pack(
    side="left",
    padx=20
)

stats_frame = ctk.CTkFrame(content)

stats_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

card3 = ctk.CTkLabel(
    stats_frame,
    text="Most Used Routes\n0",
    font=("Aptos", 18)
)

card3.pack(
    side="left",
    padx=20
)

stats_frame = ctk.CTkFrame(content)

stats_frame.pack(
    fill="x",
    padx=20,
    pady=20
)

card4 = ctk.CTkLabel(
    stats_frame,
    text="Most Used Vehicle\n0",
    font=("Aptos", 18)
)

card4.pack(
    side="left",
    padx=20
)

records_frame = ctk.CTkFrame(content)

records_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

table_title = ctk.CTkLabel(
    records_frame,
    text="Transit Records",
    font=("Aptos",20)
)

table_title.pack(
    pady=20
)

#Sidebar Navigation
dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Dashboard",
    command=view_records
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Manage Records"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Search Records"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Analytics"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Charts"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Export CSV"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

dashboard_btn = ctk.CTkButton(
    sidebar,
    text="Backup Database"
)

dashboard_btn.pack(
    fill="x",
    padx=10,
    pady=5
)

exit_btn = ctk.CTkButton(
    sidebar,
    text="Exit",
    command=app.destroy,
    fg_color="red"
)

exit_btn.pack(
    fill="x",
    padx=10,
    pady=5
)


table_title.pack(
    pady=20
)
records_box = ctk.CTkTextbox(
    records_frame,
    width=900,
    height=400
)

records_box.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)


def show_records():

    records_box.delete(
        "1.0",
        "end"
    )

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM transit_records"
    )

    records = cursor.fetchall()

    conn.close()

    for record in records:

        records_box.insert(
            "end",
            str(record) + "\n"
        )



app.mainloop()