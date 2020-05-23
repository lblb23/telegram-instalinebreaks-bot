from telegram.ext import CallbackContext


def handle_text(text, messages):
    corrected_text = text.replace(" \n\n", "\n⠀\n").replace("\n\n", "\n⠀\n")
    result = True
    traceback = "Success"

    text_len = len(corrected_text)
    num_hashtags = corrected_text.count("#")

    metadata_text = messages["metadata"].format(text_len, num_hashtags)

    return corrected_text, metadata_text, result, traceback


def send_limit_message(context: CallbackContext, chat_id: int, messages: dict) -> tuple:
    """
    Send error message about unsupported platform
    :param context: telegram context
    :param chat_id: chat id with user
    :param messages: dict with templates of messages
    :param platform: platform name
    :return: fail status and reason
    """
    context.bot.send_message(chat_id=chat_id, text=messages[f"limit_message"])
    result = False
    traceback = "Limit is exceeded"

    return result, traceback
