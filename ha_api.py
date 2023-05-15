""" API calls to Home Assistant."""
import configparser
import requests
import models

class HomeAssistantApi: # pylint: disable=too-few-public-methods
    """Home Assistant API class."""

    api_url = ""
    api_token = ""

    def __init__(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read("settings.ini")

        self.api_url = config["home_assistant"]["api_url"]
        self.api_token = config["home_assistant"]["api_token"]

    def get_states(self) -> list[models.HaSensor]:
        """Get all states from Home Assistant."""
        items = []
        try:
            response = requests.get(
                self.api_url + "/api/states",
                headers={
                    "Authorization": "Bearer " + self.api_token,
                    "Content-Type": "application/json"
                },
                timeout=5 # seconds
            )

            json = response.json()
            items = []

            for entity in json:
                # Skip non sensor entities
                if not entity["entity_id"].startswith("sensor"):
                    continue

                sensor = models.HaSensor(
                    entityId=entity["entity_id"],
                    friendlyName=entity["attributes"]["friendly_name"],
                    state=entity["state"]
                )
                items.append(sensor)
        except requests.exceptions.RequestException as err:
            print(err)
            return []
        return items
    