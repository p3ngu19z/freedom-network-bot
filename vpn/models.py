from django.db import models
from tgbot.models import User
from outline_vpn.outline_vpn import OutlineVPN
import urllib.parse


class OutlineServer(models.Model):
    api_url = models.CharField(max_length=256)
    cert_sha256 = models.CharField(max_length=256)


class OutlineKey(models.Model):
    key_id = models.IntegerField()
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    port = models.IntegerField()
    method = models.CharField(max_length=256)
    access_url = models.CharField(max_length=256)
    used_bytes = models.BigIntegerField()

    server = models.ForeignKey(OutlineServer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def url(self):
        return f"https://s3.amazonaws.com/outline-vpn/invite.html#/uk/invite/{urllib.parse.quote(self.access_url)}"

    @classmethod
    def create(cls, user, server):
        client = OutlineVPN(api_url=server.api_url)
        k = client.create_key()
        client.rename_key(k.key_id, str(user.user_id))
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
        client = OutlineVPN(api_url=self.server.api_url)
        client.delete_key(self.key_id)
        self.delete()
        return True