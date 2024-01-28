# Generated by Django 3.1.6 on 2023-09-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preconstruction', '0003_auto_20230927_0544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='developer',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='preconstruction',
            options={'ordering': ('last_updated',)},
        ),
        migrations.AlterField(
            model_name='preconstruction',
            name='last_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
