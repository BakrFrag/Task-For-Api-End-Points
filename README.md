# Models 
   ## Student Model:
          name >> charfield
   ## Teacher Model:
           name >> charfield
           age >> floatfied
   ## Course Model:
           name >> charfield
           start >> datetimefield
           end   >> datetimefield
           teachers >> many to many field to model (Teacher)
           students >> many to many field to model (Students)
# relationships 
    Student Model ManyToMany Relationship with Course Model 
    Course Model ManyToMany Relationship with Teacher Model
```
hint we don't need to break each many to many relationship <br> into 2 relations of type one to many Django Does This For Us
```
# Api EndPoint
    we offer Api End Points For 
        1.authentication (signin/signout) with Json Web Token (JWT)
        2. end points for 
                ``` Courses ```
              1.create course 
              2.edit course info
              3.delete course 
              4.display course with it id 
              5.display all courses
              6.edit students associated to course
              7.edit teachers  associated to course
                ``` Student ```
              1.create student
              2.delete student
              3.update student info 
              4.display all students 
              5.display student as single object
                 ``` Teacher ```
              1.create teacher 
              2.edit teacher info 
              3.delete teacher
              4.display all teachers 
              5.display teacher as single object 
# all thees function tested using postman and worked well 
# operate thes project on your local machine 
    1.install libraries in requirements.txt 
    2.cd into project folder and run command 
          ``` pipenv install -r requirements ```
