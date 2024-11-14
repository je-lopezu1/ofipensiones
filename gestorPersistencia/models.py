from django.db import models

class Hash(models.Model):
    id = models.IntegerField(primary_key=True)
    hash = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.id} - {self.hash}"


