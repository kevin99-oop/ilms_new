from django import forms
from django.contrib.auth.models import User
from . import models

class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


class CategoryForm(forms.ModelForm):
    class Meta:
        model=models.Category
        fields=['category_name']

class LoanForm(forms.ModelForm):
    category=forms.ModelChoiceField(queryset=models.Category.objects.all(),empty_label="Category Name", to_field_name="id")
    class Meta:
        model=models.Loan
        fields=['loan_name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }




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

class ApprovalForm(forms.Form):
	firstname=forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder': 'Enter Firstname','class':'abc'}))
	lastname=forms.CharField(max_length=120,widget=forms.TextInput(attrs={'placeholder': 'Enter Lastname','class':'abc'}))
	Dependents=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Number of Dependents','class':'abc'}))
	ApplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Monthly Gross Income','class':'abc'}))
	CoapplicantIncome=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter Co-Applicant Monthly Gross Income','class':'abc'}))
	LoanAmount=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Requested Loan Amount','class':'abc'}))
	Loan_Amount_Term=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Loan Term in Months','class':'abc'}))
	Credit_History=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Enter your Credit History','class':'abc'}))
	Gender=forms.ChoiceField( choices=GENDER_CHOICES,widget=forms.Select(attrs={'class':'abc'}))
	Married=forms.ChoiceField( choices=MARRIED_CHOICES,widget=forms.Select(attrs={'class':'abc'}))
	Education=forms.ChoiceField(choices=GRADUATED_CHOICES,widget=forms.Select(attrs={'class':'abc'}))
	Self_Employed=forms.ChoiceField(choices=SELFEMPLOYED_CHOICES,widget=forms.Select(attrs={'class':'abc'}))
	Property_Area=forms.ChoiceField(choices=PROPERTY_CHOICES,widget=forms.Select(attrs={'class':'abc'}))

	# gender=forms.CharField(max_length=150, choices=[('Male', 'Male'),('Female', 'Female')])
	# married=forms.CharField(max_length=150, choices=[('Yes', 'Yes'),('No', 'No')])
	# graduatededucation=forms.CharField(max_length=150, choices=[('Graduate', 'Graduated'),('Not_Graduate', 'Not_Graduate')])
	# selfemployed=forms.CharField(max_length=150, choices=[('Yes', 'Yes'),('No', 'No')])
	# area=forms.CharField(max_length=150, choices=[('Rural', 'Rural'),('Semiurban', 'Semiurban'),('Urban', 'Urban')])
	def save(self, commit=True):
		user = super(ApprovalForm, self).save(commit=False)
		if commit:
			user.save()
		return user
