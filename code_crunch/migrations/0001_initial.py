# Generated by Django 4.1.2 on 2022-12-28 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeBlock',
            fields=[
                ('title', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'code_block',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empID', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='EmpSignHTML',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('empID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='code_crunch.employee')),
            ],
            options={
                'db_table': 'emp_sign',
            },
        ),
        migrations.CreateModel(
            name='BlockContent',
            fields=[
                ('title', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('content', models.TextField()),
                ('empID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='code_crunch.employee')),
            ],
            options={
                'db_table': 'block_content',
            },
        ),
    ]
