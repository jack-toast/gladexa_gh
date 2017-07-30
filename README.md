# Gladexa = GLaDOS + Alexa

## A seemingly straight-forward approach to combining Alexa and GLaDOS

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

#### From the image above, we see the three main components:
1. The Alexa skill / Echo itself
2. The Lambda function that handles all of our processing and routing
3. The S3 backend that holds all of our data

### Setting up the Alexa Skill
1. Go to [developer.amazon.com](https://developer.amazon.com/) and sign in or create an account
2. Go to the Alexa tab and click Get Started under Alexa Skills Kit
