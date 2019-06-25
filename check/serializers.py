from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    # test = serializers.RelatedField(many=True)

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

#
# class StudentTp(serializers.ModelSerializer):
#     student = StudentSerializer(source='student_set', many=True)
#
#     class Meta:
#         model = Test
#         fields = '__all__'
#
