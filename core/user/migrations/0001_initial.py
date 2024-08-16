# Generated by Django 5.1 on 2024-08-16 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='media/user_covers')),
                ('address', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Обычныйй пользователь'), (2, 'Менеджер'), (3, 'Бугхалтер')], default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
