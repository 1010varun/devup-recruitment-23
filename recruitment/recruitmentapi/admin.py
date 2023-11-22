from django.contrib import admin
from .models import *
from django.core.mail import send_mail, EmailMessage
from django.core import mail
from django.template.loader import render_to_string
import threading
from threading import Thread
from django.conf import settings
from import_export.admin import ImportExportModelAdmin

class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, bcc=self.recipient_list)
        msg.content_subtype = "html"
        msg.send()

def send_html_mail(subject, html_content, recipient_list):
    EmailThread(subject, html_content, recipient_list).start()


class recruitmentsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = recruitment
    fields = ['name', 'personal_email', 'kiet_email', 'library_id', 'phone', 'gender', 'mode_of_payment', 'desk', 'payment_status',]

    list_display = ('name', 'payment_status', 'personal_email', 'id')

    list_per_page = 80

    # list_filter = ()

    # search_fields = ()

    ordering = ('name', 'id')

    actions = ["send_confirmation_mail"]
   

    def send_confirmation_mail(self, request, queryset):
        connection = mail.get_connection()
        pl =[]
        for i in queryset:
            if i.personal_email:
                pl.append(i.personal_email)

        connection.open()
        message= render_to_string('confirmation.html')
        send_html_mail('DevUp Recruitment | Registration Successful',message,pl)

        connection.close()
        queryset.update(payment_status=True)
    send_confirmation_mail.short_description = "Send an email for due paymemt"


admin.site.register(recruitment, recruitmentsAdmin)
