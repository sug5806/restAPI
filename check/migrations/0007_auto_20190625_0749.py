# Generated by Django 2.2.2 on 2019-06-25 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0006_auto_20190625_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='cls_t',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='check.cls'),
        ),
    ]
