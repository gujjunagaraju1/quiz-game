# Generated by Django 4.2.5 on 2023-09-27 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_certifiedalready'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certifiedalready',
            name='category',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, to='core.quizcategory'),
        ),
    ]
