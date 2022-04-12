from .main import GiveHelpMenu, HelpProposalMenu, HelpRequestMenu, LoginMenu, MainMenu, VolunteerRegisterMenu


class Keyboard:
    def __init__(self):
        self.__mainMenu = MainMenu()
        self.__login = LoginMenu()
        self.__helpRequestMenu = HelpRequestMenu()
        self.__helpProposalMenu = HelpProposalMenu()
        self.__volunteerRegisterMenu = VolunteerRegisterMenu()
        self.__give_help_menu = GiveHelpMenu()

    @property
    def mainMenu(self):
        return self.__mainMenu

    @property
    def helpRequestMenu(self):
        return self.__helpRequestMenu

    @property
    def helpProposalMenu(self):
        return self.__helpProposalMenu

    @property
    def login(self):
        return self.__login

    @property
    def volunteerRegisterMenu(self):
        return self.__volunteerRegisterMenu

    @property
    def giveHelpMenu(self):
        return self.__give_help_menu


keyboard = Keyboard()
