"""script de prueba"""

import utils


class InsertData(utils.ScriptTemplate):
    """insertar data en la tabla de L216"""
    SQL_QUERY = """
        INSERT INTO USERS (username, mail, passw)
            VALUES (
                '{person["username"]}',
                '{person["name"]}',
                '{person["mail"]}',
                '{person["sex"]}',
                '{person["birthdate"].strftime("%Y-%m-%d")}',
                '{person["address"]}'
            )
    """


if __name__ == "__main__":
    InsertData.main()
