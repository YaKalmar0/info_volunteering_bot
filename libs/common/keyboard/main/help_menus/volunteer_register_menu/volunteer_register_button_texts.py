from ..base import BaseHelpButtonTexts


class VolunteerRegisterButtonTexts(BaseHelpButtonTexts):
    other_help = "інше"
    other_help_callback = "other_help"

    callbackd_data_i_can_do_prefix = "i_"

    military_experience_present_prefix = "mil_"
    military_experience_present = "Маю"
    military_experience_present_callback = military_experience_present_prefix + "1"

    military_experience_missing = "Не Маю"
    military_experience_missing_callback = military_experience_present_prefix + "0"

    medical_experience_present_prefix = "med_"
    medical_experience_present = "Маю"
    medical_experience_present_callback = medical_experience_present_prefix + "1"

    medical_experience_missing = "Не Маю"
    medical_experience_missing_callback = medical_experience_present_prefix + "0"
