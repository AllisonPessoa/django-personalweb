# Generated by Django 4.1.5 on 2023-03-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_rename_link_content_oraltalks_link_video_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="oraltalks",
            name="description",
            field=models.TextField(default="", max_length=500),
            preserve_default=False,
        ),
    ]
