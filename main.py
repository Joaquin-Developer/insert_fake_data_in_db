"""insertar datos de prueba a la base"""

from typing import Dict, List
from faker import Faker
import database

def get_fake_data(length=10):
    """obtener los datos para luego insertarlos"""
    fake = Faker()
    return [fake.simple_profile() for i in range(length)]


def insert_data(data: List[Dict]):
    """para cada registro, se realiza el insert"""
    for elem in data:
        database.insert_person(elem)


if __name__ == "__main__":
    insert_data(get_fake_data(length=200))
