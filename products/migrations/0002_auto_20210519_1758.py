# Generated by Django 3.1.3 on 2021-05-19 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemplateImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='TemplateTypeOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=200)),
                ('head_image', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('sub_title', models.CharField(max_length=200)),
                ('facebook_link', models.CharField(max_length=200)),
                ('twitter_link', models.CharField(max_length=200)),
                ('insta_link', models.CharField(max_length=200)),
                ('description_image', models.CharField(max_length=200)),
                ('description_title', models.CharField(max_length=200)),
                ('description_detail', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TemplateTypeTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='videoattachment',
            name='template',
        ),
        migrations.DeleteModel(
            name='ImageAttachment',
        ),
        migrations.DeleteModel(
            name='Template',
        ),
        migrations.DeleteModel(
            name='VideoAttachment',
        ),
    ]
