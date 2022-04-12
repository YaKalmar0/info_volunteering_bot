import pandas as pd

from ..base import BaseTableClient


class CitiesTableClient(BaseTableClient):
    def get_cities(self, region_id: int):
        query = f"SELECT name FROM city WHERE region_id = {region_id};"
        result_df = pd.read_sql_query(query, self._connection)
        return result_df["name"].to_list()
