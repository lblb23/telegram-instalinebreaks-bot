def handle_text(text, messages):
    corrected_text = text.replace(" \n\n", "\n⠀\n").replace("\n\n", "\n⠀\n")
    result = True
    traceback = "Success"

    text_len = len(corrected_text)
    num_hashtags = corrected_text.count("#")

    metadata_text = messages['metadata'].format(text_len, num_hashtags)

    return corrected_text, metadata_text, result, traceback
