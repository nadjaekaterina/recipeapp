# Generated by Django 3.2.16 on 2022-11-22 18:37

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_remove_recipe_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='testpicture',
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='Add your picture here'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.CharField(default='Add your category here', max_length=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=ckeditor.fields.RichTextField(default='Add your description here'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=ckeditor.fields.RichTextField(default='Add your ingredients here'),
        ),
    ]