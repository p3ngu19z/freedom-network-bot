from django.contrib import admin
from django.http import HttpResponseRedirect

from vpn.models import OutlineServer, OutlineKey
from dtb.settings import DEBUG

# Register your models here.
admin.site.register(OutlineServer)


class OutlineKeyAdmin(admin.ModelAdmin):

    actions = ['remove']

    def remove(self, request, queryset):
        """ Select users via check mark in django-admin panel, then select "Broadcast" to send message"""
        key_ids = queryset.values_list('key_id', flat=True).distinct().iterator()

        for key_id in key_ids:
            key = OutlineKey.objects.get(key_id=key_id)
            key.remove()
        self.message_user(request, f"Just deleted {len(queryset)} keys")

        return HttpResponseRedirect(request.get_full_path())


admin.site.register(OutlineKey, OutlineKeyAdmin)
