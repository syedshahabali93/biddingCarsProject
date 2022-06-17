import os
import requests
import requests.auth
from requests.structures import CaseInsensitiveDict
import json
from dotenv import load_dotenv
# from rauth import OAuth2Service

load_dotenv()


class GoogleSheet:
    def getAccessToken(self):
        url = "https://accounts.google.com/o/oauth2/token"
        payload = 'client_id=424096849316-akcvobcofdfrr53g1r6g8bl06na6qu7l.apps.googleusercontent.com&client_secret=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&refresh_token=1%2F%2F03HTLORGXZXnRCgYIARAAGAMSNwF-L9IrA7bMNAsqHOkINUR_qYZBKNHVWEbqGEErw1a4xrTyEV7L4NPnBEbcOLW3xUrJFInEgO4&grant_type=refresh_token'
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
        print("Updated Range: " + str(response_object['updates']['updatedRange']))
        print("Updated Rows: " + str(response_object['updates']['updatedRows']))
        print("Updated Columns: " + str(response_object['updates']['updatedColumns']))
        print("Updated Cells: " + str(response_object['updates']['updatedCells']))
