from dotenv import load_dotenv
import os

load_dotenv()

USERS = {
    "Gabriel": {
        "sheet_key": os.getenv("USER_1_SHEET_KEY")
    },
    "Rebeca": {
        "sheet_key": os.getenv("USER_2_SHEET_KEY")
    }
}


def get_user_sheet(name: str):
    return USERS.get(name)