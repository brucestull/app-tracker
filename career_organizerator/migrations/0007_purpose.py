# Generated by Django 4.1.7 on 2023-11-20 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "career_organizerator",
            "0006_alter_behavioralinterviewquestion_text_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Purpose",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="The date and time this object was created.",
                        verbose_name="Created",
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="The date and time this object was last updated.",
                        verbose_name="Updated",
                    ),
                ),
                (
                    "text",
                    models.CharField(
                        help_text="The text of the purpose.",
                        max_length=500,
                        verbose_name="Text",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="The user who created the purpose.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Purposes",
            },
        ),
    ]