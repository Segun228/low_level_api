import sqlite3 as sq
import os


def get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "user.db")


def drop_user_db():
    db_path = get_db_path()
    with sq.connect(db_path) as con:
        cur = con.cursor()
        try:
            cur.execute("""
                DROP TABLE IF EXISTS user;
            """)
            print("DB dropped successfully")
        except Exception as e:
            print("Error dropping DB")
            return e


if __name__ == "__main__":
    drop_user_db()
