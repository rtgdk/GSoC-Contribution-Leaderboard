# Generated by Django 2.1.5 on 2019-03-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20190311_1906'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='relation',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='relation',
            name='repo',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='repository',
            name='users',
        ),
        migrations.RenameField(
            model_name='lastupdate',
            old_name='updated',
            new_name='allList',
        ),
        migrations.AddField(
            model_name='lastupdate',
            name='gList',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='user',
            name='totalMergedPRs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='totalOpenPRs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.TextField(unique=True),
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
        migrations.DeleteModel(
            name='Repository',
        ),
    ]