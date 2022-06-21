import os
import time

import requests
import json
from dotenv import load_dotenv
from requests.structures import CaseInsensitiveDict

load_dotenv()


class GoogleSheet:
    def fetchSheetData(self, rowNumber):
        vin_numbers_list = []
        api = os.getenv('END_POINT')
        sheetID = os.getenv('SHEET_ID')
        sheetName = os.getenv('SHEET_NAME_READ')
        range = '!I'+str(rowNumber)+':J'+str(rowNumber)
        key = os.getenv('API_KEY')
        # url = api + '/' + sheetID + '/' + 'values:batchGet?ranges=' + sheetName + range + '&key=' + key
        url = api + '/' + sheetID + '/' + 'values/' + sheetName + range + '?key=' + key
        r = requests.get(url)
        data = r.json()
        record = {}
        if "values" in data:
            if data["values"][0][0]:
                record["vin"] = data["values"][0][0]
                record["range"] = data["range"]
        else:
            record["vin"] = "vin_not_exists"
        # for r in records:
        #     if r:
        #         vin_numbers_list.append(r[0])
        return record

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

    def uploadToSheet(self, prices, range, row_number):
        api = os.getenv('END_POINT')
        sheetID = os.getenv('SHEET_ID')
        valueInputOption = os.getenv('VALUE_INPUT_OPTION')
        includeValuesInResponse = os.getenv('INCLUDE_VALUE_IN_RESPONSE')
        responseValueRenderOption = os.getenv('RESPONSE_VALUE_RENDER_OPTION')
        responseDateTimeRenderOption = os.getenv('RESPONSE_DATE_TIME_RENDER_OPTION')
        majorDimension = os.getenv('MAJOR_DIMENSION')
        range = 'COPARTCARFAX!Y'+str(row_number)+':Z'
        payload = {
            "valueInputOption": valueInputOption,
            "includeValuesInResponse": includeValuesInResponse,
            "responseValueRenderOption": responseValueRenderOption,
            "responseDateTimeRenderOption": responseDateTimeRenderOption,
            "data": [
                {
                    "range": range,
                    "majorDimension": majorDimension,
                    "values": [[prices[0], prices[1]]]
                }
            ]

        }
        print(payload)
        payload = json.dumps(payload)
        token = self.getAccessToken()
        headers = CaseInsensitiveDict()
        headers['Authorization'] = 'Bearer ' + token
        headers['Content-Type'] = 'application/json'
        url = api + '/' + sheetID + '/values/:batchUpdate'
        response = requests.post(url, headers=headers, data=payload)
        response_object = json.loads(response.text)
        # print(response_object)
        print("Updated Range: " + str(response_object['responses'][0]['updatedRange']))
        print("Updated Rows: " + str(response_object['responses'][0]['updatedRows']))
        print("Updated Columns: " + str(response_object['responses'][0]['updatedColumns']))
        print("Updated Cells: " + str(response_object['responses'][0]['updatedCells']))
