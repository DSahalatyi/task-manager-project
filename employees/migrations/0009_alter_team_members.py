# Generated by Django 5.1.1 on 2024-09-23 08:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0008_alter_team_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="members",
            field=models.ManyToManyField(
                blank=True, related_name="teams", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
