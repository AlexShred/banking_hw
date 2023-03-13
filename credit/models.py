from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name="Имя клиента")
    citizenship = models.CharField(max_length=20, verbose_name="Национальность")
    birth_year = models.DateField(verbose_name="Дата рождения")
    work_place = models.CharField(max_length=30, verbose_name="Место работы")

    def __str__(self):
        return f'Клиент {self.name}, {self.citizenship}, {self.birth_year}, {self.work_place}'


class Account(models.Model):
    number = models.CharField(max_length=16, verbose_name="Номер")
    account_type = models.IntegerField(verbose_name="Тип")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")

    def __str__(self):
        return f'Аккаунт {self.number}, {self.account_type}, {self.client_id}'


class Credit(models.Model):
    sum = models.IntegerField(verbose_name="Сумма")
    date = models.DateTimeField(auto_now=True, verbose_name="Дата")
    account = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Аккаунт")

    def __str__(self):
        return f'Клиент {self.sum}, {self.date}, {self.account_id}'
