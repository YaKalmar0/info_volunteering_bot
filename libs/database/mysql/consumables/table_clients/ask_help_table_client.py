from ..base import BaseTableClient


class AskHelpTableClient(BaseTableClient):
    def create_ask_for_help_request(self, human_id: int, data: dict):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO ask_help (people_id, help_type, description, can_pay,"
                " can_pick_up, organization, city, district, region, address, other_help) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    human_id,
                    data.get("help_type"),
                    data.get("help_details"),
                    data.get("payment"),
                    0,
                    "none",
                    data.get("city"),
                    data.get("district"),
                    data.get("region"),
                    data.get("address"),
                    data.get("other_help"),
                ),
            )
            self._connection.commit()
