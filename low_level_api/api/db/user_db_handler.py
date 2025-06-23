import sqlite3 as sq
import os


def get_db_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "user.db")


def get_users():
    try:
        with sq.connect(get_db_path()) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user;")
            return cur.fetchall()
    except Exception as e:
        print("Error while getting users from DB:", e)
        return None


def get_user(id):
    try:
        id = int(id)
        if id <= 0:
            raise ValueError("Invalid user id")
        with sq.connect(get_db_path()) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM user WHERE id = ?;", (id,))
            return cur.fetchone()
    except Exception as e:
        print("Error while getting user from DB:", e)
        return None


def create_user(username, email, password):
    try:
        if not all([username, email, password]):
            raise ValueError("Invalid data")
        with sq.connect(get_db_path()) as con:
            cur = con.cursor()
            cur.execute("""
                INSERT INTO user (username, email, password)
                VALUES (?, ?, ?)
                RETURNING *;
            """, (username, email, password))
            return cur.fetchone()
    except Exception as e:
        print("Error occurred in DB while creating user:", e)
        return None


def edit_user(id, username, email, password):
    try:
        id = int(id)
        if id <= 0 or not all([username, email, password]):
            raise ValueError("Invalid data")
        with sq.connect(get_db_path()) as con:
            cur = con.cursor()
            cur.execute("""
                UPDATE user
                SET username = ?, email = ?, password = ?
                WHERE id = ?
                RETURNING *;
            """, (username, email, password, id))
            return cur.fetchone()
    except Exception as e:
        print("Error occurred in DB while editing user:", e)
        return None


def delete_user(id):
    try:
        id = int(id)
        if id <= 0:
            raise ValueError("Invalid user id")
        with sq.connect(get_db_path()) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM user WHERE id = ?;", (id,))
            return cur.rowcount > 0
    except Exception as e:
        print("Error while deleting user from DB:", e)
        return False
