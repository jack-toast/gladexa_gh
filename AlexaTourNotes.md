# Alexa Skills Tour Notes

## Questions

- How do I make it so that only I can access the MP3's from my S3 buckets.

### Automated Insights

- Look into their [WordSmith](https://automatedinsights.com/wordsmith) platform for automatically making more natural responses.

## Justin Jeffress [@SleepyDeveloper](https://twitter.com/SleepyDeveloper)

- hello
- hello
- hello

### Two parts to any alexa skill

1. Voice User Interface (developer.amazon.com)
2. Programming Logic (aws.amazon.com)

### Flow

1. Utter something
2. Map utterance to intents
3. Package Intent into JSON
4. Send JSON to service (Lambda or other HTTPS)

### Can change up the way things are said. These are the same:

- Alexa, ask for an activity from Denver guide

- Alexa, ask Denver Guide for an activity

How can you get around using the Invocation name? --> "Alexa, turn off the lights" vs "Alexa, tell Phillips Hue to turn off the lights"

### Slots Make sure code reads like prose

## Akersh Srivastava [@Akersh_s](https://twitter.com/Akersh_S)

- Design for the screen last
- Make sure everything works on the Echo dot and then scale up from there

### Don't organize things linearly, organize them using the framework of conversation.

### Multi-turn dialogs

- Slot elicitation
- Slot confirmation
- Intent confirmation

Start by designing the "Happy path", then work to offer other routes around the "happy path" that still take the user to the endpoint.

asdf
