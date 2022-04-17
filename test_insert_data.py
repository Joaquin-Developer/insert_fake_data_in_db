"""script de prueba"""

from typing import Dict
import utils


class InsertData(utils.ScriptTemplate):
    """insertar data en la tabla de L216"""

    SQL_QUERY = """
        INSERT INTO USERS (mail, username) VALUES ({values})
    """

    CONNECTION_PARAMS = {
        "USERNAME": "root",
        "PASSWORD": "",
        "HOST": "127.0.0.1",
        "DATABASE": "l216_dev_3"
    }

    @classmethod
    def get_sql_query(cls, data: Dict = None) -> str:
        """string con la query a ejecutar"""
        # mail, username
        final_data = {
            "mail": f"""'{data["mail"]}'""",
            "username": f"""'{data["username"]}'"""
        }

        return cls.SQL_QUERY.format(values=",".join(final_data[field] for field in final_data))


if __name__ == "__main__":
    InsertData.main()
