# Generated by Django 3.2.16 on 2022-11-21 19:18

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20221114_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='test',
            field=ckeditor.fields.RichTextField(default='Other'),
        ),
    ]