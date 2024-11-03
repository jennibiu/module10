from wmata_api import app
import json
import unittest


class WMATATest(unittest.TestCase):
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        self.assertEqual(escalator_response, 200, "Expected /incidents/escalators to return 200 OK")
        elevator_response = app.test_client().get('/incidents/elevators').status_code
        self.assertEqual(elevator_response, 200, "Expected /incidents/elevators to return 200 OK")

    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]
        res = app.test_client().get('/incidents/escalators')
        json_response = json.loads(res.data.decode())
        for incident in json_response:
            for f_item in required_fields:
                self.assertIn(f_item, incident, f"Expected field {f_item} in escalator incidents")
        res = app.test_client().get('/incidents/elevators')
        json_response = json.loads(res.data.decode())
        for item in json_response:
            for f_item in required_fields:
                self.assertIn(f_item, item, f"Expected field {f_item} in elevator incidents")

    def test_escalators(self):
        res = app.test_client().get('/incidents/escalators')
        json_response = json.loads(res.data.decode())
        for item in json_response:
            self.assertEqual(item.get("UnitType").upper(), "ESCALATOR",
                             "Expected UnitType to be ESCALATOR in escalator incidents")

    def test_elevators(self):
        res = app.test_client().get('/incidents/elevators')
        json_response = json.loads(res.data.decode())
        for incident in json_response:
            self.assertEqual(incident.get("UnitType").upper(), "ELEVATOR",
                             "Expected UnitType to be ELEVATOR in elevator incidents")


if __name__ == "__main__":
    unittest.main()
