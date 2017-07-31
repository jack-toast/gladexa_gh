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
  - Name: Whatever you want. This will show in the Alexa store thing if you publish the skill. I'm not publishing, so I named it something that's easy to recognize.
  - Invocation Name: I used "glados". Make sure it's something that the Alexa voice engine can understand phonetically.
  - Global Fields: Ignore
  - Click *next*
![Skill Information](https://github.com/jack-toast/gladexa/blob/master/images/Skill%20Information.png?raw=true)

### 5. Interaction Model

![InteractionModelScreenGrab](https://github.com/jack-toast/gladexa/blob/master/images/InteractionModel.PNG?raw=true)

#### What it do?

The interaction model describes how our speech is parsed into the command message that is sent to the Lambda function.

The **Intents**, **Slot values**, and **Utterances** control the message that is sent.

Let's take an example command and break it down.

*"Alexa, ask glados to tell me an interesting fact about air"*

Alexa, | ask | glados | to | tell me an interesting fact about | air
---|---|---|---|---|---
Wake word | Linker | Invocation Name | Linker | Specifies the intent | Slot value

By saying this phrase the following JSON message is sent to our Lambda function:

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

#### We control all of this with the Intents, Slots, and Utterances

For this example there are four different intents:
```
AllStar
OriginStory
JohnsSong
InterestingFact
```
Basically we have a JSON object filled with all of our intent names, each labeled with the format "intent": "name"

For "InterestingFact" have one slot named "FactName" that is compared to the custom slot type "FACT_NAME"

AMAZON.HelpIntent, AMAZON.CancelIntent, and AMAZON.StopIntent are included to add basic functionality such as letting you cancel out of a skill midway. This helped me cancel out of an infinite loop of Alexa reading Smash Mouth lyrics.

#### Intents Schema

```json
{
  "intents": [
    {
      "intent": "AllStar"
    },
    {
      "intent": "InterestingFact",
      "slots": [
        {
          "name": "FactName",
          "type": "FACT_NAME"
        }
      ]
    },
    {
      "intent": "OriginStory"
    },
    {
      "intent": "PlaySoundFile"
    },
    {
      "intent": "JohnsSong"
    },
    {
      "intent": "AMAZON.HelpIntent"
    },
    {
      "intent": "AMAZON.CancelIntent"
    },
    {
      "intent": "AMAZON.StopIntent"
    }
  ]
}
```

#### Custom Slot Types

We only need one of these, but if your other intents that require slots, you would add them here.

##### Type
```
FACT_NAME
```

##### Values:
```
donating
air
people
```

#### Example Utterances

This is where you enter example trigger phrases. For this project, I've entered the following phrases:
```
AllStar your favorite poem
OriginStory your origin story
JohnsSong play johns favorite song
InterestingFact tell me an interesting fact about {FactName}
```


### 6. Interaction Model

![ConfigurationScreen](https://github.com/jack-toast/gladexa/blob/master/images/Configuration.PNG?raw=true)

Well that was quick...

### 7. Lambda Configuration

Amazon Lambda is a super rad cloud compute platform that will scale to any amount of demand you throw at it. For our small use case, it's just a simple to use platform that will run our python script.








asdf
