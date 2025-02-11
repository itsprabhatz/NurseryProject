# Generated by Django 5.0.3 on 2024-05-07 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vatStore', '0003_rename_color_category_season_category_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_sale',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
