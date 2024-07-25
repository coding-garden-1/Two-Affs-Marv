## cull_affs.py 

import os

def cull_affs(affs, title):

    ## Split affs into a list

    ## We do this split by both . and <br> delimiters

    # Splitting by "<br>" delimiter:

    split_affs_1 = affs.split("<br>")

    ## Splitting by . delimiter:

    split_affs = []

    for item in split_affs_1:

        split_affs.extend(item.split("."))
    
    non_empty_affs = []

    
    for item in split_affs:
        # Check if the item is not an empty string
        if item.strip() != "":
            # If it's not empty, add it to the new list
            non_empty_affs.append(item)

    split_affs = non_empty_affs

    ## Split_affs is now a list containing each aff separately

    chosen_affs = []

    ## Make user choices on which affs to keep:

    for aff in split_affs:

        print(aff)

        keep_choice = input("Keep or no? (y/n): ")

        if keep_choice == 'y':
            chosen_affs.append(aff) 

        elif keep_choice == 'n':
            pass

        else:
            print("Invalid choice.")

    chosen_affs = '.\n'.join(map(str, chosen_affs))

    ## Standardize so the string always ends in .\n

    chosen_affs = chosen_affs.replace(".\n", "\n")
    chosen_affs = chosen_affs.replace("\n", ".\n")

    # Go to output folder

    if os.path.exists("output"):
        os.chdir("output")

    # Export culled affs
        
    with open(title + "_culled.txt", "w") as file:
        file.write(chosen_affs)

    return chosen_affs
        

        
