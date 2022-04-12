from ..base import BaseHelpMenu, create_inline_keyboard
from .constants import help_types_btns, help_types_calls, transfer_types_btns, transfer_types_calls
from .help_proposal_button_texts import HelpProposalButtonTexts as ButtonTexts


class HelpProposalMenu(BaseHelpMenu):
    def __init__(self):
        super().__init__()

        self.__inline_transfer_possibility = create_inline_keyboard(
            transfer_types_btns, transfer_types_calls, ButtonTexts.callback_data_prefix_transfer
        )

        self.__help_inline_keyboard = create_inline_keyboard(
            help_types_btns, help_types_calls, prefix=ButtonTexts.callback_data_prefix_for_help
        ).add(self._own_help)

    @property
    def help_inline_keyboard(self):
        return self.__help_inline_keyboard

    @property
    def transfer_inline_keyboard(self):
        return self.__inline_transfer_possibility
