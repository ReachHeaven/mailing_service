import pytz as pytz
from django.db import models


class Mailing(models.Model):
    start_datetime = models.DateTimeField(verbose_name="Time to start")
    content = models.TextField(verbose_name="Text to send")
    operator = models.CharField(max_length=3, verbose_name="Operator")
    end_datetime = models.DateTimeField(verbose_name="Time to end")

    def __str__(self):
        return f"Mailing {self.id} from {self.start_datetime} to {self.end_datetime}"


class Client(models.Model):
    TIMEZONES = tuple((idx, tz) for idx, tz in enumerate(pytz.all_timezones))

    phone_number = models.CharField(verbose_name="Phone number", max_length=11)
    operator_code = models.CharField(max_length=3, verbose_name="Operator code")
    timezone = models.CharField(verbose_name='Time zone', max_length=32, choices=TIMEZONES, default='UTC')

    def __str__(self):
        return f'Client {self.id} with number {self.phone_number}'

class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]

    time_create = models.DateTimeField(verbose_name='Time create', auto_now_add=True)
    sending_status = models.CharField(verbose_name='Sending status', max_length=15, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f'Message {self.id} with text {self.mailing} for {self.client}'

