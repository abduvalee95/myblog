# Generated by Django 4.0 on 2022-04-15 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категории')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='categry',
            field=models.CharField(default='Без котегория', max_length=255),
        ),
    ]
