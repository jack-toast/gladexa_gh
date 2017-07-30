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
1. Sign into the [Amazon Developer console](https://developer.amazon.com/)
2. Go to the Alexa tab and click **Get Started** under Alexa Skills Kit
![Circled for ya](https://github.com/jack-toast/gladexa/blob/master/images/ASK%20get%20started.png?raw=true)
3. Add a new skill! ![Clickety Clack](https://github.com/jack-toast/gladexa/blob/master/images/addnewskill%20copy.PNG?raw=true)
4. Skill Information
  - Skill Type: Custom Interaction Model
  - Language: English (U.S. or U.K.) or German
  - Name: Whatever you want. This will show in the Alexa store thing.
  - Invocation Name: for this project I used *glados*
  - Global Fields: ignore these
  - Click *next*
![Skill Information](https://github.com/jack-toast/gladexa/blob/master/images/Skill%20Information.png?raw=true)
5. 
