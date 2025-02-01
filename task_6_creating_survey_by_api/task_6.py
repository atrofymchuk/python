#!/usr/bin/env python3
"""
This script uses the Survey Monkey (https://www.surveymonkey.com) service creates a survey
and sends an invitation to go through it.
"""
import http.client
import json
import argparse
import os


access_token = os.environ.get("SURVEY_TOKEN")
headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f"Bearer {access_token}"
}

conn = http.client.HTTPSConnection("api.surveymonkey.com")

def create_survey(name_survey):
    """
    This function takes one argument "name of survey", creates survey,
    returns response for POST /surveys
    """
    conn.request("POST", "/v3/surveys", name_survey, headers)
    res = conn.getresponse()
    data_create_survey = res.read()
    data_create_survey_1 = data_create_survey.decode("utf-8")
    return data_create_survey_1


def create_pages(name_page, survey_id_1):
    """
    This function takes two arguments "name of page, survey id", creates name page, returns response
    for POST /surveys/{id}/pages
    """
    url = f"/v3/surveys/{survey_id_1}/pages"
    conn.request("POST", url, name_page, headers)
    res = conn.getresponse()
    data_create_pages = res.read()
    data_create_pages_1 = data_create_pages.decode("utf-8")
    return data_create_pages_1


def create_question(question, survey_id_1, page_id_1):
    """
    This function takes three arguments "question, survey id, page id",
    creates a new question on a survey page
    """
    url = f"/v3/surveys/{survey_id_1}/pages/{page_id_1}/questions"
    conn.request("POST", url, question, headers)
    res = conn.getresponse()
    data_create_question = res.read()
    print(data_create_question.decode("utf-8"))


def create_list(name_contact_list):
    """
    This function takes one argument "name contact list", creates a new contact list,
    returns response for POST /contact_lists
    """
    conn.request("POST", "/v3/contact_lists", name_contact_list, headers)
    res = conn.getresponse()
    data_create_list = res.read()
    print(data_create_list.decode("utf-8"))
    data_create_list_1 = data_create_list.decode("utf-8")
    return data_create_list_1

def create_contacts(contacts, list_id_1):
    """
    This function takes two arguments "contact, list id", creates a new contact.
    """
    url = f"/v3/contact_lists/{list_id_1}/contacts"
    conn.request("POST", url, contacts, headers)
    res = conn.getresponse()
    data_contact = res.read()
    print(data_contact.decode("utf-8"))

def create_collector(colector_name):
    """
    This function takes one argument "collector name", creates a new collector.
    """
    url = f"/v3/surveys/{survey_id}/collectors"
    conn.request("POST", url, colector_name, headers)
    res = conn.getresponse()
    data_collector = res.read()
    print(data_collector.decode("utf-8"))

parser = argparse.ArgumentParser(description='Script reads JSON file and emails from file')
parser.add_argument('filename', help="Name of JSON file")
parser.add_argument('email', help="Name of file with email")
args = parser.parse_args()

with open(args.filename, 'r', encoding='utf-8') as file:
    data = json.load(file)
    for x, y in data.items():
        dict_survey = {"title": x}
        answer = create_survey(json.dumps(dict_survey))
        answer_python = json.loads(answer)
        survey_id = answer_python["id"]
        for c, v in y.items():
            dict_pagename = {"title": c, "description": "", "position": 1}
            answer_2 = create_pages(json.dumps(dict_pagename), survey_id)
            answer_python_2 = json.loads(answer_2)
            pagename_id = answer_python_2["id"]
            i = 1
            for q, w in v.items():
                list_question = []
                list_question.append(q)
                for e, r in w.items():
                    list_question.append(r)
                i += 1
                dict_question = {"family": "single_choice","subtype": "vertical",
                                 "answers": {"choices": [{"text": list_question[2][0],
                                 "position": 1},{"text": list_question[2][1],
                                 "position": 2},{"text": list_question[2][2],
                                 "position": 3}]},"headings": [{"heading": list_question[0]}],
                                 "position": i}
                create_question(json.dumps(dict_question), survey_id, pagename_id)

#Create contact list
print("Creating contact list:")
dict_name_list = {"name":"My contact list"}
name_list = create_list(json.dumps(dict_name_list))
answer_name_list = json.loads(name_list)
list_id = answer_name_list["id"]

#Create collector
print("Creating collector:")
collector_name = {"type":"weblink","name":"Test collector"}
create_collector(json.dumps(collector_name))

#Create contacts
print("Creating contacts:")
with open(args.email, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    j = 0
    for line in lines:
        list_email = lines[j]
        STR_EMAIL = str(list_email)
        EMAIL = STR_EMAIL.rstrip()
        dict_contact = {"first_name": "Test", "last_name": "Test", "email": EMAIL,
                        "phone_number": "", "custom_fields": {}}
        create_contacts(json.dumps(dict_contact), list_id)
        j += 1
