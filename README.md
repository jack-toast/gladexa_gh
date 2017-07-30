# Gladexa = GLaDOS + Alexa

### Quick Links:
- [Amazon Lambda](http://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
  - [Boto 3 Documentation](https://boto3.readthedocs.io/en/latest/)
- [Amazon Alexa Skills Kit](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/getting-started-guide)
  - [Understanding Custom Skills](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/overviews/understanding-custom-skills)
- [Amazon Simple Storage Service](https://aws.amazon.com/documentation/s3/)
- [GLaDOS Voice Lines](https://theportalwiki.com/wiki/GLaDOS_voice_lines)
- [Decypher Media (AlwaysBCoding) Alexa Lambda Tutorial](https://www.youtube.com/watch?v=zt9WdE5kR6g&t=697s)

### How it all works
![Main Diagram](https://github.com/jack-toast/gladexa/blob/master/images/overview%20diagram.png?raw=true)

#### The three main components:
- The Alexa skill / Echo itself
- The Lambda function that handles all of our processing and routing
- The S3 backend that holds all of our data

### Setting up the Alexa Skill
#### 1. [Amazon Developer console](https://developer.amazon.com/) >> Sign In
#### 2. Alexa Tab >> Alexa Skills Kit >> **Get Started**
![Circled for ya](https://github.com/jack-toast/gladexa/blob/master/images/ASK%20get%20started.png?raw=true)
#### 3. Add a new skill ![Clickety Clack](https://github.com/jack-toast/gladexa/blob/master/images/addnewskill%20copy.PNG?raw=true)
#### 4. Skill Information
  - Skill Type: Custom Interaction Model
  - Language: English (U.S. or U.K.) or German
  - Name: Whatever you want. This will show in the Alexa store thing if you publish the skill. I'm not publishing, so I named it for my own organization.
  - Invocation Name: I used "glados". Make sure it's something that the Alexa voice engine can understand phonetically
  - Global Fields: Ignore
  - Click *next*
![Skill Information](https://github.com/jack-toast/gladexa/blob/master/images/Skill%20Information.png?raw=true)

#### 5. Interaction Model

Apparently [Draw.io](https://www.draw.io/) has pokemon icons, so I'll be using those to explain how **Intents** and **Slots** work.

So lets say we have three different intents in our skill

![Pokemans](https://github.com/jack-toast/gladexa/blob/master/images/pokemon2.png?raw=true)

Intent | Slot Type | Slot Value Options
--- | --- | ---
 OG Red | B-Tier Pokemon | Rattata, Pidgey, Magikarp
Ultra | A-Tier Pokemon | Dragonair, Nidoking, Rapidash
Master | S-Tier Pokemon | Mewtwo, Zapdos, Mew

So if we invoked our Pokemans Skill, we would pass an intent of either OG Red, Ultra, or Master. Within each intent we pass a value into a slot.

An example invocation of our Alexa skill could be as follows.















asdf
