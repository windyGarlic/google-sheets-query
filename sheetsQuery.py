from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Credentials


# INSERT SPREADSHEET ID HERE
SPREADSHEET_ID = '1lXXXXXXXXXXXXXXXXXXXXXXXXXXXXXcM'


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def connect():
    credentials = None
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)

    try:
        while True:
            print("This will get list's of the range you provide(first index - second index).\nType done to exit")
            counter = 1
            getInput = input("Sheet name: ")
            if getInput == "done":
                return False
            else:
                pass
            getInput2 = input("First index: ")
            if getInput2 == "done":
                return False
            else:
                pass
            getInput3 = input("Second index: ")
            if getInput3 == "done":
                return False
            else:
                pass
            var = doSomething(credentials, getInput, getInput2, getInput3)
            print(var)
        
    except HttpError as error:
        print(error)

def doSomething(credentials, SHEET_NAME, START_INDEX, END_INDEX):
    service = build('sheets', "v4", credentials=credentials)
    sheets = service.spreadsheets()
    result = sheets.values().get
    result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{SHEET_NAME}!{START_INDEX}:{END_INDEX}").execute()
    values = result.get('values', [])
    return values

connect()
