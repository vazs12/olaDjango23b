# Generated by Django 4.1.7 on 2023-04-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0002_alter_resposta_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='resposta',
            field=models.CharField(max_length=200),
        ),
    ]
