# Gladexa = GLaDOS + Alexa

### Quick Links:
- [Amazon Lambda](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
  - [Boto 3 Documentation](https://boto3.readthedocs.io/en/latest/)
- [Amazon Alexa Skills Kit](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/getting-started-guide)
  - [Understanding Custom Skills](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/overviews/understanding-custom-skills)
- [Amazon Simple Storage Service](https://aws.amazon.com/documentation/s3/)
- [GLaDOS Voice Lines](https://theportalwiki.com/wiki/GLaDOS_voice_lines)
- [Decypher Media (AlwaysBCoding) Alexa Lambda Tutorial](https://www.youtube.com/watch?v=zt9WdE5kR6g&t=697s)

### What does this skill do?
- Recites the opening lyrics to the song "Allstar" (Alexa Voice)
- Tells the user how the one ring was made (Alexa Voice)
- Rick-rolls (Actual song MP3)
- Tells specific Portal quotes (GLaDOS voice)

#### Example Phrases:
- "Alexa, ask glados to tell me your favorite poem"
- "Alexa, ask glados to tell me your origin story"
- "Alexa, ask glados to play johns favorite song"
- "Alexa, ask glados to play some tunes"
- "Alexa, ask glados to tell me the interesting fact about (air, people, donating)"

### How it all works
![Main Diagram](https://github.com/jack-toast/gladexa/blob/master/images/overview%20diagram.png?raw=true)

#### The three main components:
- The Alexa skill / Echo itself
- The Lambda function that handles all of our processing and routing
- The S3 backend that holds all of our data

## Setting up the Alexa Skill
### 1. [Amazon Developer console](https://developer.amazon.com/) >> Sign In
### 2. Alexa Tab >> Alexa Skills Kit >> **Get Started**
![Circled for ya](https://github.com/jack-toast/gladexa/blob/master/images/ASK%20get%20started.png?raw=true)
### 3. Add a new skill ![Clickety Clack](https://github.com/jack-toast/gladexa/blob/master/images/addnewskill%20copy.PNG?raw=true)
### 4. Skill Information
  - Skill Type: Custom Interaction Model
  - Language: English (U.S. or U.K.) or German
  - Name: Whatever you want. This will show in the Alexa store thing if you publish the skill. I'm not publishing, so I named it for my own organization.
  - Invocation Name: I used "glados". Make sure it's something that the Alexa voice engine can understand phonetically
  - Global Fields: Ignore
  - Click *next*
![Skill Information](https://github.com/jack-toast/gladexa/blob/master/images/Skill%20Information.png?raw=true)

### 5. Interaction Model

![InteractionModelScreenGrab](https://github.com/jack-toast/gladexa/blob/master/images/InteractionModel.PNG?raw=true)

#### What it do?

The interaction model describes how our speech is parsed into a command message that is sent to the Lambda function.

The **Intents**, **Slot values**, and **Utterances** control the message that is sent.

Let's take an example command and break it down.

*"Alexa, ask glados to tell me the interesting fact about air"*

Alexa, | ask | glados | to | tell me an interesting fact about | air
------|-----|--------|----|-----------------------------------|------
Wake word | Linker | Invocation Name | Linker | Specifies the intent | Slot value

The skill parses the above phrase and sends a JSON message to the Lambda function.

By saying this phrase the following JSON message is sent:

```json
{
  "session": {
    "sessionId": "SessionId.UNIQUE_SESSION_ID",
    "application": {
      "applicationId": "amzn1.ask.skill.YOUR_APPLICATON_ID"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.YOUR_ACCOUNT_ID_WILL_SHOW_UP_HERE"
    },
    "new": true
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.UNIQUE_REQUEST_ID",
    "locale": "en-US",
    "timestamp": "2017-07-31T00:34:01Z",
    "intent": {
      "name": "InterestingFact",
      "slots": {
        "FactName": {
          "name": "FactName",
          "value": "air"
        }
      }
    }
  },
  "version": "1.0"
}
```

For our application, we only care about the following:

```json
"intent": {
  "name": "InterestingFact",
  "slots": {
    "FactName": {
      "name": "FactName",
      "value": "air"
    }
  }
}
```












asdf
