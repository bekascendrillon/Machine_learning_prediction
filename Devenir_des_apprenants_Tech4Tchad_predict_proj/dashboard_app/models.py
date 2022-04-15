from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
    )

class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveBigIntegerField(validators=[MinValueValidator(22), MaxValueValidator(39)], null=True)	
    sex = models.PositiveBigIntegerField(choices=GENDER, null=True)
    niveau = models.PositiveBigIntegerField(validators=[MinValueValidator(2), MaxValueValidator(5)], null=True)
    predictions = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_Devenir_des_apprenants_Tech4Tchad_model.joblib')
        self.predictions = ml_model.predict([[self.age, self.sex, self.niveau]])
        return super().save(*args, **kwargs)

class Meta:
    ordering = ['-date']

def __str__(self):
    return self.name
