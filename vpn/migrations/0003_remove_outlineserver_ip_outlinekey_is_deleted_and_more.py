# Generated by Django 4.0.5 on 2022-06-29 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn', '0002_outlinekey_port'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outlineserver',
            name='ip',
        ),
        migrations.AddField(
            model_name='outlinekey',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outlineserver',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='outlineserver',
            name='limit_bytes',
            field=models.BigIntegerField(default=1000000000000),
        ),
        migrations.AddField(
            model_name='outlineserver',
            name='transferred_bytes',
            field=models.BigIntegerField(default=0),
        ),
    ]