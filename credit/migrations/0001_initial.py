# Generated by Django 3.2 on 2023-03-13 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('citizenship', models.CharField(max_length=20, verbose_name='Национальность')),
                ('birth_year', models.DateField(verbose_name='Дата рождения')),
                ('work_place', models.CharField(max_length=30, verbose_name='Место работы')),
            ],
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField(verbose_name='Сумма')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.client', verbose_name='Аккаунт')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, verbose_name='Номер')),
                ('account_type', models.IntegerField(verbose_name='Тип')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='credit.client', verbose_name='Клиент')),
            ],
        ),
    ]
