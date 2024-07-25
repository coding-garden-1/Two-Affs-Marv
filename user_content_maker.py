
import openai 
from openai import OpenAI


def user_content_maker(transcript, input, output):
        
    with open("openai_key.txt","r") as file:
        key = file.read().strip()

    client = OpenAI(
        api_key=key,
    )

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": f"Your job is to to generate {output} given {input}."},
            {"role": "user", "content": transcript}
         ]
    )
    generated_message = completion.choices[0].message.content
    return generated_message



