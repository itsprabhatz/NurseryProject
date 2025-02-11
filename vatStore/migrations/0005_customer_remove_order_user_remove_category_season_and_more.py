# Generated by Django 5.0.3 on 2024-05-08 06:18

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vatStore', '0004_alter_category_options_product_is_sale_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/product/')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='Season',
        ),
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='category',
            name='type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vatStore.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='uploads/product/'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vatStore.customer'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name=django.contrib.auth.models.User)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('address1', models.CharField(blank=True, max_length=200)),
                ('address2', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=200)),
                ('state', models.CharField(blank=True, max_length=200)),
                ('zipcode', models.CharField(blank=True, max_length=200)),
                ('country', models.CharField(blank=True, max_length=200)),
                ('old_cart', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='ProductDetail',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
