# Generated by Django 4.1.5 on 2023-01-15 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Publication",
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
                ("title", models.CharField(max_length=500)),
                ("author", models.CharField(max_length=500)),
                ("year", models.PositiveSmallIntegerField()),
                ("image", models.ImageField(upload_to="")),
                ("month", models.PositiveSmallIntegerField(blank=True)),
                ("note", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "publication_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.publication",
                    ),
                ),
                ("journal_name", models.CharField(max_length=100)),
                ("journal_abbr", models.CharField(blank=True, max_length=50)),
                ("volume", models.PositiveSmallIntegerField(blank=True)),
                ("number", models.PositiveSmallIntegerField(blank=True)),
                ("issue", models.PositiveSmallIntegerField(blank=True)),
                ("starting_page", models.PositiveSmallIntegerField(blank=True)),
                ("ending_page", models.PositiveSmallIntegerField(blank=True)),
                ("file", models.FileField(blank=True, upload_to="uploads/")),
                ("abstract", models.TextField(blank=True)),
            ],
            bases=("base.publication",),
        ),
        migrations.CreateModel(
            name="Instrument",
            fields=[
                (
                    "publication_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.publication",
                    ),
                ),
                ("link_github", models.URLField(blank=True)),
                ("link_project", models.URLField(blank=True)),
                ("abstract", models.TextField(blank=True)),
            ],
            bases=("base.publication",),
        ),
        migrations.CreateModel(
            name="Presentation",
            fields=[
                (
                    "publication_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.publication",
                    ),
                ),
                ("event_name", models.CharField(max_length=100)),
                ("event_abbr", models.CharField(max_length=50)),
                ("presentation_date", models.DateField(blank=True)),
                ("address", models.CharField(max_length=500)),
                ("abstract", models.TextField(blank=True, max_length=500)),
                ("link_abstract", models.URLField(blank=True)),
                ("link_content", models.URLField(blank=True)),
            ],
            bases=("base.publication",),
        ),
        migrations.CreateModel(
            name="Software",
            fields=[
                (
                    "publication_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="base.publication",
                    ),
                ),
                ("link_github", models.URLField(blank=True)),
                ("link_project", models.URLField(blank=True)),
                ("abstract", models.TextField(blank=True)),
            ],
            bases=("base.publication",),
        ),
    ]
