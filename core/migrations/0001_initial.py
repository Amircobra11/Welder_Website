# Generated by Django 5.2 on 2025-04-03 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100, verbose_name='نام سایت')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='لوگو')),
                ('phone', models.CharField(max_length=20, verbose_name='شماره تماس')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('about_text', models.TextField(verbose_name='درباره ما')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
