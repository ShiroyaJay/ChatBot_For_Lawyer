# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
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

# actions/actions.py
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import openai


# class ActionFetchLawInfo(Action):
#     def name(self) -> Text:
#         return "action_fetch_law_info"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract the law topic from the user's message
#         law_topic = next(tracker.get_latest_entity_values("topic"), None)

#         if law_topic:
#             # Fetch information from the Indian law website using OpenAI's GPT-3
#             response = self.fetch_info_from_gpt3(law_topic)

#             dispatcher.utter_message(text=response)
#         else:
#             dispatcher.utter_message(text="I couldn't find a law topic in your message.")

#         return []

#     def fetch_info_from_gpt3(self, law_topic: str) -> str:
#         # Set up your OpenAI GPT-3 API key
#         openai.api_key = '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'

#         # Define the prompt for GPT-3
#         prompt = f"Retrieve information about Indian law related to {law_topic}"

#         # Use OpenAI GPT-3 to generate a response
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=prompt,
#             max_tokens=200
#         )

#         return response['choices'][0]['text']

# actions/actions.py
# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from openai import OpenAI


# import os

# class ActionFetchLawInfo(Action):
#     def name(self) -> Text:
#         return "action_fetch_law_info"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         # Extract the law topic from the user's message
#         user_message = tracker.latest_message.get('text',None)
#         print("User Message:", user_message)

#         if user_message:
#             # Fetch information from the Indian law website using OpenAI's GPT-3
#             response = self.fetch_info_from_gpt3(user_message)

#             dispatcher.utter_message(text=response)
#         else:
#             dispatcher.utter_message(text="I couldn't find a law topic in your message.")   

#         return []

#     def fetch_info_from_gpt3(self, user_message: str) -> str:
#         # Set up your OpenAI GPT-3 API key (use environment variable)
#         client = OpenAI(
#         # This is the default and can be omitted
#         api_key="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",
#         )

#         # Make an API request to G
        
#             # defaults to os.environ.get("OPENAI_API_KEY")
        
        
#         # if not api_key:
#         #     # Handle the case where the API key is not available
#         #     return "Error: OpenAI API key is missing."
       

#         # Define the URL of the Indian law website
#         indian_law_url = "https://blog.ipleaders.in/criminal-law-in-india/"  # Replace with the actual URL

#         # Define the prompt for GPT-3, including the URL
#         prompt = f"Retrieve information about Indian law related to {user_message} from {indian_law_url}"

#         try:
#             # Use OpenAI GPT-3 to generate a response
#             # response = client.completions.create(
#             #     model="gpt-3.5-turbo",  # Use the appropriate model name
#             #     messages=[
#             #         {"role": "system", "content": "You are a helpful assistant."},
#             #         {"role": "user", "content": prompt}
#             #     ]
#             # )
#             response = client.completions.create(
#                 engine="text-davinci-002",  # Use the appropriate engine name
#                 prompt=prompt,
#                 max_tokens=150  # Adjust as needed
#             )
            
#             return response['choices'][0]['text'].strip()
#             # return response['choices'][0]['message']['content']

#             # return response['choices'][0]['text']
#         except Exception as e:
#             # Handle any exceptions that may occur during the API call
#             return f"Error: {str(e)}"

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import openai

# openai.api_key = "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"

# class ActionFetchLawInfo(Action):
#     def name(self):
#         return "action_fetch_law_info"

#     def run(self, dispatcher, tracker, domain):
#         prompt = tracker.latest_message.get('text')
#         response = self.chatbot(prompt)
#         dispatcher.utter_message(text=response)

#     def chatbot(self, prompt):
#         response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=prompt,
#             temperature=0.7,
#             max_tokens=100,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#         return response.choices[0].text

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import openai
from openai import OpenAI



class ActionFetchLawInfo(Action):
    def name(self) -> Text:
        return "action_fetch_law_info"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = tracker.latest_message.get('text', None)
        print("User Message:", user_message)

        if user_message:
            response = self.fetch_info_from_gpt3(user_message)

            dispatcher.utter_message(text=response)
        else:
            dispatcher.utter_message(text="I couldn't find a law topic in your message.")

        return []

    def fetch_info_from_gpt3(self, user_message: str) -> str:
        api_key="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"
        client = OpenAI(api_key=api_key)

        # indian_law_url = "https://blog.ipleaders.in/criminal-law-in-india/"
        # prompt = f"Retrieve information about Indian law related to {user_message} from {indian_law_url}"
        prompt = f"Answer the following question only if it's related to Indian law: '{user_message}'. Otherwise, ask the user to provide a question about Indian law."

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use the appropriate model name
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            # return response['choices'][0]['message']['content']
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"