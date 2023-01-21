import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('test')

user = SHEET.worksheet('user')


def get_info():
    """ Get user info
    """
    data_str = input("Enter your data here? \n")
    print((f"The data provided is {data_str}"))
    return data_str


def update_user_worksheet(data):
    """
    Update user worksheet
    """
    print("Updating sales worksheet....\n")
    user_worksheet = SHEET.worksheet("user")
    user_worksheet.append_row(data)


data = get_info()

update_user_worksheet(data)