from django.shortcuts import render
from rest_framework.response import Response

from .models import *
from django.views.generic import CreateView, ListView

from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny


# # Create your views here.


class Student_Create(CreateView):
    model = student
    template_name = 'check/student_create.html'
    fields = '__all__'
    # form_class = MyModelForm


class Student_list(ListView):
    model = student
    template_name = 'check/student_list.html'


# ############# REST_frame_work
#
from rest_framework import generics
from .serializers import *

class Studentlist(generics.ListAPIView):

    queryset = student.objects.all()
    serializer_class = studentSerializer


class StudentCreate(generics.CreateAPIView):
    serializer_class = studentSerializer


class NameCreate(generics.CreateAPIView):
    serializer_class = nameSerializer


class UserCreateAPI(generics.CreateAPIView):
    queryset = manager.objects.all()
    serializer_class = userCreateSerializer
    permission_classes = (AllowAny, )


class StudentDetail(generics.RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = studentDetailSerializer
    lookup_field = 'name'

    def retrieve(self, request, *args, **kwargs):

        queryset = student.objects.filter(name__name=kwargs['name'])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class Studentlist(generics.ListAPIView):
    queryset = student.objects.all()
    serializer_class = studentSerializer
    def list(self, request, *args, **kwargs):

        user_cls = request.user.cls

        queryset = student.objects.filter(cls__cls=user_cls).order_by('name', 'date')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# class StudentDate(generics.ListAPIView):
#     def list(self, request, *args, **kwargs):
#         if 'year' in kwargs and 'month' in kwargs:
#             year = kwargs['year']
#             month = kwargs['month']
#
#         queryset = Student.objects.filter(date__year=year, date__month=month)
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     serializer_class = StudentSerializer
#
#
# class StudentCls(generics.ListAPIView):
#     serializer_class = StudentSerializer
#
#     def list(self, request, *args, **kwargs):
#         if 'cls' in kwargs:
#             cls = kwargs['cls']
#
#         queryset = Student.objects.filter(cls_t__cls_type=cls)
#
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class StudentDateCls(generics.ListAPIView):
#     serializer_class = StudentSerializer
#     ordering_fields = ('date', '-name')
#     ordering = ('date', 'name')
#
#     def list(self, request, *args, **kwargs):
#         if 'cls' in kwargs:
#             cls = kwargs['cls']
#
#         else:
#             cls = None
#
#         if 'year' in kwargs and 'month' in kwargs:
#             year = kwargs['year']
#             month = kwargs['month']
#
#         else:
#             year = None
#             month = None
#
#         queryset = Student.objects.filter(cls_t__cls_type=cls, date__year=year, date__month=month).order_by('date', 'name')
#
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
