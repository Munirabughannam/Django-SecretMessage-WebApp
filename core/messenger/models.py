from django.db import models


class MessageData(models.Model):
    unique_link = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.unique_link
