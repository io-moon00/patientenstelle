# Generated by Django 5.0.6 on 2024-07-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page',
            field=models.CharField(choices=[('home', 'Home'), ('news', 'News'), ('offer', 'Angebot'), ('about', 'About'), ('membership', 'Mitgliedschaft'), ('contact', 'Contact'), ('links', 'Links')], default='home', max_length=10),
        ),
    ]
