import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class GoogleSheet:
    def fetchSheetData(self):
        vin_numbers_list = []
        api = os.getenv('END_POINT')
        sheetID = os.getenv('SHEET_ID')
        sheetName = os.getenv('SHEET_NAME')
        range = os.getenv('RANGE')
        key = os.getenv('API_KEY')
        url = api + '/' + sheetID + '/' + 'values:batchGet?ranges=' + sheetName + range + '&key=' + key
        print(url)
        #    url1 = 'https://sheets.googleapis.com/v4/spreadsheets/1CvNA5p0dgmmcosOFvmDC9U1uNuHHk8F8FhRH7AMVrjU/values:batchGet?ranges=COPARTCARFAX!A141:AM&key=AIzaSyCyXD3Jwiw7lOuhOHgtlXNWjGMkJilEd3M'
        r = requests.get(url)
        data = r.json()

        # with open('values.json', 'r', encoding='utf-8') as f:
        #     data = json.load(f)

        records = data["valueRanges"][0]["values"]
        for r in records:
            if r:
                if r[6]:
                    vin_numbers_list.append(r[6])

        return vin_numbers_list

#
# p1 = GoogleSheet()
# print(p1.fetchSheetData())
