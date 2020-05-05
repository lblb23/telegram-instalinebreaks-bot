def handle_text(text):
    corrected_text = text.replace(" \n\n", "\n⠀\n").replace("\n\n", "\n⠀\n")
    result = True
    traceback = "Success"

    return corrected_text, result, traceback
