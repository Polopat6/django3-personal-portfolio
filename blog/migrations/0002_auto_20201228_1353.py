# Generated by Django 3.1.4 on 2020-12-28 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='url',
        ),
        migrations.AddField(
            model_name='blogs',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
