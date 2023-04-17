from django.db import models
from django.contrib.auth.models import User

class Klient(models.Model):
    klient_name = models.CharField('Vardas', max_length=50)
    klient_last_name = models.CharField('Pavarde', max_length=50)
    klient_firm = models.CharField('Imone', max_length=50)
    klient_kontacts = models.CharField('Kontaktai', max_length=50)
    def __str__(self):
        return f'{self.klient_name} {self.klient_last_name}'
    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = 'Klientai'
# Create your models here.
class Projektas(models.Model):
    name = models.CharField('Pavadinimas', max_length=50)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    klient = models.ManyToManyField(Klient)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    workers = models.ForeignKey('Worker', on_delete=models.SET_NULL, null=True)
    job = models.ForeignKey('Job', on_delete=models.SET_NULL, null=True)
    accounts = models.ForeignKey('Account', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Projektas'
        verbose_name_plural = 'Projektai'

    def __str__(self):
        klient_names = [klient.klient_name for klient in self.klient.all()]
        return f'{self.name} {self.workers} {self.job} {self.accounts} ({", ".join(klient_names)})'


    def display_klient(self):
        klient_names = [klient.klient_name for klient in self.klient.all()]
        return ", ".join(klient_names)
    display_klient.short_description = 'Klientai'
    def display_worker(self):
        return f'{self.workers.worker_name}  {self.workers.worker_last_name}' if self.workers else ""
    display_worker.short_description = 'Darbotojai'
    def display_job(self):
        return f'{self.job.job_name}' if self.job else ""
    display_job.short_description = 'Darbas'
    def display_account(self):
        return f'{self.accounts.ammount_of_money}' if self.accounts else ""
    display_account.short_description = 'Saskaitahhhhh'



class Worker(models.Model):
    worker_name = models.CharField('Vardas', max_length=50)
    worker_last_name = models.CharField('Pavarde', max_length=50)
    worker_duty = models.CharField('Pareigos', max_length=50)
    def __str__(self):
        return f'{self.worker_name} {self.worker_last_name}'
    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = 'Darbuotojai'


class Job(models.Model):
    job_name = models.CharField('Pavadinimas', max_length=50)
    job_note = models.CharField('Pastabos', max_length=50)
    def __str__(self):
        return f'{self.job_name}'
    class Meta:
        verbose_name = 'Darbas'
        verbose_name_plural = 'Darbai'


class Account(models.Model):
    date_of_issue = models.DateField('Išrašymo data')
    ammount_of_money = models.FloatField('Suma')
    def __str__(self):
        return f'{self.ammount_of_money}'
    class Meta:
        verbose_name = 'Saskaita'
        verbose_name_plural = 'Saskaitos'
