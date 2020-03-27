from django.urls import path,include
from . import views


urlpatterns = [
   path('create/',views.create,name='create'),
   path('main/',views.main,name='main'),
   path('enquiry/',views.enquiry,name='enquiry'),
   path('applied/',views.applied,name='applied'),
   path('detail/<int:pk>/',views.detail,name='detail'),
   path('registering/',views.registering,name='registering'),
   path('delete/<int:pk>/', views.delete, name='delete'),
   path('search/',views.search,name='search'),
   path('modify/<int:pk>/',views.modify,name='modify'),
   path('prac/',views.prac,name='prac'),
   path('apply/',views.apply,name='apply'),
   path('study/',views.study,name='study'),
   path('working/',views.working,name='working'),
   path('tourist/',views.tourist,name='tourist')
]
