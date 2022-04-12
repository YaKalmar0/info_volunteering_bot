import json

import pandas as pd

from ..base import BaseTableClient


class PeopleTableClient(BaseTableClient):
    def human_exists(self, telegram_id) -> bool:
        query = f"SELECT * FROM people WHERE telegram_id = {telegram_id};"
        result_df = pd.read_sql_query(query, self._connection)
        human_exists = not result_df.empty
        return human_exists

    def create_human(self, telegram_id: int, full_name: str, role: str, phone_list):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO people (role, telegram_id, full_name, phone_list) VALUES(%s, %s, %s, %s);",
                (role, telegram_id, full_name, json.dumps(phone_list)),
            )
            self._connection.commit()

    def get_human(self, telegram_id: int):
        query = f"SELECT * FROM people WHERE telegram_id={telegram_id};"
        result_df = pd.read_sql_query(query, self._connection)
        return result_df

    def get_human_phone_list(self, telegram_id: int):
        query = f"SELECT phone_list FROM people WHERE telegram_id={telegram_id};"
        result_df = pd.read_sql_query(query, self._connection)
        json_dict = json.loads(result_df["phone_list"][0])
        return json_dict

    def get_human_id(self, telegram_id: int):
        query = f"SELECT id FROM people WHERE telegram_id={telegram_id};"
        result_df = pd.read_sql_query(query, self._connection)
        return result_df["id"][0]

    def update_human_phone_list(self, telegram_id: int, phone_list):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "UPDATE people SET phone_list=%s WHERE telegram_id=%s;", (json.dumps(phone_list), telegram_id)
            )
            self._connection.commit()

    def update_human_full_name(self, telegram_id: int, full_name: str):
        with self._connection.cursor() as cursor:
            cursor.execute("UPDATE people SET full_name=%s WHERE telegram_id=%s;", (full_name, telegram_id))
            self._connection.commit()

    def update_human_role(self, telegram_id: int, role: str):
        with self._connection.cursor() as cursor:
            cursor.execute("UPDATE people SET role=%s WHERE telegram_id=%s;", (role, telegram_id))
            self._connection.commit()
