import os
import re

def process_all_text_files(input_directory, output_file_path):
    try:
        original_edited_pairs = {}
        edited_affs = {}
        
        for root, dirs, files in os.walk(input_directory):
            for filename in files:
                if filename.startswith('user_content_') and filename.endswith('.txt'):
                    timestamp = filename.split('_')[2]
                    user_content = read_file(os.path.join(root, filename))
                    
                    assistant_filename = f"assistant_content_{timestamp}"
                    assistant_path = os.path.join(root, assistant_filename)
                    if os.path.exists(assistant_path):
                        assistant_content = read_file(assistant_path)
                        
                        # Collapse multi-line affiliations into single lines
                        user_content = collapse_text(user_content)
                        assistant_content = collapse_text(assistant_content)
                        
                        original_edited_pairs[user_content] = assistant_content
        
        with open(output_file_path, 'w') as outfile:
            outfile.write(str(original_edited_pairs))
        
        print(f"Processed files saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return original_edited_pairs

def read_file(file_path):
    with open(file_path, 'r') as infile:
        lines = infile.readlines()
        single_line_text = "\\n".join(line.strip() for line in lines)
        return single_line_text

def collapse_text(text):
    # Remove line breaks and replace with spaces
    text = text.replace('\n', ' ')
    # Add a period after each sentence if it's not already there
    text = re.sub(r'(?<=[.!?])(?=[^\s])', '. ', text)
    return text


