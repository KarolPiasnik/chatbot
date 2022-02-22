# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import json

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
class action_menu(Action):

    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        f = open("data/menu.json")

        data = json.load(f)
        result = ""
        result += "Menu is as below:\n"

        for i in data["items"]:
            result += i["name"] + ":\n" + "\tprice: " + str(i["price"]) + "PLN\n\tpreparation time: " + str(i["preparation_time"]*60) + " minutes\n"
        dispatcher.utter_message(text=result)

        return []

class ActionOpeningHours(Action):

    def name(self) -> Text:
        return "action_opening_hours"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        f = open("data/opening_hours.json")

        data = json.load(f)
        result = ""
        result += "Opening hours are as below:\n"

        for i in data["items"]:
            result += i + ": " + str(data["items"][i]["open"]) + ":00 - " + str(data["items"][i]["open"])+":00\n"
        dispatcher.utter_message(text=result)

        return []
