from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionNegotiatePrice(Action):
    def name(self) -> Text:
        return "action_negotiate_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        product = tracker.get_slot('product')
        user_offer = next(tracker.get_latest_entity_values("offer_price"), None)

        # Example product data (you should replace this with your own data)
        product_data = {
            "Samsung Galaxy S10": {"retail_price": 300, "min_price": 270},
            "iPhone 8": {"retail_price": 400, "min_price": 360}
        }

        if product in product_data:
            retail_price = product_data[product]["retail_price"]
            min_price = product_data[product]["min_price"]
            counter_offer = self.calculate_counter_offer(user_offer, retail_price, min_price)

            dispatcher.utter_message(text=f"How about {counter_offer} for the {product}?")
            return [SlotSet("counter_offer_price", counter_offer)]
        else:
            dispatcher.utter_message(text="Sorry, I don't have information about this product.")
            return []

    @staticmethod
    def calculate_counter_offer(user_offer, retail_price, min_price):
        # Initial counter offer is the retail price
        if user_offer >= retail_price:
            return retail_price
        else:
            # Gradually decrease the price, but never below the minimum
            decrement_factor = 5  # or any other factor you choose
            new_offer = retail_price - decrement_factor

            # Ensure the offer does not go below the minimum price
            if new_offer < min_price:
                return min_price
            else:
                return new_offer

