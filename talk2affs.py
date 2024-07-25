# main.py 

from openai import OpenAI
import sounddevice as sd 
import soundfile as sf 
import os
import re 
import shutil
import os
from datetime import datetime

with open("openai_key.txt","r") as file:
    key = file.read().strip()

client = OpenAI(
    api_key=key,
)



def affirm_make(transcript):

    completion = client.chat.completions.create(
      model="ft:gpt-3.5-turbo-0125:personal:dylan-affs:9Fln01C5",
      messages=[
        {"role": "system", "content": "This is an affirmation bot that generates positive affirmations formatted/worded in a specific way, and these affirmations come from the user's direct self-concept needs. He should format this in a way that it can be read by a text to speech bot with no hiccups (so there should be no <br>s and each sentence should end with a period.) Please write You Are affirmations."},
        {"role": "user", "content": transcript}
      ]
    )

    return completion.choices[0].message.content

def whisper_transcription(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file,  # Pass the file object directly
            response_format="text"
        )
        return response


def audio_recorder(file_path, duration=90, sample_rate=44100):
    print(f"Recording audio for {duration} seconds. Speak into the microphone...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2, dtype='float32')
    sd.wait()  # Wait for recording to complete
    sf.write(file_path, audio_data, sample_rate)
    print(f"Audio recording saved to {file_path}")

def title_make(affs):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You take in a list of affirmations and give them a good title. Example titles are Hot Girls Want You, You Are Her Dream Girl, Chased By Suitors, Top Tier Treatment, People Commit 2 U, You KNOW You're Hot, etc. Max 3 words (22 char) per title."},
            {"role": "user", "content": affs}
        ]
    )
    generated_message = completion.choices[0].message.content
    return generated_message

def category_decide(affs, categories):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": f"You take in a list of affirmations and categorize the whole list into one of the following categories: {categories}. You are not allowed to make up your own categories. Your response will be parsed as raw code, so you must only return one category, in lower case. You cannot return new categories or say anything other than the category you believe the list belongs in. Please try to be as accurate as possible with your choice."},
            {"role": "user", "content": affs}
        ]
    )
    generated_message = completion.choices[0].message.content
    return generated_message

def selector(affs, transcribed):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "You take in a list of ai generated affirmations alongside their intended role and return only the affirmations in the list that are actually relevant to the intended purpose. You cannot change any wording or make your own, you are simply a culler. Make sure there are periods at the end of each affirmation."},
            {"role": "user", "content": "Ai generated affirmations list: " + affs + " Intended purpose for which affirmations were generated: " + transcribed}
        ]
    )
    generated_message = completion.choices[0].message.content
    return generated_message

    
def talk2affs():

    cwd = os.getcwd()
    os.chdir("output")
    # Make folder

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_folder_timestamped =f"output_{timestamp}"



    os.mkdir(output_folder_timestamped)


    shutil.copy("bgm.mp3", output_folder_timestamped)
    os.chdir(output_folder_timestamped)

    ## Transcribe user speech

    audio_recorder("recorded.wav")

    transcribed = whisper_transcription("recorded.wav")

    user_vent = transcribed

    print(transcribed)


    ## Generate affirmations 

    affs1 = affirm_make(transcribed)
    affs2 = affirm_make(transcribed)
    affs3 = affirm_make(transcribed)
    affs4 = affirm_make(transcribed)
    affs5 = affirm_make(transcribed)

    affs = affs1+affs2+affs3+affs4+affs5
    #affs=affs1+affs2+affs3
    #affs=affs1 
    ## Print affirmations on screen

    print(affs)

    ## Select the 7 best according to default ChatGPT

    #selected_affs = selector(affs1+affs2+affs3, transcribed)

    ## Make a good title with ChatGPT

    title = title_make(affs1)

    ## Remove spaces

    title = title.replace(" ", "_")
    ## Print title on screen

    print(title)

    ## Export the full 50 and the GPT-selected 7

    #with open(title + ".txt", "w") as file:
        #file.write(selected_affs)

    #with open(title + "_unabridged.txt", "w") as file:
        #file.write(affs1+affs2+affs3+affs4+affs5)

    with open(title + "_unabridged.txt", "w") as file:
        file.write(affs)

    ## Return the affirmations

    return affs, title, cwd, user_vent, output_folder_timestamped

