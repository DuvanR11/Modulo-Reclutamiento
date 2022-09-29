import datetime
from importlib.resources import contents
from secrets import choice
from tkinter import Widget
from django import forms
from appCrispy.models import Engineer, SMOKER
from django.core.validators import RegexValidator

#Every letters to lowercase
class Lowercase(forms.CharField):
    def to_python(self, value):
        return value.lower()

#Every letters to uppercase
class Uppercase(forms.CharField):
    def to_python(self, value):
        return value.upper()

class EngineerForm (forms.ModelForm):
  
  SALARY = (
  ('', 'Salary expectation (month)'),
  ('Between ($3000 and $4000)', 'Between ($3000 and $4000)'),
  ('Between ($4000 and $5000)', 'Between ($4000 and $5000)'),
  ('Between ($5000 and $6000)', 'Between ($5000 and $6000)'),
  ('Between ($7000 and $8000)', 'Between ($7000 and $8000)'),
  )
  
  SITUATION = (
  ('Pending','Pending'),
  ('Approved','Approved'),
  ('Dissaproved','Dissaproved'),
  )
  
  #VALIDATIONS
  
  firstname = forms.CharField(label='First Name', min_length=3, max_length=50,  validators=[RegexValidator(regex='^[a-zA-ZÀ-ÿ\s]*$', message='Only letters are allowed')],
                              error_messages={'required':'SYNTAX ERROR!'} , widget=forms.TextInput(attrs={'placeholder': 'Enter First Name', 'style': 'text-transform: capitalize'}))
  
  lastname = forms.CharField(label='Last Name', min_length=3, max_length=50, validators=[RegexValidator(regex='^[a-zA-ZÀ-ÿ\s]*$', message='Only letters are allowed')],
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'style': 'text-transform: capitalize'}))
  
  # situation = forms.ChoiceField (label='Situation', choices=SITUATION , widget=forms.Select(attrs={'placeholder': 'Select a situation'}))

  job =  Uppercase (label='Job Code', min_length=5, max_length=5, 
                            widget=forms.TextInput(attrs={'placeholder': 'Example: IT-001','style': 'text-transform: uppercase'}))
  
  email = Lowercase (label='Email', min_length=8, max_length=50, validators=[RegexValidator(regex='[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', message='Put a valid email address!')],
                              widget=forms.TextInput(attrs={'placeholder': 'Mail', 'style': 'text-transform: lowercase'}))
  
  age = forms.CharField(label='Age', min_length=2, max_length=2, validators=[RegexValidator(regex='^[0-9]*$', message='Only numbers are allowed')], 
                        widget=forms.TextInput(attrs={'placeholder': 'Enter Age'}))
  
  experience = forms.BooleanField(label='I have experience', required=False,)
  
  salary = forms.ChoiceField (label='Salary', choices=SALARY , widget=forms.Select(attrs={'placeholder': 'Select a salary expectation'}))
  
  
  message = forms.CharField(label='About you', max_length=5000,
                        required=False,
                        widget=forms.Textarea(attrs={'placeholder': 'Enter a little description about yourself', 'rows': '5', 'cols': '50'}))
  
  file = forms.FileField(label='Upload your CV', required=False,)
  
  image = forms.ImageField(label='Upload your photo', required=False,)
  
  phone = forms.CharField(label='Phone', min_length=10, max_length=10, validators=[RegexValidator(regex='^[0-9]*$', message='Only numbers are allowed')], 
                        widget=forms.TextInput(attrs={'placeholder': 'Enter Phone', }))

  birthday = forms.DateField(label='Birthday', widget=forms.DateInput(attrs={'placeholder': 'Enter your birthday', 'type': 'date'}))
  
  
  university = forms.CharField(label='University', min_length=3, max_length=50,
                            
                              widget=forms.TextInput(attrs={'placeholder': 'Enter University', 'style': 'text-transform: capitalize'}))
  faculty = forms.CharField(label='Faculty', min_length=3, max_length=50,
                            
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Faculty', 'style': 'text-transform: capitalize'}))
  institution = forms.CharField(label='Institution', min_length=3, max_length=50,
                            
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Institution', 'style': 'text-transform: capitalize'}))
  
  course = forms.CharField(label='Course', min_length=3, max_length=50,
                             
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Course', 'style': 'text-transform: capitalize'}))
  
  start_course = forms.DateField(label='Start Course', widget=forms.DateInput(attrs={'placeholder': 'Enter your start course', 'type': 'date'}))

  end_course = forms.DateField(label='End Course', widget=forms.DateInput(attrs={'placeholder': 'Enter your end course', 'type': 'date'}))
  
  about_course = forms.CharField(label='About your course', max_length=5000,
                              required=False,
                              widget=forms.Textarea(attrs={'placeholder': 'Enter a little description about your course', 'rows': '5', 'cols': '50'}))
  
  company = forms.CharField(label='Company', min_length=3, max_length=50,
                              
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Company', 'style': 'text-transform: capitalize'}))
  
  position = forms.CharField(label='Position', min_length=3, max_length=50,
                              
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Position', 'style': 'text-transform: capitalize'}))
  
  start_work = forms.DateField(label='Start Work', widget=forms.DateInput(attrs={'placeholder': 'Enter your start work', 'type': 'date'}))
  
  end_work = forms.DateField(label='End Work', widget=forms.DateInput(attrs={'placeholder': 'Enter your end work', 'type': 'date'}))
  
  employed = forms.BooleanField(label='I am employed', )
  
  travel = forms.BooleanField(label='I am traveling', )
  
  remote = forms.BooleanField(label='I am remote', )
  
  about_work = forms.CharField(label='About your work', max_length=5000,
                              required=False,
                              widget=forms.Textarea(attrs={'placeholder': 'Enter a little description about your work', 'rows': '5', 'cols': '50'}))
  

  
  GENDER = [('M', 'Male'),('F', 'Female')]  
  gender = forms.CharField (label='Gender', widget=forms.RadioSelect (choices=GENDER))
  smoker = forms.CharField (label='Smoker', widget=forms.RadioSelect (choices=SMOKER))
 
  
  class Meta:  
    model = Engineer
    exclude = ['created_at', 'situation']
    widgets = {
        # 'personality': forms.Select(attrs={'style': 'font-size: 13px'}),
        'image': forms.FileInput(attrs={'accept': 'image/png, image/jpeg'}),
        'file': forms.FileInput(attrs={'accept': 'application/pdf,'}),
    }
    
    
    
  #LIST ALL THE FIELDS THAT ARE DISABLED
  
  def __init__ (self, *args, **kwargs):
    super (EngineerForm, self).__init__(*args, **kwargs)
    
    instance = getattr (self, 'instance', None)
    list = ['firstname', 'lastname', 'email', 'phone', 'job', 'age','message','birthday','personality',
                       'salary','gender','experience','file','image','smoker',
                       'frameworks','languages', 'databases', 'libraries', 'mobile', 'other',
                       'university','faculty' ,'institution', 'course' ,'start_course' ,'end_course', 'about_course', 'status_course',
                       'company', 'position', 'start_work', 'end_work', 'about_work', 'employed' ,'travel' ,'remote',]
    
    for field in list:
      if instance and instance.pk:
        self.fields[field].disabled = True
      
  
  #VALIDATIONS
  
  def clean_job (self):
    job = self.cleaned_data['job']
    if job == 'FR-22' or job == 'BA-33' or job == 'FK-23':
      return job
    else:
      raise forms.ValidationError('Invalid job code')
    
    
  # def clean_file  (self):
  #   file = self.cleaned_data['file']
  #   content_type = file.content_type
  #   if content_type == 'application/pdf':
  #     return file
  #   else:
  #     raise forms.ValidationError('Invalid file, please upload a PDF file')
 
  def clean_start_course (self):
    start_course = self.cleaned_data['start_course']
    if start_course > datetime.date.today():
        raise forms.ValidationError('Invalid start course')
    return start_course
  
  def clean_end_course (self):
    end_course = self.cleaned_data['end_course']
    if end_course > datetime.date.today():
        raise forms.ValidationError('Invalid end course')
    return end_course


