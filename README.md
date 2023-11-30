# google-sheets-query
This python program gets data from google sheets pages and outputs as a list.<br><br>
![image](https://github.com/windyGarlic/google-sheets-query/assets/111098407/a299aa05-6883-4099-8d84-23ac87328448)

<h3>Notes</h3>  
- Sheet-To-Graph README.md is in the graph branch <br>
- sheet is the name of the specific sheet tab (bottom left). 
<h2>Install</h2>
```
git clone https://github.com/windyGarlic/google-sheets-query

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

<h2>Setup</h2>

To connect to the API you need a file called credentials.json in the same directory as the scripts. You can get that my creating a google project and getting a oauth2 client ID.

Create a project here: https://developers.google.com/workspace/guides/create-project

Once created, make an oauth2 client ID in the API tab. Save that as credentials.json in the same directory as the program.

You will also need to add your spreadsheet ID (The string after '/d/' in the google sheets url) to sheetsConnector.py 
![image](https://github.com/windyGarlic/butter/assets/111098407/c3ad50dc-71f8-43d5-bed3-a770ec470bc3)
