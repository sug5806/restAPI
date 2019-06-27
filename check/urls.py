from django.urls import path
from .views import *
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'student'

urlpatterns = [
    path('', Student_list.as_view(), name='list'),
    path('create/', Student_Create.as_view(), name='create'),
    path('create/student/', StudentCreate.as_view()),
    path('create/name/', NameCreate.as_view()),
    path('admin/create/', UserCreateAPI.as_view(), name='user_create'),
    path('api/get_token/', obtain_auth_token),
    path('list/std/', Studentlist.as_view()),
    path('detail/<name>/', StudentDetail.as_view()),
    # path('list/<int:year>/<int:month>/', StudentDate.as_view()),
    # path('list/<cls>/', StudentCls.as_view()),
    # path('list/<cls>/<int:year>/<int:month>', StudentDateCls.as_view()),
]