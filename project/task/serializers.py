from rest_framework.serializers import ModelSerializer;
from task.models import Course,Teacher,Student;
class CousersSerializer(ModelSerializer):
        class Meta:
            model=Course;
            fields='__all__';
class CourseSerializer(ModelSerializer):
       class Meta:
           model=Course;
           fields=['name','start','end','students','teachers'];
# class CreateCourseSeializer(ModelSerializer):
#     class Meta:
#         model=Course;
#         fields=['name',"start","end","students","teachers"]
class EditCourseStudentSerializer(ModelSerializer):
    class Meta:
        model=Course;
        fields=['students'];
class EditCourseTeacherSerializer(ModelSerializer):
    class Meta:
        model=Course;
        fields=['teachers'];
class StudentsSerializer(ModelSerializer):
    class Meta:
        model=Student;
        fields='__all__';
class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student;
        fields=['name',];
class TeachersSerializer(ModelSerializer):
      class Meta:
          model=Teacher;
          fields='__all__';
class TeacherSerializer(ModelSerializer):
      class Meta:
          model=Teacher;
          fields=['name','age'];

