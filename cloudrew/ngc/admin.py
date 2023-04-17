from django.contrib import admin
from .models import Projektas, Klient, Worker, Job, Account
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    model = Projektas
    list_display = ('name', 'display_klient', 'display_worker', 'display_job', 'display_account')


class KlientAdmin(admin.ModelAdmin):
    model = Klient
    list_display = ('klient_name', 'klient_last_name', 'klient_firm', 'klient_kontacts')


class WorkerAdmin(admin.ModelAdmin):
    model = Worker
    list_display = ('worker_name', 'worker_last_name', 'worker_duty')


class JobAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('job_name', 'job_note')


class AccountAdmin(admin.ModelAdmin):
    model = Job
    list_display = ('date_of_issue', 'ammount_of_money')


admin.site.register(Projektas, ProjectAdmin)
admin.site.register(Klient, KlientAdmin)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(Account, AccountAdmin)