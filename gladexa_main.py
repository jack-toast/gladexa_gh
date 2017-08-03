"""
Gladexa Main Lambda Function
Author: Jonathan Yost

This thingydo is the main brains of the Gladexa project.

"""

from __future__ import print_function

import json
import boto3
import re
import random

s3 = boto3.client('s3')

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_sound_response(title, speech_output, card_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': speech_output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + card_output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# --------------- Hello and Goodbye Functions ------------------

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_00_part1_entry-1.mp3"/></speak>'
    card_output = 'playing GLaDOS_00_part1_entry-1.mp3'
    reprompt_text = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_escape_01_part1_nag05-1.mp3"/></speak>'
    should_end_session = False
    return build_response(session_attributes, build_sound_response(
        card_title, speech_output, card_output, reprompt_text, should_end_session))

def handle_session_end_request():
    session_attributes = {}
    card_title = "Session Ended"
    speech_output = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_15_part1_into_the_fire-5.mp3"/></speak>'
    card_output = 'playing GLaDOS_00_part1_entry-1.mp3'
    reprompt_text = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_escape_01_part1_nag05-1.mp3"/></speak>'
    should_end_session = True
    return build_response(session_attributes, build_sound_response(
        card_title, speech_output, card_output, reprompt_text, should_end_session))

# ---------------------------------------------------------------



# -------------------- No man's land ----------------------------



# ---------------------- Very serious code below -------------------------------

def get_smash(intent, session):
    """ This function is extremely important, do not remove. """
    session_attributes = {}
    reprompt_text = None

    speech_output = "Somebody once told me the world is gonna roll me."\
        " I aint the sharpest tool in the shed. "\
        " She was looking kind of dumb with her finger and her thumb, "\
        " In the shape of an L on her forehead"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_johns_song(intent, session):
    session_attributes = {}
    card_title = "Rick Astley"
    speech_output = '<speak><audio src="https://s3.amazonaws.com/arrowesciottest/Rick+Astley+-+Never+Gonna+Give+You+Up.mp3"/></speak>'
    card_output = 'playing Ricky the kid'
    reprompt_text = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_escape_01_part1_nag05-1.mp3"/></speak>'
    should_end_session = False
    return build_response(session_attributes, build_sound_response(
        card_title, speech_output, card_output, reprompt_text, should_end_session))


def get_mordor(intent, session):
    """
    Call phrase: "[OriginStory] your origin story"
    """

    session_attributes = {}
    reprompt_text = None

    speech_output = "Now, the Elves made many rings, but secretly Sauron made " \
    "One Ring to rule all the others, and their power was bound up with it, " \
    "to be subject wholly to it and to last only so long as it too should last. "

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def get_fact(intent, session):
    session_attributes = {}
    card_title = "InterestingFact"
    reprompt_text = None

    if(intent['slots']['FactName']['value'] == None):
        fact_name == donating
    else:
        fact_name = str(intent['slots']['FactName']['value']).lower()

    if fact_name == 'air':
        # air
        speech_output = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_fact_air.mp3"/></speak>'
    elif fact_name == 'donating':
        # organ
        speech_output = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_fact_organs.mp3"/></speak>'
    elif fact_name == 'people':
        # train
        speech_output = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_fact_train.mp3"/><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_fact_train2.mp3"/></speak>'
    else:
        # invalid datar
        speech_output = '<speak><audio src="https://s3.amazonaws.com/glados-home-automation/GLaDOS_15_part1_into_the_fire-5.mp3"/></speak>'

    card_output = 'portal facts'
    should_end_session = True
    return build_response(session_attributes, build_sound_response(
        card_title, speech_output, card_output, reprompt_text, should_end_session))


# --------------------------------- Events -------------------------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "OriginStory":
        return get_mordor(intent, session)

    elif intent_name == "AllStar":
        return get_smash(intent, session)

    elif intent_name == "JohnsSong":
        return get_johns_song(intent, session)

    elif intent_name == "InterestingFact":
        return get_fact(intent, session)

    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()

    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()

    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    """
    if (event['session']['application']['applicationId'] !=
             "amzn1.ask.skill.f34782b4-d823-4091-86e6-66472ae6ff02"):
         raise ValueError("Invalid Application ID")
    """

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
