from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Credentials
import numpy as np
import matplotlib.pyplot as plt

# INSERT SPREADSHEET ID HERE
SPREADSHEET_ID = ''

# SET VARIABLES TO CREATE TABLE HERE #
sheet = ""
xlist_first_index = ""
xlist_second_index = ""
ylist_first_index = ""
ylist_second_index = ""
# Label variables
title = ""
xlabel = ""
ylabel = ""

# Supports bar, scatter, plot
graph = ""


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():
# Auth
    credentials = None
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)

# Starts sorting data
    try:
        Xaxis = get_data(credentials,sheet, xlist_first_index, xlist_second_index)
        Yaxis = get_data(credentials,sheet, ylist_first_index, ylist_second_index)
        Xaxislist = []
        YaxisList = []
        filteredIS = []
        filteredTE = []
        
        for innerList in Xaxis:
            try:
                if graph == 'scatter':
                    Xaxislist.append(int(innerList[0]))
                elif graph == 'bar':
                    Xaxislist.append(innerList[0])
            except:
                Xaxislist.append('0')
        for innerlist in Yaxis:
            try:
                YaxisList.append(int(innerlist[0]))        
            except:
                YaxisList.append('0')

# Removes outliers (change as needed)
        for x,y in zip(Xaxislist,YaxisList):
#            if int(y) <= 20000 and int(x) < 20000:
            filteredIS.append(x)
            filteredTE.append(y)

# Set labels and makes graph
        print(filteredIS)
        print("\n\n\n")
        print(filteredTE)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        if graph == 'scatter':
            plt.scatter(filteredIS, filteredTE)
        if graph == 'bar':
            plt.bar(filteredIS, filteredTE)
        if graph == 'plot':
            plt.plot(filteredIS, filteredTE)                    
        plt.show()

    except HttpError as error:
        print(error)

def get_data(credentials, SHEET_NAME, START_INDEX, END_INDEX):
    service = build('sheets', "v4", credentials=credentials)
    sheets = service.spreadsheets()
    result = sheets.values().get
    result = sheets.values().get(spreadsheetId=SPREADSHEET_ID, range=f"{SHEET_NAME}!{START_INDEX}:{END_INDEX}").execute()
    values = result.get('values', [])
    return values

main()
