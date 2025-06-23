import gspread
import json
import os
from google.oauth2 import service_account

SHEET_NAME = "Ayuvanaa Registrations"

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

service_account_info = json.loads(os.getenv("GOOGLE_CREDENTIALS"))
creds = service_account.Credentials.from_service_account_info(service_account_info)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

def append_to_sheet(row_data):
    sheet.append_row(row_data)
