# Generated by Django 4.1.5 on 2023-03-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0005_alter_banner_description_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="oraltalks",
            old_name="link_content",
            new_name="link_video",
        ),
        migrations.RemoveField(
            model_name="banner",
            name="link_content",
        ),
        migrations.RemoveField(
            model_name="oraltalks",
            name="address",
        ),
        migrations.AlterField(
            model_name="banner",
            name="event_abbr",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="oraltalks",
            name="event_abbr",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="oraltalks",
            name="presentation_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]