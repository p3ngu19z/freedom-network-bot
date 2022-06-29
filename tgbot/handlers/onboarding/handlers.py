from dtb.settings import DONATE_BANK_CARD, DONATE_MONOBANK_URL
from telegram import Update
from telegram.ext import CallbackContext

from tgbot.handlers.onboarding import static_text
from tgbot.models import User
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_start_command, make_keyboard_for_donate_command

from vpn.utils import get_or_create_key, replace_key
from tgbot.handlers.onboarding.utils import verification_required


@verification_required
def command_start(update: Update, context: CallbackContext) -> None:
    command_donate(update, context)

    u, created = User.get_user_and_created(update, context)
    text = static_text.key_text
    key = get_or_create_key(u)
    update.message.reply_text(text=text,
                              reply_markup=make_keyboard_for_start_command(key.url))


@verification_required
def command_key(update: Update, context: CallbackContext) -> None:
    user = User.get_user(update, context)
    key = get_or_create_key(user)
    update.message.reply_text(text=static_text.key_text,
                              reply_markup=make_keyboard_for_start_command(key.url))


@verification_required
def command_replace_key(update: Update, context: CallbackContext) -> None:
    user = User.get_user(update, context)
    key = replace_key(user)
    update.message.reply_text(text=static_text.replace_key_text,
                              reply_markup=make_keyboard_for_start_command(key.url))


@verification_required
def command_donate(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text=static_text.donate_text.format(bank_card=DONATE_BANK_CARD),
                              reply_markup=make_keyboard_for_donate_command(DONATE_MONOBANK_URL))


def contact_callback(update: Update, context: CallbackContext) -> None:
    contact = update.effective_message.contact
    if update.effective_user.id != contact.user_id:
        return
    elif "380" not in contact.phone_number[0:4]:
        update.message.reply_text(static_text.invalid_phone_number)
    else:
        user = User.get_user(update, context)
        user.is_verified = True
        user.save()
        update.message.reply_text(static_text.account_successfully_verified)
        command_start(update, context)
