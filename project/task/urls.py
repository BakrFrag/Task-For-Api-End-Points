from django.urls import path
from task.views import *;
urlpatterns = [
    path('courses/',CoursesView.as_view(),name="courses"),
    path("courses/create/",CreateCourseView.as_view(),
    name="create"),
    path("courses/<pk>/",CourseView.as_view(),name="course"),
    path("courses/delete/<pk>",DeleteCourse.as_view(),name="deletecourse"),
    path("courses/update/<pk>",UpdateCourse.as_view(),name="updatecourse"),
    path('students/',StudentsView.as_view(),name="students"),
    path("students/add/",AddStudentView.as_view(),
    name="addstudent"),
    path("students/<pk>/",ShowStudentView.as_view(),name="student"),
    path("students/delete/<pk>/",DeleteStudentView.as_view(),name="deletestudent"),
    path("students/update/<pk>",UpdateStudentView.as_view(),name="updatestudent"),
    path("teachers",TeachersView.as_view(),name="teachers"),
    path("teachers/add",AddTeacherView().as_view(),name="addteacher"),
    path("teachers/<pk>",ShowTeacherView.as_view(),name="teacher"),
    path("teachers/update/<pk>",UpdateTeacherView.as_view(),
    name="updateteacher"),
    path("teachers/delete/<pk>",DeleteTeacherView.as_view(),
    name="deleteteachers"),
    path("courses/<pk>/students/update",UpdateCourseStudents.as_view(),name="updatestudents"),
    path("courses/<pk>/teachers/update",UpdateCourseTeachers.as_view(),name="updateteachers"),    
]
