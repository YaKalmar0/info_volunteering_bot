from .consumables import (
    AskHelpTableClient,
    BaseDataBase,
    CitiesTableClient,
    OfferHelpTableClient,
    PeopleTableClient,
    RegionsTableClient,
    VolunteerTableClient,
)


class DataBase(BaseDataBase):
    def __init__(self):
        super().__init__()

    @property
    def people_table(self):
        return PeopleTableClient(self._connection)

    @property
    def volunteer_table(self):
        return VolunteerTableClient(self._connection)

    @property
    def ask_help_table(self):
        return AskHelpTableClient(self._connection)

    @property
    def offer_help_table(self):
        return OfferHelpTableClient(self._connection)

    @property
    def regions_table(self):
        return RegionsTableClient(self._connection)

    @property
    def cities_table(self):
        return CitiesTableClient(self._connection)
