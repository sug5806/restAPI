from django.urls import path
from .views import *


app_name = 'student'

urlpatterns = [
    path('', Student_list.as_view(), name='list'),
    # path('create/', Student_Create.as_view(), name='create'),
    path('list/', Studentlist.as_view()),
    path('create/', StudentCreate.as_view()),
    path('list/<int:year>/<int:month>/', StudentDate.as_view()),
    path('list/<cls>/', StudentCls.as_view()),
    path('list/<cls>/<int:year>/<int:month>', StudentDateCls.as_view()),
]