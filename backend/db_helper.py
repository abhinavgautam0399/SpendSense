import mysql.connector
from contextlib import contextmanager
import os
import logging


logger = logging.getLogger("db_helper")
logger.setLevel(logging.INFO)


@contextmanager
def get_db_cursor(commit=False):
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        cursor = connection.cursor(dictionary=True)
        yield cursor

        if commit:
            connection.commit()

    except Exception as e:
        if connection:
            connection.rollback()
        logger.error(f"DB ERROR: {e}")
        raise e

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



def fetch_expenses_for_date(expense_date):
    logger.info(f"Fetching expenses for date: {expense_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM expenses WHERE expense_date = %s
            """,
            (expense_date.strftime("%Y-%m-%d"),)
        )
        expenses = cursor.fetchall()

    return expenses



def delete_expenses_for_date(expense_date):
    logger.info(f"Deleting expenses for date: {expense_date}")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            DELETE FROM expenses WHERE expense_date = %s
            """,
            (expense_date.strftime("%Y-%m-%d"),)
        )



def insert_expense(expense_date, amount, category, notes):
    logger.info(f"Inserting expense for date: {expense_date}")

    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            """
            INSERT INTO expenses (expense_date, amount, category, notes)
            VALUES (%s, %s, %s, %s)
            """,
            (expense_date, amount, category, notes)
        )



def fetch_expense_summary(start_date, end_date):
    logger.info(f"Fetching summary from {start_date} to {end_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            """
            SELECT category, SUM(amount) AS total
            FROM expenses
            WHERE expense_date BETWEEN %s AND %s
            GROUP BY category
            """,
            (start_date, end_date)
        )

        data = cursor.fetchall()

    return data



if __name__ == "__main__":
    print("DB helper loaded successfully")