# Neurips HS: Voice to Voice with emotion (demo title) 
Neurips High School track

Current Authors: Vatsa Pandey, Samanyu Chandana, Raj Sadhankar, James _-_-_ (idk :3)

## Main Idea:
  - People in the community hae to use stuff like google translate to communicate, and that leaves emotion cut out, and doesnt account for dialects or tone
  - We target languages in the indian subcontinent + english
  - build an airpod-to-airpod demo app as its irl use presentation

## Step-by-step process:

- get mass amount of audio/text data that accounts for tone and dialect, as well as good translation (prev. data precedent set by [Krutrim](https://twitter.com/krutrim) by ola, find out more on their data sources?)
- Get a tone/emotion classifier for the audio, classifiy it at 5sec bursts, add the tags of that to the text where the words are
- Train different parts of the model
- work out inference
- build the airpod to airpod demo
- write up and submit paper

## Model arch

 - STT model, outputs text
 - emotion classifier model for audio
 - translation transformer, lang to lang
 - TTS model on final translated text to mediums
