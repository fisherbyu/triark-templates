# Generated by Django 4.1.2 on 2022-12-29 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_crunch', '0006_alter_contenttype_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codeblock',
            name='title',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='contenttype',
            name='title',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
