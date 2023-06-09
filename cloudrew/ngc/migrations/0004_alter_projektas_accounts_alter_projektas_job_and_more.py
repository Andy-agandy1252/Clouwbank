# Generated by Django 4.2 on 2023-04-14 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ngc', '0003_alter_account_ammount_of_money_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projektas',
            name='accounts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ngc.account'),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ngc.job'),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='klient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ngc.klient'),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='workers',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ngc.worker'),
        ),
    ]
