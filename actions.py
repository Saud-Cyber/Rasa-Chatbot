from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

career_data = {
    "Cybersecurity": {
        "course": "Certified Ethical Hacker (CEH), CISSP, CompTIA Security+",
        "salary": "₹6L–₹15L per annum",
        "certification": "CEH, CISSP, CompTIA Security+, OSCP"
    },
    "Data Science": {
        "course": "Data Science with Python, Machine Learning by Andrew Ng, R Programming",
        "salary": "₹7L–₹20L per annum",
        "certification": "Certified Data Scientist (CDS), IBM Data Science Professional"
    },
    "Business": {
        "course": "MBA, Business Analytics, Strategic Management",
        "salary": "₹5L–₹20L per annum",
        "certification": "MBA, Project Management Professional (PMP)"
    },
    "Marketing": {
        "course": "Digital Marketing, Marketing Analytics, Social Media Strategy",
        "salary": "₹3L–₹12L per annum",
        "certification": "Google Digital Marketing Certification, HubSpot Content Marketing"
    }
}

class ActionSubmitCareerForm(Action):
    def name(self) -> Text:
        return "action_submit_career_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        skill = tracker.get_slot('skill')
        interest = tracker.get_slot('interest')
        education = tracker.get_slot('education')
        suggestion = "Based on your profile, your options are: Cybersecurity, Data Science, Business, Marketing. You can ask for details, like 'Tell me about Cybersecurity'."
        dispatcher.utter_message(text=suggestion)
        dispatcher.utter_message(response="utter_ask_career_detail")
        return []

class ActionCareerDetails(Action):
    def name(self) -> Text:
        return "action_career_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        career = tracker.get_slot("career")
        if career:
            career_title = career.title()
            info = career_data.get(career_title)
            if info:
                msg = (
                    f"{career_title}:\n"
                    f"- Recommended courses: {info['course']}\n"
                    f"- Average salary: {info['salary']}\n"
                    f"- Certifications: {info['certification']}\n"
                )
            else:
                msg = "Sorry, I don't have detailed info for that career."
            dispatcher.utter_message(text=msg)
        else:
            dispatcher.utter_message(text="Please specify Cybersecurity, Data Science, Business, or Marketing.")
        return []
