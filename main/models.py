from django.db import models


class Quote(models.Model):
    text = models.TextField(unique=True)
    source = models.CharField(max_length=255)
    weight = models.FloatField(default=1.0)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.text} — {self.source}"

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(weight__gte=0),
                                   name='weight_non_negative')
        ]
