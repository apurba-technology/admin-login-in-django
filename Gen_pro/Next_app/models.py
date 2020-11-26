from django.db import models

# Create your models here.

class Banner(models.Model): 
    name = models.CharField(max_length=50)
    banner_image = models.ImageField(upload_to='images/')

class Notice(models.Model):
    title = models.CharField(max_length=20)
    description =models.TextField(max_length=150)
    attach_file = models.FileField(upload_to='notice/')

class Programme(models.Model):
    title = models.CharField(max_length=20)
    programme_mission = models.CharField(max_length=20)
    description =models.CharField(max_length=100)
    incharge_teacher = models.FileField(upload_to='images/')
    programme_image = models.FileField(upload_to='images/')

class admin_regestion_me(models.Model):
	name=models.CharField(max_length=20)
	e_mail=models.CharField(max_length=20)
	password=models.CharField(max_length=20)
	#password1=models.CharField(max_length=20)
	class Meta:
		db_table="Admin_Regestion"



    