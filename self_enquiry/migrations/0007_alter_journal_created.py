# Generated by Django 4.1.9 on 2023-08-24 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_enquiry', '0006_alter_growthopportunity_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time the journal was created.'),
        ),
    ]