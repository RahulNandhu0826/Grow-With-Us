# Generated by Django 4.1.1 on 2023-05-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_diet_diet_chart_diets'),
    ]

    operations = [
        migrations.AddField(
            model_name='users_reg',
            name='payment_done',
            field=models.CharField(default='no', max_length=30, null=True),
        ),
    ]
