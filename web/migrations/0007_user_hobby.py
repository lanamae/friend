# Generated by Django 3.2.5 on 2022-07-06 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20220706_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='web.hobby', verbose_name='Whats your hobby?'),
        ),
    ]
