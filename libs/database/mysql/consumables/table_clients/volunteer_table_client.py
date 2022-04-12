from ..base import BaseTableClient


class VolunteerTableClient(BaseTableClient):
    def create_volunteer(self, people_id: int, data: dict):
        with self._connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO volunteer (people_id, i_can_do, military, medical,"
                " city, district, region, address, other_help) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (
                    people_id,
                    data.get("i_can_do"),
                    data.get("mil_exp"),
                    data.get("med_exp"),
                    data.get("city"),
                    data.get("district"),
                    data.get("region"),
                    data.get("address"),
                    data.get("other_help"),
                ),
            )
            self._connection.commit()
