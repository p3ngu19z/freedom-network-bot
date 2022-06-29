from telegram import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

from tgbot.handlers.onboarding.static_text import connect_text, monobank_text, send_phone_button_text


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


def make_keyboard_for_request_contact() -> ReplyKeyboardMarkup:
    buttons = [[
        KeyboardButton(send_phone_button_text, request_contact=True),
    ]]

    return ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

