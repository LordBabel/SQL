import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('cars.db')
cursor = conn.cursor()

# Create a table to store car data
cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    manufacturer TEXT,
                    price REAL,
                    top_speed REAL
                )''')

# Create a table to store car colors or modifications
cursor.execute('''CREATE TABLE IF NOT EXISTS car_details (
                    id INTEGER PRIMARY KEY,
                    car_id INTEGER,
                    detail_type TEXT,
                    detail_value TEXT,
                    FOREIGN KEY (car_id) REFERENCES cars(id)
                )''')

# Define the data about the cars
cars_data = [
    ("Bugatti La Voiture Noire", "Bugatti", 19000000, 261),
    ("Pagani Zonda HP Barchetta", "Pagani", 17600000, 338),
    ("Rolls-Royce Sweptail", "Rolls-Royce", 13000000, 0),  # Top speed unknown
    ("Koenigsegg CCXR Trevita", "Koenigsegg", 4800000, 254),
    ("Lamborghini Veneno Roadster", "Lamborghini", 4000000, 221),
    ("Lykan HyperSport", "W Motors", 3400000, 245),
    ("McLaren P1 LM", "McLaren", 3500000, 214),
    ("Ferrari Pininfarina Sergio", "Ferrari", 3000000, 206),
    ("Limited Edition Bugatti Veyron by Mansory Vivere", "Bugatti", 3000000, 255),
    ("Aston Martin Valkyrie", "Aston Martin", 3000000, 250),
    ("Ferrari LaFerrari Aperta", "Ferrari", 3000000, 217),
    ("Zenvo ST1", "Zenvo", 1800000, 233),
    ("Aston Martin One-77", "Aston Martin", 1750000, 220),
    ("Ferrari LaFerrari", "Ferrari", 1400000, 217),
    ("McLaren Speedtail", "McLaren", 2134000, 250),
    ("Porsche 918 Spyder", "Porsche", 845000, 214),
    ("Bugatti Chiron", "Bugatti", 3000000, 261),
    ("Lamborghini Sian", "Lamborghini", 3200000, 217),
    ("Ferrari SF90 Stradale", "Ferrari", 625000, 211),
    ("Koenigsegg Jesko", "Koenigsegg", 2795000, 300)
    # Add more cars here...
]

# Insert data into the 'cars' table
for car in cars_data:
    cursor.execute("INSERT INTO cars (name, manufacturer, price, top_speed) VALUES (?, ?, ?, ?)", car)

# Define the data about car colors or modifications
car_details_data = [
    (1, "color", "Black"),
    (1, "trim", "Gold"),
    (2, "color", "Blue"),
    (2, "modification", "Carbon Fiber Body Kit"),
    (3, "color", "Silver"),
    (4, "color", "White"),
    (5, "color", "Green"),
    (6, "color", "Red"),
    (7, "color", "Yellow"),
    (8, "color", "Blue"),
    (9, "color", "Red"),
    (10, "color", "Yellow"),
    (11, "color", "Blue"),
    (12, "color", "Black"),
    (13, "color", "Red"),
    (14, "color", "Orange"),
    (15, "color", "Yellow"),
    (16, "color", "Silver"),
    (17, "color", "Blue"),
    (18, "color", "Green"),
    (19, "color", "Red"),
    (20, "color", "Black"),
    # Add more car details here...
]

# Insert data into the 'car_details' table
for detail in car_details_data:
    cursor.execute("INSERT INTO car_details (car_id, detail_type, detail_value) VALUES (?, ?, ?)", detail)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data inserted successfully!")
