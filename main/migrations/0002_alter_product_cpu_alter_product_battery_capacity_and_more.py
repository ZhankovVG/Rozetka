# Generated by Django 4.2.1 on 2023-05-16 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CPU',
            field=models.CharField(blank=True, max_length=122, null=True, verbose_name='Процессор'),
        ),
        migrations.AlterField(
            model_name='product',
            name='battery_capacity',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ёмкость батареи'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand_1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.brandelectronics', verbose_name='Марка электроники'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.brandhouseholdappliances', verbose_name='Марка бытовой техники'),
        ),
        migrations.AlterField(
            model_name='product',
            name='display_size',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Размер дисплея'),
        ),
        migrations.AlterField(
            model_name='product',
            name='operating_system',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Операционная система'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Оперативная память'),
        ),
        migrations.AlterField(
            model_name='product',
            name='series',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Серия'),
        ),
    ]