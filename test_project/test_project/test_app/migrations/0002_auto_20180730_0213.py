# Generated by Django 2.0.5 on 2018-07-30 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='post',
        ),
        migrations.AddField(
            model_name='userpost',
            name='cos',
            field=models.ForeignKey(default='123', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='portfolio',
            field=models.URLField(blank=True, default='123'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='123', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='text',
            field=models.TextField(default='123'),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='topic',
            field=models.CharField(default='123', max_length=28),
        ),
    ]