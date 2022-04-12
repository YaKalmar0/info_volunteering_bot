from ..base import BaseTableClient


class OfferHelpTableClient(BaseTableClient):
    def create_offer_help_request(self, human_id: int, data: dict):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO offer_help (people_id, help_type, description, pay_method,"
                " delivery, organization, city, district, region, address, other_help) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    human_id,
                    data.get("help_type"),
                    data.get("help_details"),
                    data.get("payment"),
                    data.get("transfer"),
                    "none",
                    data.get("city"),
                    data.get("district"),
                    data.get("region"),
                    data.get("address"),
                    data.get("other_help"),
                ),
            )
            self._connection.commit()
