from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class QuizCategory(models.Model):
    Title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
    description=models.CharField(max_length=100)
    def __str__(self):
        return self.Title

    
    
class QuizQuestions(models.Model):
    category=models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    question=models.TextField()
    opt_1=models.CharField(max_length=200)
    opt_2=models.CharField(max_length=200)
    opt_3=models.CharField(max_length=200)
    opt_4=models.CharField(max_length=200)
    level=models.CharField(max_length=150)
    time_limit=models.IntegerField()
    right_opt=models.CharField(max_length=200)
    
    def __str__(self):
        return self.question
    
    
class UserSubmitAnswer(models.Model):
    question=models.ForeignKey(QuizQuestions,on_delete=models.CASCADE,default="")
    right_answer=models.CharField(max_length=200,default="")
    user=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    category=models.ForeignKey(QuizCategory,on_delete=models.CASCADE,default="")
    
    
    
class UserTotalScore(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Score=models.IntegerField()
    category=models.ForeignKey(QuizCategory,on_delete=models.CASCADE)
    Total=models.IntegerField()
    percentage=models.FloatField()
    
class CertifiedAlready(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(QuizCategory,on_delete=models.CASCADE,default=" ")
    certified=models.BooleanField(default=False)
    date_issue=models.DateTimeField(auto_now=True)
    
  


    
    
    

    
    

# Create your models here.
