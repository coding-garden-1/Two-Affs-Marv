from pydub import AudioSegment
import os
import requests


def eleven_labs_tts(text_content, filename, selected_voice_id, voice_settings):
    CHUNK_SIZE = 1024

    if not selected_voice_id:
        print("Error: Voice not found")
        return

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{selected_voice_id}"

    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": "sk_ab43dadadbff224c583789ae99c46554e8eab55495d1a0b7"
    }

    data = {
        "text": text_content,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": voice_settings.get("stability", 0.5),
            "similarity_boost": voice_settings.get("similarity_boost", 0.5)
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)
                    
        print(f'Audio file "{filename}" generated successfully')
        return filename
    else:
        print(f'Error: {response.status_code}, {response.text}')


def text2tape(sentences, title, selected_voice_id, voice_settings):
    #bgm_decrease = input("decrease BGM volume by what number (0-10): ")

    bgm_decrease = 6

    # Load background music
    bgm = AudioSegment.from_mp3("bgm.mp3") - bgm_decrease
    sentences = sentences.split(".")
    # List to hold file names of generated speech segments
    speech_filenames = []

    # Convert each sentence to speech, save it to a file, and adjust volume
    for i, sentence in enumerate(sentences):
        print(sentence)
        speech_filename = f"speech_{i}.mp3"

        # Convert text to speech and save it to a file
        eleven_labs_tts(sentence, speech_filename, selected_voice_id, voice_settings)

        # Adjust volume of speech segment
        speech_segment = AudioSegment.from_mp3(speech_filename) + 8

        # Save the adjusted speech segment to a file
        adjusted_speech_filename = f"adjusted_speech_{i}.mp3"

        speech_segment.export(adjusted_speech_filename, format="mp3")

        # Add the filename to the list
        speech_filenames.append(adjusted_speech_filename)

    # List to hold each speech segment with 15 seconds of silence
    final_segments_with_silence = []

    # Add each speech segment to the final audio with x seconds of silence between them
    for speech_filename in speech_filenames:
        # Load the speech segment
        speech_segment = AudioSegment.from_mp3(speech_filename)

        # Add the speech segment to the list of final segments
        final_segments_with_silence.append(speech_segment)

        # Add 15 seconds of silence after each speech segment
        final_segments_with_silence.append(AudioSegment.silent(duration=9000))

    # Concatenate all segments
    final_audio = sum(final_segments_with_silence)

    # Overlay with background music
    final_audio_with_bgm = final_audio.overlay(bgm)

    # Save final audio

    audiopath = title + ".mp3"

    final_audio_with_bgm.export(audiopath, format="mp3")

    cwd = os.getcwd()

    audiopath = cwd + '/' + audiopath

    # Clean up temporary files

    for filename in os.listdir('.'):
        if "speech" in filename or "bgm" in filename:
            os.remove(filename)
    return audiopath
