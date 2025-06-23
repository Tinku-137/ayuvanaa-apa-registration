import gspread
from google.oauth2 import service_account

# Load credentials from secrets.json file
creds = service_account.Credentials.from_service_account_file("secrets.json")

# Authenticate gspread with those credentials
client = gspread.authorize(creds)

# Open the Google Sheet
SHEET_NAME = "Ayuvanaa Registrations"  # make sure this matches your actual sheet name
sheet = client.open(SHEET_NAME).sheet1

def append_to_sheet(data: dict):
    values = list(data.values())
    sheet.append_row(values)
