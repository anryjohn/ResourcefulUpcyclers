# Generated by Django 2.0.1 on 2018-06-04 04:04

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180426_1925'),
        ('item', '0002_request'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Business')),
                ('offers', models.ManyToManyField(blank=True, default=None, to='item.Inventory')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='item.StoreLocation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
