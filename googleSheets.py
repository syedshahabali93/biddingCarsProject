import os
import requests
import requests.auth
from requests.structures import CaseInsensitiveDict
import json
from dotenv import load_dotenv

load_dotenv()


class GoogleSheet:
    def getAccessToken(self):
        url = "https://accounts.google.com/o/oauth2/token"
        client_id = os.getenv('CLIENT_ID')
        client_secret = os.getenv('CLIENT_SECRET')
        refresh_token = os.getenv('REFRESH_TOKEN')
        grant_type = os.getenv('GRANT_TYPE')
        payload = "client_id="+client_id+"&client_secret="+client_secret+"&refresh_token="+refresh_token+"&grant_type="+grant_type+""
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        json_object = json.loads(response.text)
        token = json_object['access_token']
        return token

    def uploadToSheet(self, payload):
        api = os.getenv('END_POINT')
        payload = json.dumps(payload)
        sheetID = os.getenv('SHEET_ID')
        valueInputOption = os.getenv('VALUE_INPUT_OPTION')
        includeValuesInResponse = os.getenv('INCLUDE_VALUE_IN_RESPONSE')
        responseValueRenderOption = os.getenv('RESPONSE_VALUE_RENDER_OPTION')
        insertDataOption = os.getenv('INSERT_DATA_OPTION')
        range = os.getenv('RANGE')
        token = self.getAccessToken()
        headers = CaseInsensitiveDict()
        headers['Authorization'] = 'Bearer ' + token
        headers['Content-Type'] = 'application/json'
        url = api + '/' + sheetID + '/values/' + range + ':append?valueInputOption=' + valueInputOption + '&includeValuesInResponse=' + includeValuesInResponse + '&responseValueRenderOption=' + responseValueRenderOption + '&insertDataOption=' + insertDataOption
        response = requests.post(url, headers=headers, data=payload)
        response_object = json.loads(response.text)
        print(response_object)
        print("Updated Range: " + str(response_object['updates']['updatedRange']))
        print("Updated Rows: " + str(response_object['updates']['updatedRows']))
        print("Updated Columns: " + str(response_object['updates']['updatedColumns']))
        print("Updated Cells: " + str(response_object['updates']['updatedCells']))

    def readFromSheet(self):
        dates_List = []
        api = os.getenv('END_POINT')
        sheetID = os.getenv('SHEET_ID')
        sheetName = os.getenv('SHEET_NAME_READ')
        range = os.getenv('RANGE_READ')
        key = os.getenv('API_KEY')
        url = api + '/' + sheetID + '/' + 'values:batchGet?ranges=' + sheetName + range + '&key=' + key
        response = requests.get(url)
        data = response.json()
        records = data["valueRanges"][0]["values"]
        for row in records:
            date = {}
            if row:
                try:
                    date['year'] = row[9]
                    date['make'] = ((row[10].lower()).title())
                    date['model'] = ((row[11].lower()).title())
                    date['vin'] = row[8]
                    dates_List.append(date)
                except IndexError:
                    continue
        return dates_List
