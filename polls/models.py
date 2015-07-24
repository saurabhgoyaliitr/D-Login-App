from django.db import models
from django.utils import timezone

class Question(models.Model):
    def  __unicode__(self): 
        return self.question_text
    def was_pub_rec(self) :
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

    question_text  = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published') 




class Choice(models.Model): 
    def __unicode__(self) :  
        return self.choice_text

    question = models.ForeignKey(Question)
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default=0) 


