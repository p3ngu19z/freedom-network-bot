from functools import wraps
from typing import Callable

from tgbot.models import User
from tgbot.handlers.onboarding import static_text
from tgbot.handlers.onboarding.keyboards import make_keyboard_for_request_contact


def verification_required(func: Callable):
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        user = User.get_user(update, context)
        if not user.is_verified:
            context.bot.send_message(chat_id=update.message.chat_id, text=static_text.phone_number_request,
                                     reply_markup=make_keyboard_for_request_contact())
            return
        else:
            return func(update, context, *args, **kwargs)

    return command_func
