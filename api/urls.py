from django.urls import path
from api import views


urlpatterns = [
    #function based views
    path('students/', views.studentViews),
    path('students/<int:pk>/', views.studentDetailViews),
    #Class based views
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetail.as_view())

]