import gspread
import json
import os
from google.oauth2 import service_account

SHEET_NAME = "Ayuvanaa Registrations"

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = service_account.Credentials.from_service_account_file("secrets.json")
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).sheet1

def append_to_sheet(row_data):
    sheet.append_row(row_data)
