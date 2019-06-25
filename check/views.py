from django.shortcuts import render
from rest_framework.response import Response

from .models import Student
from django.views.generic import CreateView, ListView
from .forms import MyModelForm
from django.views.generic import CreateView, ListView

from .forms import MyModelForm
from .models import Student


# Create your views here.


class Student_Create(CreateView):
    # model = Student
    template_name = 'check/student_create.html'
    # fields = ['name', 'cls_type', 'test', 'date']
    form_class = MyModelForm
    

class Student_list(ListView):
    model = Student
    template_name = 'check/student_list.html'


from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student


class Studentlist(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(generics.CreateAPIView):
    serializer_class = StudentSerializer



class StudentDate(generics.ListAPIView):
    def list(self, request, *args, **kwargs):
        if 'year' in kwargs and 'month' in kwargs:
            year = kwargs['year']
            month = kwargs['month']
        print("year   : ", year)
        print("month   : ", month)

        queryset = Student.objects.filter(date__year=year, date__month=month)
        print(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    serializer_class = StudentSerializer


class StudentCls(generics.ListAPIView):
    serializer_class = StudentSerializer

    def list(self, request, *args, **kwargs):
        if 'cls' in kwargs:
            cls = kwargs['cls']

        print("cls   : ", cls)

        queryset = Student.objects.filter(cls_t__cls_type=cls)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class StudentDateCls(generics.ListAPIView):
    serializer_class = StudentSerializer
    ordering_fields = ('date', '-name')
    ordering = ('date', 'name')

    def list(self, request, *args, **kwargs):
        if 'cls' in kwargs:
            cls = kwargs['cls']

        else:
            cls = None

        if 'year' in kwargs and 'month' in kwargs:
            year = kwargs['year']
            month = kwargs['month']

        else:
            year = None
            month = None

        print('cls:  ', cls)
        print('year:   ', year)
        print('month:   ',  month)

        queryset = Student.objects.filter(cls_t__cls_type=cls, date__year=year, date__month=month).order_by('date', 'name')

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
