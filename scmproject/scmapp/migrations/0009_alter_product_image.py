# Generated by Django 4.2 on 2023-05-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scmapp', '0008_product_image_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
