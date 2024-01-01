# Generated by Django 5.0 on 2023-12-25 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Color_M',
            fields=[
                ('Color_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Color_Name', models.CharField(max_length=24)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product_Size_M',
            fields=[
                ('Size_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Size_Name', models.CharField(max_length=8)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameField(
            model_name='product_m',
            old_name='Categories_ID',
            new_name='Category',
        ),
        migrations.CreateModel(
            name='Product_Color',
            fields=[
                ('P_Color_ID', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECom.product_m')),
                ('Color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECom.product_color_m')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Size',
            fields=[
                ('P_Size_ID', models.AutoField(primary_key=True, serialize=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('Color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECom.product_color')),
                ('Size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ECom.product_size_m')),
            ],
        ),
    ]
