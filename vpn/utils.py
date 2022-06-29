from vpn.models import OutlineServer, OutlineKey
from tgbot.models import User
from random import choice


def get_or_create_key(user: User, exclude_id=None) -> OutlineKey:
    key = OutlineKey.objects.filter(user=user).filter(is_deleted=False).first()
    if not key:
        server = get_best_server(exclude_id=exclude_id)
        key = OutlineKey.create(user, server)
    return key


def replace_key(user: User) -> OutlineKey:
    old_key = OutlineKey.objects.filter(user=user).filter(is_deleted=False).first()
    if old_key:
        old_key_server_id = old_key.server.id
        old_key.remove()
        return get_or_create_key(user, exclude_id=old_key_server_id)
    else:
        return get_or_create_key(user)


def get_best_server(exclude_id=None) -> OutlineServer:
    try:
        return choice(OutlineServer.objects.exclude(id=exclude_id).filter(is_deleted=False).all())
    except IndexError:
        return OutlineServer.objects.first()
