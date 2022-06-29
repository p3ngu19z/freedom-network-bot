from django.db import models
from tgbot.models import User
from outline_vpn.outline_vpn import OutlineVPN
import urllib.parse
from vpn.constatns import *


class OutlineServer(models.Model):
    api_url = models.CharField(max_length=256)
    cert_sha256 = models.CharField(max_length=256)

    is_deleted = models.BooleanField(default=False)
    transferred_bytes = models.BigIntegerField(default=0)
    limit_bytes = models.BigIntegerField(default=DEFAULT_SERVER_DATA_LIMIT)


class OutlineKey(models.Model):
    key_id = models.IntegerField()
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    port = models.IntegerField()
    method = models.CharField(max_length=256)
    access_url = models.CharField(max_length=256)
    used_bytes = models.BigIntegerField()

    is_deleted = models.BooleanField(default=False)

    server = models.ForeignKey(OutlineServer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def url(self):
        return f"{OUTLINE_INVITE_URL}{urllib.parse.quote(self.access_url + SERVER_NAME)}"

    @classmethod
    def create(cls, user, server):
        client = OutlineVPN(api_url=server.api_url, cert_sha256=server.cert_sha256)
        k = client.create_key()
        client.rename_key(k.key_id, str(user.user_id))
        client.add_data_limit(k.key_id, DATA_LIMIT)
        o_key = OutlineKey(
            key_id=k.key_id,
            name=str(user.user_id),
            password=k.password,
            port=k.port,
            method=k.method,
            access_url=k.access_url,
            used_bytes=k.used_bytes,
            user=user,
            server=server
        )
        o_key.save()
        return o_key

    def remove(self):
        client = OutlineVPN(api_url=self.server.api_url, cert_sha256=self.server.cert_sha256)
        client.delete_key(self.key_id)
        self.is_deleted = True
        self.save()
        return True
