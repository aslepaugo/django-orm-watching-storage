from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        entered_at = self.entered_at

        if self.leaved_at:
            leaved_at = self.leaved_at
        else:
            leaved_at = localtime()

        duration = (leaved_at - entered_at).total_seconds()
        return duration

    def format_duration(self):
        duration = self.get_duration()
        hours = int(duration)//3600
        minutes = int((duration % 3600)//60)
        return f"{hours}:{minutes}"

    def is_visit_long(self, visit_limit=3600):
        duration = self.get_duration()
        return duration >= visit_limit
