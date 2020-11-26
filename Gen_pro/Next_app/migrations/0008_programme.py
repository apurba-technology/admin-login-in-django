# Generated by Django 2.2 on 2020-11-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Next_app', '0007_delete_pro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=150)),
                ('attach_file', models.FileField(upload_to='notice/')),
            ],
        ),
    ]