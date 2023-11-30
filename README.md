# google-sheets-to-graph
This python program gets data from google sheets and creates graphs using matplotlib. It is curently set to use scatter plot graphs, but can be changed.<br><br>


enter valuses into the code e.g:<br>
![Screenshot from 2023-11-30 13-47-45](https://github.com/windyGarlic/google-sheets-query/assets/111098407/ff768b7b-f729-419e-be86-5578b2cf9073)

<br>
![Screenshot from 2023-11-30 13-48-23](https://github.com/windyGarlic/google-sheets-query/assets/111098407/7558dca3-31b5-4ddc-abc5-1c6ec79e58ad)

<h2>Install</h2>

```
git clone https://github.com/windyGarlic/google-sheets-query

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib matplotlib numpy
```

<h2>Setup</h2>

To connect to the API you need a file called credentials.json in the same directory as the scripts. You can get that my creating a google project and getting a oauth2 client ID.

Create a project here: https://developers.google.com/workspace/guides/create-project

Once created, make an oauth2 client ID in the API tab. Save that as credentials.json in the same directory as the program.

You will also need to add your spreadsheet ID (The string after '/d/' in the google sheets url) to sheetsConnector.py 
![image](https://github.com/windyGarlic/butter/assets/111098407/c3ad50dc-71f8-43d5-bed3-a770ec470bc3)
