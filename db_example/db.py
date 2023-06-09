import sqlite3


def create_table():
    connection = sqlite3.connect("cinema.db")
    connection.execute(
        """
        CREATE TABLE "Seat" (
            "seat_id"	TEXT,
            "taken"	INTEGER,
            "price"	REAL
        );
        """
    )
    connection.commit()
    connection.close()


def insert_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute(
        """
        INSERT INTO "Seat" ("seat_id","taken","price") VALUES ("A11" ,"0" , "90"), ("A2" ,"1" , "100"), ("A3" ,"0" , "80")
        """
    )
    connection.commit()
    connection.close()


def select_all():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM "Seat" 
        """
    )
    result = cursor.fetchall()
    connection.close()
    return result


def select_specific_columns():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT "seat_id", "price" FROM "Seat"
        """
    )
    result = cursor.fetchall()
    connection.close()
    return result


def select_with_condition():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT "seat_id", "price" FROM "Seat" WHERE "price">=50
        """
    )
    result = cursor.fetchall()
    connection.close()
    return result


def update_value(occupied, seat_id):
    connection = sqlite3.connect("cinema.db")
    connection.execute(
        """
        UPDATE "Seat" SET "taken"=? WHERE "seat_id"=?
        """,
        [occupied, seat_id],
    )
    connection.commit()
    connection.close()


def delete_record():
    connection = sqlite3.connect("cinema.db")
    connection.execute(
        """
        DELETE FROM "Seat" WHERE "seat_id"="A3"
        """
    )
    connection.commit()
    connection.close()


def check_taken_status_based_seat_id():
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT "taken" FROM "Seat" WHERE "seat_id"="A4"
        """
    )
    result = cursor.fetchall()
    connection.close()
    return result[0][0]


print(check_taken_status_based_seat_id())
