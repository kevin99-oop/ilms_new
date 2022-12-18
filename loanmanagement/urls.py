
from django.contrib import admin
from django.urls import path
from loan import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include
from customer.views import emi, loan, maintenance
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('adminloan/', admin.site.urls),


    path('customer/',include('customer.urls')),
    path('',views.home_view,name=''),
    path('logout', LogoutView.as_view(template_name='loan/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
   
    path('adminlogin', LoginView.as_view(template_name='loan/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-customer', views.admin_view_customer_view,name='admin-view-customer'),
    path('customer-view-customer', views.customer_view_customer_view,name='customer-view-customer'), 
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),
    

    path('admin-loan', views.admin_loan_view,name='admin-loan'),
    path('admin-add-loan', views.admin_add_loan_view,name='admin-add-loan'),
    path('admin-view-loan', views.admin_view_loan_view,name='admin-view-loan'),
    path('admin-update-loan', views.admin_update_loan_view,name='admin-update-loan'),
    path('update-loan/<int:pk>', views.update_loan_view,name='update-loan'),
    path('admin-delete-loan', views.admin_delete_loan_view,name='admin-delete-loan'),
    path('delete-loan/<int:pk>', views.delete_loan_view,name='delete-loan'),

    path('admin-view-loan-holder', views.admin_view_loan_holder_view,name='admin-view-loan-holder'),
    path('admin-view-approved-loan-holder', views.admin_view_approved_loan_holder_view,name='admin-view-approved-loan-holder'),
    path('admin-view-disapproved-loan-holder', views.admin_view_disapproved_loan_holder_view,name='admin-view-disapproved-loan-holder'),
    path('admin-view-waiting-loan-holder', views.admin_view_waiting_loan_holder_view,name='admin-view-waiting-loan-holder'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),
    # Change Password
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='customer/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),

     # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('emi/', emi ,name='emi'),
    path('loan/', loan ,name='loan'),
    path('maintenance/', maintenance, name='maintenance'),
    path('myform/', views.myform, name='myform'),
]
