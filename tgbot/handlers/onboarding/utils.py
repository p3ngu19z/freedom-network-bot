from functools import wraps
from typing import Callable

from tgbot.handlers.onboarding import static_text
from telegram import ParseMode


def check_language(func: Callable):
    @wraps(func)
    def command_func(update, context, *args, **kwargs):
        if update.effective_user.language_code == 'ru':
            update.message.reply_text(text=static_text.check_language_text, parse_mode=ParseMode.HTML)
            return
        else:
            return func(update, context, *args, **kwargs)

    return command_func
