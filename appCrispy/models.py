from email import message
from email.policy import default
from pyexpat import model
from random import choices
from venv import create
from django.db import models
from multiselectfield import MultiSelectField

SITUATION = (
  ('Pending','Pending'),
  ('Approved','Approved'),
  ('Dissaproved','Dissaproved'),
)

PERSONALITY = (
  ( '', 'Select a personality'),
  ('I am introvert ', 'I am introvert '),
  ('I am extrovert ', 'I am extrovert '),
  ('I am sociable ', 'I am sociable '),
  ('I am antisociable ', 'I am antisociable '),
  ('I am serious', 'I am serious'),
)

SMOKER = (
  ('1','Yes'),
  ('2','No'),
)


FRAMEWORKS= (
  ('Laravel','Laravel'),
  ('Angular','Angular'),
  ('Django','Django'),
  ('Flask','Flask'),
  ('Vue','Vue'),
  ('Other','Other'),
)

LANGUAGES= (
  ('Python','Python'),
  ('Php','Php'),
  ('Javascript','Javascript'),
  ('C++','C++'),
  ('Java','Java'),
  ('Other','Other'),
)

DATABASES= (
  ('MySql','MySql'),
  ('Postgree','Postgree'),
  ('MongoDB','MongoDB'),
  ('SqLite3','SqLite3'),
  ('Oracle','Oracle'),
  ('Other','Other'),
)

LIBRARIES= (
  ('Ajax','Ajax'),
  ('Jquery','Jquery'),
  ('React','React'),
  ('Char.js','Char.js'),
  ('BootsTrap','BootsTrap'),
  ('Other','Other'),
)

MOBILE= (
  ('React Native','React Native'),
  ('Kivy','Kivy'),
  ('Flutter','Flutter'),
  ('Ionic','Ionic'),
  ('Xamarim','Xamarim'),
  ('Other','Other'),
)

OTHER= (
  ('UML','UML'),
  ('SQL','SQL'),
  ('Docker','Docker'),
  ('GIT','GIT'),
  ('GraphQL','GraphQL'),
  ('Others','Others'),
)

#EDUCATION
STATUS_COURSE = (
  ('','Select a status'),
  ("I'm studying ","I'm studying"),
  ("I'm took a break ","I'm took a break "),
  ("Completed ",'Completed'),
)



class Engineer (models.Model):
  #PERSONAL
  firstname = models.CharField(max_length=50) 
  lastname = models.CharField(max_length=50)
  job = models.CharField(max_length=5)
  age = models.CharField(max_length=2)
  email = models.EmailField(max_length=200)
  message = models.TextField()
  phone = models.CharField(max_length=10) 
  birthday = models.DateField(auto_now=False, auto_now_add=False)
  personality =  models.CharField(max_length=50,null=True,choices=PERSONALITY)
  salary = models.CharField(max_length=50)
  gender = models.CharField(max_length=7)
  experience = models.BooleanField(null=True)
  file = models.FileField( upload_to='documents/',blank=True, verbose_name='CV')
  image = models.ImageField(upload_to='images/', null=True, verbose_name='Image')
  smoker = models.CharField(max_length=3,null=True,choices=SMOKER,default='')    
  situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
  created_at = models.DateTimeField(auto_now_add=True)
  
  #SKILLS
  frameworks = MultiSelectField(choices=FRAMEWORKS, default = "")
  languages = MultiSelectField(choices=LANGUAGES, default = "")
  databases = MultiSelectField(choices=DATABASES, default = "")
  libraries = MultiSelectField(choices=LIBRARIES, default = "")
  mobile = MultiSelectField(choices=MOBILE, default = "")
  other = MultiSelectField(choices=OTHER, default = "")
  #EDUCATIONAL
  university = models.CharField(max_length=50)
  faculty = models.CharField(max_length=50)
  institution = models.CharField(max_length=50)
  course = models.CharField(max_length=50)
  start_course = models.DateField(auto_now=False, auto_now_add=False)
  end_course = models.DateField(auto_now=False, auto_now_add=False)
  about_course = models.TextField()
  status_course = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)
  #PROFESSIONAL
  company = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  start_work = models.DateField(auto_now=False, auto_now_add=False)
  end_work = models.DateField(auto_now=False, auto_now_add=False)
  about_work = models.TextField()
  employed = models.BooleanField(null=True, verbose_name="I'm employe")
  travel = models.BooleanField(null=True, verbose_name="I'm available for travel")
  remote = models.BooleanField(null=True, verbose_name="I'm to remote work")
  
  
  
  def clean (self):
    self.firstname = self.firstname.capitalize()
    self.lastname = self.firstname.capitalize()
  
  def __str__(self):
    return self.firstname 