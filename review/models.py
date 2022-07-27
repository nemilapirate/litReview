from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

from ticket.models import Ticket

CHOICES = ((0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"))


class Review(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        verbose_name='Note'
    )
    headline = models.CharField(max_length=128, verbose_name='Titre')
    body = models.TextField(max_length=8192, blank=True, verbose_name='Commentaire')
    time_created = models.DateTimeField(auto_now_add=True)
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

