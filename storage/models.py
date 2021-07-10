from django.db import models
from datetime import datetime, timedelta

class Data(models.Model):
    name = models.CharField(max_length=50)
    num = models.IntegerField(default=0)
    term = models.DateField(null=True)
    memo = models.TextField(null=True)
    def is_today(self):
        delta=timedelta(days=2)
        if (self.term.today()<=self.term) and (self.term<=self.term.today()+delta):
            return True
        else:
            return False

    def __str__(self):
        return self.name