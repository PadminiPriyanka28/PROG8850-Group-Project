import mysql.connector
import random
from datetime import datetime, timedelta

# DB Config
db_config = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "Root@1234",
    "database": "project_db"
}

# Generate Random Climate Data
def generate_fake_data(n=1000):
    locations = ["Toronto", "Ottawa", "Vancouver", "Calgary", "Montreal", "Halifax"]
    start_date = datetime(2023, 1, 1)
    data = []

    for _ in range(n):
        location = random.choice(locations)
        date = start_date + timedelta(days=random.randint(0, 365))
        temperature = round(random.uniform(-10.0, 35.0), 2)
        precipitation = round(random.uniform(0.0, 50.0), 2)
        humidity = round(random.uniform(30.0, 100.0), 2)
        data.append((location, date.strftime('%Y-%m-%d'), temperature, precipitation, humidity))

    return data

# Insert Data into DB
def insert_data():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    sql = "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES (%s, %s, %s, %s, %s)"
    values = generate_fake_data(1000)

    cursor.executemany(sql, values)
    db.commit()
    print(f"✅ Inserted {cursor.rowcount} rows into ClimateData")
    cursor.close()
    db.close()

if __name__ == "__main__":
    insert_data()
