"""modulo para ejecutar queries a una DB"""
from typing import Dict
import pymysql
import db_config


def get_connection() -> pymysql.Connection:
    """get connection object"""
    try:
        return pymysql.connect(
            user=db_config.USERNAME,
            password=db_config.PASSWORD,
            host=db_config.HOST,
            database=db_config.DATABASE
        )
    except Exception as ex:
        raise ex


def query(sql_query: str):
    """execute sql query"""
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(sql_query)
    cursor.close()
    connection.close()


def insert_person(person: Dict):
    """insert person in table PERSON"""
    query(f"""
        INSERT INTO PERSON (username, name, mail, sex, birthdate, address)
        VALUES (
            '{person.username}',
            '{person.name}',
            '{person.mail}',
            '{person.sex}',
            '{person["birthdate"].strftime("%Y-%m-%d")}',
            '{person.address}'
        )
    """)
