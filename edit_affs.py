## edit_affs.py

import os 


def edit_affs(culled_affs, title):

    edit_choice = input("Do you want to manually edit any affirmations? (y/n): ")

    if edit_choice.lower() == 'y':

        ## Open the text file in a text editor. For my PC, I use subl.
        ## It would be better to just open the file, however directly opening text files doesn't happen on my PC.
       
        os.system(f"code {title}_culled.txt")

        print("Go ahead and edit :)")

        print("Make sure to save.")

        ## Wait for the user to be done.

        done_status = input("Press enter when you're done: ")

        ## write the users edited text file as a variable

        if os.path.exists("output"):
            os.chdir("output")

        with open(f"{title}_culled.txt", "r") as file:
            edited_affs = file.read()

        return edited_affs
            
    
    ## If the user doesn't want to edit, move on to other features..

    else:

        return culled_affs