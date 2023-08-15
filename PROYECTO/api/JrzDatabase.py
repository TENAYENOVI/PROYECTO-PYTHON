# %%
import sqlite3
import csv

def create_ranking_table():
    conn = sqlite3.connect("Jrz.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS ranking(
                   id INTEGER PRIMARY KEY,
                   artist TEXT NOT NULL,
                   song TEXT NOT NULL,
                   position INTEGER NOT NULL
                   )
                   """)
    
    conn.commit()
    conn.close()


# %%
def read_csv_file(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def insert_data_to_ranking_table(data):
    conn = sqlite3.connect("hot100.db")
    cursor = conn.cursor()

    for row in data:
        cursor.execute("""
            INSERT INTO ranking (artist, song, position)
            VALUES (?, ?, ?)
        """, (row["Artist"], row["Song"], int(row["Position"])))

    conn.commit()
    conn.close()

# %%
if __name__ == "__main__":
    csv_file = "Billboard Hot 100-07-08-2023.csv"
    data_to_insert = read_csv_file(csv_file)
    insert_data_to_ranking_table(data_to_insert)

# %%
if __name__ == "__main__":
    create_ranking_table()
# %%
