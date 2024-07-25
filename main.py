from text2tape import text2tape
from talk2affs import talk2affs
from cull_affs import cull_affs
from edit_affs import edit_affs
from pick_voice import pick_voice
from dataset_maker import dataset_maker
import time 
import os 

## listen to the user and generate affirmations

timestamp = time.strftime("%Y%m%d-%H%M%S")

harmonize_affs, title, cwd, user_vent, output_folder = talk2affs()

title = title.replace("_", "").replace(",","").strip()

os.chdir(cwd)

# now that we have the affs, write it as user content

os.chdir(cwd)

os.chdir('output')

os.chdir(output_folder)

with open(f"user_content_{timestamp}.txt", "w") as file:
    file.write(harmonize_affs)

os.chdir(cwd)
## cull down unwanted affs

culled_affs = cull_affs(harmonize_affs, title)

print(culled_affs)

## give the user the opportunity to edit if they please

edited_affs = edit_affs(culled_affs, title)

print(edited_affs)

# write the edited affs to assistant content

os.chdir(cwd)

os.chdir('output')

os.chdir(output_folder)

with open(f"assistant_content_{timestamp}.txt", "w") as file:
    file.write(edited_affs)

os.chdir(cwd)

## store the affs into the dataset (original vs edited)

dataset_maker(harmonize_affs, edited_affs, user_vent)

# do some filepath hackery

os.chdir(cwd)

os.chdir('output')

#os.mkdir(output_folder)

os.chdir(output_folder)

## make an audio from those affirmations

selected_voice_id, voice_settings = pick_voice()

audio_path = text2tape(edited_affs, title, selected_voice_id, voice_settings)

print(audio_path)

# play it :)


# Unix-based system
if os.name == 'posix':  
    os.system(f"xdg-open {audio_path}")

 # Windows system
elif os.name == 'nt': 
    os.startfile(audio_path)


# add it to a playlist :) 

os.chdir(cwd)

playlist_file = 'meditations.m3u'

with open(playlist_file, 'a') as file:
    file.write(audio_path + '\n')