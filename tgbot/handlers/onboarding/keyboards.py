from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton

from tgbot.handlers.onboarding.static_text import connect_text, monobank_text


def make_keyboard_for_start_command(url) -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(connect_text, url=url),
    ]]

    return InlineKeyboardMarkup(buttons)


def make_keyboard_for_donate_command(url) -> InlineKeyboardMarkup:
    buttons = [[
        InlineKeyboardButton(monobank_text, url=url),
    ]]

    return InlineKeyboardMarkup(buttons)

