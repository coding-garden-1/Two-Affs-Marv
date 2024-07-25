import json

def dataset_maker(harmonize_affs, edited_affs, user_vent):

    # initialize the list of "conversations" (only one on this version)

    finetune_dataset_lines = []

    # put together the "conversations"

    harmonize_affs_str = harmonize_affs

    user_content = f"{harmonize_affs_str}. These affirmations are supposed to match this vent: {user_vent}"

    assistant_content = edited_affs.replace("\n","")

    conversation = {
        "messages": [
            {"role": "system", "content": "You edit affirmations to best match the user vent and the best written style."},
            {"role": "user", "content": user_content},
            {"role": "assistant", "content": assistant_content}
        ]
    }

    finetune_dataset_lines.append(conversation)

    with open("original_edited_pairings.jsonl", "a", encoding="utf-8") as file:
        for conv in finetune_dataset_lines:
            json_line = json.dumps(conv, ensure_ascii=False)
            file.write(json_line + "\n")
