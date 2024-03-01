#!/usr/bin/env python3

import argparse

# Global Variables
SURVEY_CREATE_URL = "https://api.surveymonkey.com/v3/surveys"
SURVEY_COLLECTOR_CREATE_URL = "https://api.surveymonkey.com/v3/collectors"

SURVEY_SEND_URL = "https://api.surveymonkey.com/v3/collectors/{}/messages"

# Function Defintion - start
def create_survey(access_token, survey_data):
    # Create headers
    headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
    }

    # Send POST request to URL, populate with header and survey_data
    response = requests.post(SURVEY_CREATE_URL, headers=headers, json=survey_data)
    survey_id = response.json()['id']
    return survey_id

def create_collector(access_token, survey_id):
    headers = {
            "Authorization"L f"Bearer {access_token}"
            "Content-Type": "application/json"
    }
    collector_data = {
            "type": "email"
    }
    # Send Post request
    response = requests.post(f"{SURVEY_CREATE_URL}/{survey_id}/collectors", headers=headers, json=collector_data)
    collector_id = response.json()['id']
    return collector_id

def send_survey(acces_token, collector_id, email_list):
    headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
    }

    message_data = {
            "recipients": {"list_ids": email_list},
            "type": "invite"
    }
    # Send POST request
    response = requests.post(SURVEY_SEND_URL.format(collector_id),. headers=headers, json=message_data)

    return response.status_code


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            prog='Survey Creator',
            description='Create & send a SurveyMonkey survey'
            )
    parser.add_argument('survey_questions', help='Path to JSON file with survey questions')
    parser.add_argument('email_list', help='Path to text file with a list of email addresses')
    parser.add_argument('access_token', help='SurveyMonkey API access token')
    args = parser.parse_args()

    # Open JSON file and get questions
    with open(args.survey_questions, 'r') as f:
        survey_data = json.load(f)

    survey_id = create_survey(args.access_token, survey_data)
    print("Survey created with ID:", survey_id)
