# Generated by Django 3.2 on 2022-07-03 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20220627_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='color',
            field=models.CharField(choices=[('Gray', 'Серый'), ('Black', 'Чёрный'), ('White', 'Белый'), ('Ginger', 'Рыжий'), ('Mixed', 'Смешанный')], max_length=16),
        ),
    ]
