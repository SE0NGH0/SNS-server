# Generated by Django 4.2.7 on 2023-11-02 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sns", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="mainphoto",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]