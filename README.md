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

 - STT model, outputs text (whisper-small is good, finetune it on our langauges, need around 40 hours per language for a finetune, then convert to and inference with whisper.cpp)
 - emotion classifier model for audio
 - translation transformer, lang to lang
 - TTS model on final translated text to mediums

## Data Sourcing

 - TTS/STT
   - YT vids
 - Emotion Classifier
   - WIP
 - Lang-to-lang transform
   - Base language text
     - [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)
     - Need more scraping, the culturaX values seem odd/out of proportion, though they are good enough for starters (*put this under future tasks/bias recognition in interp*)
   - Instruct
     - https://huggingface.co/datasets/sam2ai/hindi_alpaca_dolly_67k
   - Tone/dialect
     - Try harvesting data from Krutrim?
     - https://huggingface.co/datasets/bigscience/xP3all
     - https://huggingface.co/datasets/CohereForAI/xP3x
     - https://huggingface.co/datasets/CohereForAI/aya_dataset
     - https://huggingface.co/datasets/allenai/MADLAD-400      
