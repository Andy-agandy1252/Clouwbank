# Generated by Django 4.2 on 2023-04-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngc', '0002_alter_account_options_alter_job_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ammount_of_money',
            field=models.FloatField(verbose_name='Suma'),
        ),
        migrations.AlterField(
            model_name='account',
            name='date_of_issue',
            field=models.DateField(verbose_name='Išrašymo data'),
        ),
        migrations.AlterField(
            model_name='projektas',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
