import json
import requests
from flask import Flask

WMATA_API_KEY = "524b22577a1446a280052b064e0c18aa"
INCIDENTS_URL = "https://jhu-intropython-mod10.replit.app/"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}
app = Flask(__name__)
# your api key

@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
    ans = []
    res = requests.get(INCIDENTS_URL, headers=headers)
    if res.status_code == 200:
        data = res.json()
        for i in data.get('ElevatorIncidents', []):
            s1 = unit_type.lower()
            s2 = i.get('UnitType').lower() + 's'
            if s1 == s2:
                item = {
                    "StationCode": i.get("StationCode"),
                    "StationName": i.get("StationName"),
                    "UnitName": i.get("UnitName"),
                    "UnitType": i.get("UnitType")
                }
                ans.append(item)
    else:
        return json.dumps({"error": "Failed to retrieve data from WMATA API"}), 500
    return json.dumps(ans), 200


if __name__ == '__main__':
    app.run(debug=True, port=6001)
