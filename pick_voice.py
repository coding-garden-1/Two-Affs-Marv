def pick_voice():
    voices = {
        "Soft": "2107gNQFNSTeANblDCbg",
        "Master Chief": "sgvFCzQsTVvUerl8SB7F",
        "Dylan": "JW1R9arGrJs4DFjiEpLy",
        "Donna Paulsen (quiet)": {
            "voice_id": "u0JBfOkscWTptrWTNYSW",
            "settings": {
                "stability": 0.93,
                "similarity_boost": 0.82,
                "style": 0.88
            }
        },
        "Donna Paulsen": {
            "voice_id": "8jrgx0Xrm4xm6CbU6UDU",
            "settings": {
                "stability": 0.81,
                "similarity_boost": 0.75,
                "style": 0.72
            }
        },
        "Mike Ross": {
            "voice_id": "ylwQn27F4vbjPn5XpnFW",
            "settings": {
                "stability": 0.82,
                "similarity_boost": 0.65,
                "style": 0.85
            }
        },
        "Harvey Specter": {
            "voice_id": "UrmeurwgB1VtP6a5pCbg",
            "settings": {
                "stability": 0.6,
                "similarity_boost": 0.82
            }
        },
        "Solid Snake": {
            "voice_id": "ZrDQCdsmIwCz14Zgza22",
            "settings": {
                "stability": 0.75,
                "similarity_boost": 0.75
            }
        },
        "Relax Guy": {
            "voice_id": "E6OBVUX3uqPYtkV4B4Et",
            "settings": {
                "stability": 0.50,
                "similarity_boost": 0.87,
                "style": 0.48,
                "use_speaker_boost": False
            }
        }
    }

    for index, voice in enumerate(voices, start=1):
        print(f"{index}: {voice}")

    chosenvoiceindex = int(input(f"Which voice (1-{len(voices)}) "))
    chosenvoice = list(voices.values())[chosenvoiceindex - 1]

    if not isinstance(chosenvoice, dict):
        selected_voice_id = chosenvoice
        settings = {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    else:
        selected_voice_id = chosenvoice["voice_id"]
        settings = chosenvoice.get("settings", {})

    return selected_voice_id, settings
