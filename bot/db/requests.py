import sqlite3
from typing import List


def new_user(user_id: int, username: str, first_name: str, is_admin: str = 'no') -> None:
    """
    This function creates a new user in the database.
    :param user_id: The ID of the user (cannot be None).
    :param username: The username of the user.
    :param first_name: The first name of the user.
    :param is_admin: Whether the user is an admin ('yes' or 'no').
    :return: None
    """
    if not user_id:
        raise ValueError("user_id can't be None")
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        cursor.execute("""
                INSERT INTO users (user_id, username, user_first_name, is_admin)
                VALUES (?, ?, ?, ?)
            """, (user_id, username, first_name, is_admin))
        conn.commit()
    except Exception as e:
        print(f"Transaction failed: {e}")
    finally:
        conn.close()


def get_users() -> List[int]:
    """
    Fetches user IDs from the table in database.

    Return:
        List[int]: A list of user IDs.
    """
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT user_id FROM users')
        user_ids = cursor.fetchall()
        return [user_id[0] for user_id in user_ids]
    except Exception as e:
        print(f"Transaction failed: {e}")
    finally:
        conn.close()
