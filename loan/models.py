from django.db import models
from django.contrib.auth.models import User
from customer.models import Customer
class Category(models.Model):
    category_name =models.CharField(max_length=20)
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.category_name

class Loan(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    loan_name = models.CharField(max_length=200)
    creation_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.loan_name

class LoanRecord(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Loan = models.ForeignKey(Loan, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=100,default='Pending')
    creation_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.loan

class Question(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    description =models.CharField(max_length=500)
    admin_comment=models.CharField(max_length=200,default='Nothing')
    asked_date =models.DateField(auto_now=True)
    def __str__(self):
        return self.description



# Create your models here.
class Approvals(models.Model):
	GENDER_CHOICES = (
		('Male', 'Male'),
		('Female', 'Female')
	)
	MARRIED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	GRADUATED_CHOICES = (
		('Graduate', 'Graduated'),
		('Not_Graduate', 'Not_Graduate')
	)
	SELFEMPLOYED_CHOICES = (
		('Yes', 'Yes'),
		('No', 'No')
	)
	PROPERTY_CHOICES = (
		('Rural', 'Rural'),
		('Semiurban', 'Semiurban'),
		('Urban', 'Urban')
	)

	firstname=models.CharField(max_length=120)
	lastname=models.CharField(max_length=120)
	Dependents=models.IntegerField(default=0)
	Applicantincome=models.IntegerField(default=0)
	Coapplicatincome=models.IntegerField(default=0)
	LoanAmount=models.IntegerField(default=0)
	Loan_Amount_Term=models.IntegerField(default=0)
	Credit_History=models.IntegerField(default=0)
	Gender=models.CharField(max_length=150, choices=GENDER_CHOICES)
	Married=models.CharField(max_length=150, choices=MARRIED_CHOICES)
	Education=models.CharField(max_length=150, choices=GRADUATED_CHOICES)
	Self_Employed=models.CharField(max_length=150, choices=SELFEMPLOYED_CHOICES)
	Property_Area=models.CharField(max_length=150, choices=PROPERTY_CHOICES)

	def __str__(self):
		return self.firstname

