import sqlite3 as sq
import os


def get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "user.db")


def main():
    db_path = get_db_path()
    with sq.connect(db_path) as con:
        cur = con.cursor()
        try:
            cur.execute("""
                CREATE TABLE user(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                );
            """)
            print("DB created successfully")
        except Exception as e:
            print("Error creating DB")
            return e


if __name__ == "__main__":
    main()
