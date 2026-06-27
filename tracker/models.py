from django.db import models
from django.contrib.auth.models import User

class FoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()
    protein = models.FloatField(default=0)   # grams
    carbs = models.FloatField(default=0)     # grams
    fat = models.FloatField(default=0)       # grams
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-id']

    def __str__(self):
        return f"{self.name} ({self.calories} kcal) - {self.user.username}"
