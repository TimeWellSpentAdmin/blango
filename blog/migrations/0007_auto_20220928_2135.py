# Generated by Django 3.2.5 on 2022-09-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20220928_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=1987),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
