from django.urls import path
from app import views


urlpatterns = [
    path('',views.home,name="home"),
    path('adminR/',views.adminR,name="adminR"),
    path('addbook/',views.addbook,name="addbook"),
    path('show/',views.show,name="show"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('edit/<int:id>/',views.edit,name="edit"),
    path('update/<int:id>/',views.update,name="update"),
    path('student/',views.student,name="student")
]
