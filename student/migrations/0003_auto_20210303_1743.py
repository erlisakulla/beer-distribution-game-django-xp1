<<<<<<< HEAD
# Generated by Django 3.1.7 on 2021-03-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210303_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='assigned_games',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='time_registered',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
=======
# Generated by Django 3.1.7 on 2021-03-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20210303_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='assigned_games',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='time_registered',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
>>>>>>> ce29bf3716dd0ce95bd0600ec0cc41dbd2acf737
