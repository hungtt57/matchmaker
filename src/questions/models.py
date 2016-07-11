from django.db import models

# Create your models here.



class Question(models.Model):
	text = models.TextField()
	active = models.BooleanField(default=True)
	draft =  models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	# answers = models.ManyToManyField('Answer')

	def __unicode__(self): #def __str__
		return self.text[:10]  #only show 10 text


class Answer(models.Model):
	question = models.ForeignKey(Question)
	text = models.CharField(max_length=120)
	active = models.BooleanField(default=True)
	draft =  models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)

	def __unicode__(self): #def __str__
		return self.text[:10]  #only show 10 text
