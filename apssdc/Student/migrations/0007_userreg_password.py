# Generated by Django 3.0.6 on 2020-06-09 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0006_userreg'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreg',
            name='Password',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
