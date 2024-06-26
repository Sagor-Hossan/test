from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models import Sum

class customUser(AbstractUser):
    GENDER = [('male','Male'),('female','Female')]
    GOAL = [('lose_weight','Lose Weight'),('gain_weight','Gain Weight'),('maintain_weight','Maintain Weight')]

    name = models.CharField(max_length=50,null=True,blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic/',null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    height = models.FloatField(null=True,blank=True)
    weight = models.FloatField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER,null=True,blank=True)
    goal = models.CharField(max_length=20,choices=GOAL,null=True,blank=True)

    def __str__(self):
        return self.username

# class userWeight(models.Model):
#     user = models.ForeignKey(customUser,on_delete=models.CASCADE)
#     weight = models.FloatField()
#     date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.user.username

class ConsumedCalories(models.Model):
    user = models.ForeignKey(customUser, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    calorie_consumed = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True, null=True)
    time = models.TimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.item_name


class foodModel(models.Model):
    user = models.ForeignKey(customUser,on_delete=models.CASCADE)
    food_name = models.CharField(max_length=50)
    calories = models.FloatField(null=True)
    image = models.ImageField(upload_to='food_pics/')

    def __str__(self):
        return self.food_name
