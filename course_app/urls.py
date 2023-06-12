from django.urls import path
from course_app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('course/',views.course,name='course'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('delete_all',views.delete_all,name='delete_all'),
    path('edit/<int:id>',views.edit,name='edit')
] 