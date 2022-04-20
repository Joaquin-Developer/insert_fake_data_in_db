# pylint: disable=broad-except
"""librería para hacer los insert genericos"""

from typing import Dict, List
from faker import Faker
import pymysql
import db_config


class NoHayQueryException(Exception):
    """Tipo de exception para cuando no hay query sql"""


class ScriptTemplate:
    """class for generic Scripts"""
    SQL_QUERY = None
    CONNECTION_PARAMS = None
    DATA_LENGTH = 100

    @classmethod
    def get_sql_query(cls, data: Dict = None) -> str:
        """string con la query a ejecutar"""
        if not cls.SQL_QUERY:
            raise NoHayQueryException("No hay SQL query.")

        if not data:
            return cls.SQL_QUERY

        # si algun campo es string, le agrego comillas
        for key in data.keys():
            if isinstance(data[key], str):
                data[key] = f"'{data[key]}'"

        fields = ",".join(field for field in data.keys())
        values = ",".join(data[field] for field in data.keys())

        return cls.SQL_QUERY.format(fields=fields, values=values)

    @classmethod
    def get_connection(cls) -> pymysql.Connection:
        """get connection object"""
        # config = connection_params or db_config
        config = cls.get_connection_params()

        try:
            return pymysql.connect(
                user=config.USERNAME,
                password=config.PASSWORD,
                host=config.HOST,
                database=config.DATABASE
            )
        except Exception as ex:
            raise ex

    @classmethod
    def query(cls, sql_query):
        """execute sql query"""
        connection = cls.get_connection()
        cursor = connection.cursor()
        cursor.execute(sql_query)
        cursor.close()
        connection.close()

    @classmethod
    def get_connection_params(cls):
        """
        - return a default connection parameters
        - CONNECTION_PARAMS debe ser un dict con los siguientes campos:
            USERNAME, PASSWORD, HOST, DATABASE
        """
        return cls.CONNECTION_PARAMS or db_config

    @classmethod
    def get_fake_data(cls) -> List[Dict]:
        """obtener los datos para luego insertarlos"""
        if not cls.DATA_LENGTH:
            cls.DATA_LENGTH = 100

        fake = Faker()
        return [fake.simple_profile() for i in range(cls.DATA_LENGTH)]

    @classmethod
    def insert_data(cls, data: List[Dict]):
        """para cada registro, se realiza el insert"""
        query = cls.SQL_QUERY
        if not query:
            raise Exception("No hay query SQL")

        for elem in data:
            try:
                query = cls.get_sql_query(elem)

                cls.query(query)

            except Exception as ex:
                print(ex)
                continue

    @classmethod
    def insert_person_generic(cls, person: Dict):
        """insert person in table PERSON, generic query"""

        cls.query(f"""
            INSERT INTO PERSON (username, name, mail, sex, birthdate, address)
            VALUES (
                '{person["username"]}',
                '{person["name"]}',
                '{person["mail"]}',
                '{person["sex"]}',
                '{person["birthdate"].strftime("%Y-%m-%d")}',
                '{person["address"]}'
            )
        """)

    @classmethod
    def main(cls):
        """main"""
        data = cls.get_fake_data()
        print("- Cargando datos")
        cls.insert_data(data)
        print("Datos cargados con éxito.")
