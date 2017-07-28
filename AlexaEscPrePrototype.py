"""
Arrow ESC Alexa Integration
Author: Jonathan Yost
This program/script/word-thing is to be used by the Arrow ESC to show Arrow's Alexa integration functionality.

Backup: Before prototype

"""

from __future__ import print_function

import json
import boto3
import re

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

def build_sound_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak> This output speech uses SSML </speak>""
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
    speech_output = "Hello and, again, welcome to the Aperture Science computer-aided enrichment center."

    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Hello? Is anyone there?"

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "The talking is over"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

# ---------------------------------------------------------------
# -------------------- No man's land ----------------------------



# ---------------- Handle requests to node data -----------------

def convert_to_known_type(measurement_type):
    if(measurement_type == "temperature"):
        return "temp"
    else:
        return measurement_type

def unit_specific_response(measurement_type, node_id, sensor_data):
    if measurement_type == "temp":
        return "The temperature is " + sensor_data + " degrees fahrenheit at " + node_id

    elif measurement_type == "humidity":
        return "The humidity at " + node_id + " is " + sensor_data + " percent"

    elif measurement_type == "pressure":
        return "The pressure at " + node_id + " is " + sensor_data + " pascals"

    elif measurement_type == "uv" or measurement_type == "ultraviolet":
        return node_id + " scored a whopping " + sensor_data + " on the UV index"

    elif measurement_type == "ir" or measurement_type == "infrared":
        return "I don't quite know what this means, but there were " + sensor_data + " IR units at " + node_id

    elif measurement_type == "visible":
        return "I don't quite know what this means, but there were " + sensor_data + " brightness units at " + node_id

    elif measurement_type == "noise":
        return "The volume is approximately " + sensor_data + " noise units at " + node_id

    else:
        return " Well, this is embarrassing. I didn't understand you..."

def get_env_data_specific(intent, session):
    """ Called when the user asks for env data"""
    session_attributes = {}
    reprompt_text = None
    bucket = "arrowesciottest"
    key = "data1.json"

    measurement_type = intent['slots']['MeasurementType']['value']
    measurement_type = measurement_type.lower()
    measurement_type = measurement_type.replace("-", "")
    measurement_type = convert_to_known_type(measurement_type)

    disp_id = intent['slots']['NodeID']['value']

    # Decrement the node number by 1
    node_id = 'node' + str(int(re.findall("\d+", disp_id)[0])-1)

    node_id = node_id.lower()

    try:
        response = s3.get_object(Bucket=bucket, Key=key) #returns the data1.json file as an object
    except Exception as e:
        print(e)
        print("Error getting object {} from bucket {}." .format(key, bucket))
        raise e

    # Read in the data and decode it
    read_data = response['Body'].read().decode('utf-8')

    # Parse the json file into a dictionary data structure
    parsed_data = json.loads(read_data)

    should_end_session = True

    disp_id = 'node ' + str(disp_id)

    try:
        sensor_data = parsed_data[node_id][measurement_type][-1]
    except Exception as e:
        shucks_output = "Whoops. There appears to be no valid " + str(measurement_type) + " data at " + disp_id

        return build_response(session_attributes, build_speechlet_response(
        intent['name'], shucks_output, reprompt_text, should_end_session))

    speech_output = unit_specific_response(measurement_type, str(disp_id), str(sensor_data))

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_individual_skittle_count(intent, session):
    """ Called when the user asks for a specific number of skittles """
    session_attributes = {}
    reprompt_text = None
    bucket = "arrowesciottest"
    key = "data1.json"

    skittle_color = intent['slots']['Color']['value']


    # skittle order: orange, yellow, green, purple, red
    if skittle_color == "orange":
        read_index = 0
    elif skittle_color == "yellow":
        read_index = 1
    elif skittle_color == "green":
        read_index = 2
    elif skittle_color == "purple":
        read_index = 3
    elif skittle_color == "reed" or skittle_color == "red" or skittle_color == "read":
        # Alexa cannot seem to understand me when I say 'red', so I have to check for a lot more options.
        read_index = 4
        skittle_color = "red"
    else:
        read_index = 5 # breaks the code.. watch out. spooky


    try:
        response = s3.get_object(Bucket=bucket, Key=key) #returns the data1.json file as an object
    except Exception as e:
        print(e)
        print("Error getting object {} from bucket {}." .format(key, bucket))
        raise e

    # Read in the data and decode it
    read_data = response['Body'].read().decode('utf-8')

    # Parse the json file into a dictionary data structure
    parsed_data = json.loads(read_data)

    should_end_session = False

    skittle_count = 0

    try:
        sensor_data = parsed_data['industrial']['levels'][read_index]
    except Exception as e:
        shucks_output = "Well shit. We couldn't find the number of " + str(skittle_color) + " skittles."

        return build_response(session_attributes, build_speechlet_response(
        intent['name'], shucks_output, reprompt_text, should_end_session))

    speech_output = "There are " + str(sensor_data) + " " + str(skittle_color) + " skittles"
    should_end_session = True

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


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
    """ This function is extremely important, do not remove. """
    session_attributes = {}
    reprompt_text = None

    speech_output = " Were no strangers to love."\
        " You know the rules and so do I. "\
        " A full commitments what Im thinking of. "\
        " You wouldnt get this from any other guy"

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

def get_ballmer(intent, session):
    """ This function is extremely important, do not remove. """
    session_attributes = {}
    reprompt_text = None

    speech_output = "DEVELOPERS "

    for i in range(0, 14):
        speech_output += "DEVELOPERS "

    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

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

def get_mp3(intent,session):
    """
    Call Phrase: TalkingOver
    """
    session_attributes = {}
    reprompt_text = None

    speech_output = "Trying to use the SSML Stuff"

    should_end_session = False
    return build_response(session_attributes, build_sound_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

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
    if intent_name == "GetEnvData":
        return get_env_data_specific(intent, session)

    elif intent_name == "WhatsTheSkittleCount":
        return get_individual_skittle_count(intent, session)

    elif intent_name == "OriginStory":
        return get_mordor(intent, session)

    elif intent_name == "AllStar":
        return get_smash(intent, session)

    elif intent_name == "JohnsSong":
        return get_johns_song(intent, session)

    elif intent_name == "DevelopersDevelopersDevelopers":
        return get_ballmer(intent, session)

    elif intent_name == "PlaySoundFile":
        return get_mp3(intent, session)

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
