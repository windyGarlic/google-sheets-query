# google-sheets-to-graph
This python program gets data from google sheets and creates graphs using matplotlib. It is curently set to use scatter plot graphs, but can be changed.<br><br>


Enter values into the code e.g:<br>
![Screenshot from 2023-11-30 13-47-45](https://github.com/windyGarlic/google-sheets-query/assets/111098407/ff768b7b-f729-419e-be86-5578b2cf9073)

<br>

![Screenshot from 2023-11-30 13-48-23](https://github.com/windyGarlic/google-sheets-query/assets/111098407/486ce4e3-9751-428f-8a67-7c247eba2b84)


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
![image](https://github.com/windyGarlic/google-sheets-query/assets/111098407/9607b242-e8ec-41c2-b1b1-08e2288410bf)

