from django.shortcuts import render
from rest_framework import generics;
from task.models import Course,Teacher,Student;
from task.serializers import *;
# Create your views here.
class CoursesView(generics.ListAPIView):
    queryset=Course.objects.all();
    serializer_class=CousersSerializer;
class CourseView(generics.RetrieveAPIView):
    model=Course;
    queryset=Course.objects.all();
    lookup_field='pk'
    serializer_class=CourseSerializer;
class CreateCourseView(generics.CreateAPIView):
    serializer_class=CourseSerializer;
    model=Course;
    queryset=Course.objects.all();
    lookup_field='pk';
class UpdateCourse(generics.UpdateAPIView):
    model=Course;
    lookup_field='pk';
    serializer_class=CourseSerializer;
    queryset=Course.objects.all();
class DeleteCourse(generics.DestroyAPIView):
    model=Course;
    lookup_field='pk';
    serializer_class=CourseSerializer;
    queryset=Course.objects.all();
class UpdateCourseStudents(generics.UpdateAPIView):
    model=Course;
    lookup_field='pk';
    serializer_class=EditCourseStudentSerializer;
    queryset=Course.objects.all();
class UpdateCourseTeachers(generics.UpdateAPIView):
    model=Course;
    lookup_field='pk';
    serializer_class=EditCourseTeacherSerializer;
    queryset=Course.objects.all();
class StudentsView(generics.ListAPIView):
    Model=Student;
    serializer_class=StudentsSerializer;
    queryset=Student.objects.all();
class ShowStudentView(generics.RetrieveAPIView):
    model=Student;
    lookup_field="pk";
    queryset=Student.objects.all();
    serializer_class=StudentsSerializer;
class AddStudentView(generics.CreateAPIView):
    model=Student;
    lookup_field="pk";
    queryset=Student.objects.all();
    serializer_class=StudentSerializer;
class UpdateStudentView(generics.UpdateAPIView):
    model=Student;
    lookup_field="pk";
    queryset=Student.objects.all();
    serializer_class=StudentSerializer;
class DeleteStudentView(generics.DestroyAPIView):
    model=Student;
    lookup_field="pk";
    queryset=Student.objects.all();
    serializer_class=StudentSerializer;
class TeachersView(generics.ListAPIView):
    model=Teacher;
    queryset=Teacher.objects.all();
    serializer_class=TeachersSerializer;
class ShowTeacherView(generics.RetrieveAPIView):
      model=Teacher;
      lookup_field='pk';
      queryset=Teacher.objects.all();
      serializer_class=TeacherSerializer;
class UpdateTeacherView(generics.UpdateAPIView):
      model=Teacher;
      lookup_field='pk';
      queryset=Teacher.objects.all();
      serializer_class=TeacherSerializer;
class AddTeacherView(generics.CreateAPIView):
      model=Teacher;
      lookup_field='pk';
      queryset=Teacher.objects.all();
      serializer_class=TeacherSerializer;

class DeleteTeacherView(generics.DestroyAPIView):
      model=Teacher;
      lookup_field='pk';
      queryset=Teacher.objects.all();
      serializer_class=TeacherSerializer;
