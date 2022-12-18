from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.db.models import Q
from django.core.mail import send_mail
from loan import models as CMODEL
from loan import forms as CFORM
from django.contrib.auth.models import User
from django.http import HttpResponse
from PIL import Image
import pytesseract 
import pytesseract
from PIL import ImageEnhance, ImageFilter, Image
import pytesseract

from PIL import Image
import os
from .models import Customer
def ocr(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text


def handle_uploaded_file(f):
    with open('profile_pic/Customer/'+str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def customerclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'customer/customerclick.html')

def customer_signup_view(request):
    userForm=forms.CustomerUserForm()
    customerForm=forms.CustomerForm()
    mydict={'userForm':userForm,'customerForm':customerForm}
    if request.method=='POST':
        fileName = request.FILES['file']
        #request.POST['profile_pic'] = "profile_pic/Customer/"+str(fileName)
        userForm=forms.CustomerUserForm(request.POST)
        customerForm=forms.CustomerForm(request.POST,request.FILES)
        handle_uploaded_file(fileName)
        text = ocr("profile_pic/Customer/"+str(fileName)) 
        if "income tax department" in text.lower():
            print("\n\npan card\n\n")
        else:
            print("\n\nNo pan card Ditected\n\n")
            return render(request,'customer/customersignup.html',context=mydict)
        print("before if")
        if userForm.is_valid():
            print("user form valid")
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            customer=Customer()
            customer.user=user
            customer.mobile = request.POST['mobile']
            customer.address = request.POST['address']
            customer.profile_pic = "profile_pic/Customer/"+str(fileName)
            customer.card_text = text
            customer.credit_score = request.POST['credit_score']
            customer.asset_value = request.POST['asset_value']
            customer.monthly_income = request.POST['monthly_income']
            customer.save()
            print("user created")
            my_customer_group = Group.objects.get_or_create(name='CUSTOMER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('customerlogin')
    return render(request,'customer/customersignup.html',context=mydict)

def is_customer(user):
    return user.groups.filter(name='CUSTOMER').exists()

@login_required(login_url='customerlogin')
def customer_dashboard_view(request):
    dict={
        'customer':models.Customer.objects.get(user_id=request.user.id),
        'available_loan':CMODEL.Loan.objects.all().count(),
        'applied_loan':CMODEL.LoanRecord.objects.all().filter(customer=models.Customer.objects.get(user_id=request.user.id)).count(),
        'total_category':CMODEL.Category.objects.all().count(),
        'total_question':CMODEL.Question.objects.all().filter(customer=models.Customer.objects.get(user_id=request.user.id)).count(),

    }
    return render(request,'customer/customer_dashboard.html',context=dict)

def apply_loan_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    loans = CMODEL.Loan.objects.all()
    return render(request,'customer/apply_loan.html',{'loans':loans,'customer':customer})

def apply_view(request,pk):
    customer = models.Customer.objects.get(user_id=request.user.id)
    loan = CMODEL.Loan.objects.get(id=pk)
    loanrecord = CMODEL.LoanRecord()
    loanrecord.Loan = loan
    loanrecord.customer = customer
    loanrecord.save()
    return redirect('history')

def history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    loans = CMODEL.LoanRecord.objects.all().filter(customer=customer)
   
    return render(request,'customer/history.html',{'loans':loans,'customer':customer})
    
def ask_question_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    questionForm=CFORM.QuestionForm() 
    
    if request.method=='POST':
        questionForm=CFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            
            question = questionForm.save(commit=False)
            question.customer=customer
            question.save()
            return redirect('question-history')
    return render(request,'customer/ask_question.html',{'questionForm':questionForm,'customer':customer})

def question_history_view(request):
    customer = models.Customer.objects.get(user_id=request.user.id)
    questions = CMODEL.Question.objects.all().filter(customer=customer)
    return render(request,'customer/question_history.html',{'questions':questions,'customer':customer})

def emi(request):
    return render(request, 'customer/emi.html')

def loan(request):
    return render(request, 'customer/loan.html')


def maintenance(request):
    return render(request, 'customer/maintenance.html')
