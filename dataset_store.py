from dataset_maker import dataset_maker
from process_all_text_files import process_all_text_files

def dataset_store(input_directory, user_vent):
    output_file_path = 'inputs.txt'
    # C


    # f(C)
    #input_type = input("the ai takes in: ")


    # B
    output_type = "edited affirmations"
    input_type = "original affirmations"

    original_edited_pairings = process_all_text_files(input_directory, output_file_path)

    with open(output_file_path, 'r') as file:
        transcripts = file.readlines()

    dataset_maker(input_type, output_type, original_edited_pairings, user_vent)
