import pandas as pd

from ..base import BaseTableClient


class RegionsTableClient(BaseTableClient):
    def select_regions(self):
        query = "SELECT name FROM region;"
        result_df = pd.read_sql_query(query, self._connection)
        return result_df["name"].to_list()

    def select_region(self, name: str):
        query = f"SELECT id FROM region WHERE name='{name}';"
        result_df = pd.read_sql_query(query, self._connection)
        return result_df["id"][0]
