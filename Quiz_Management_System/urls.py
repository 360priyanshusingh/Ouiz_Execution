"""Quiz_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import delete as delete
from django.conf import settings
from django.contrib import admin
from django.urls import path

from Quiz_Management.views import *
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name="home"),
    path('loginAdmin',loginAdmin,name="login"),
    path('loginteacher',loginteacher,name="loginteacher"),
    path('adminHome',adminHome,name="adminHome"),
    path('hometeacher',hometeacher,name="hometeacher"),
    path('veiwTeacher',veiwTeacher,name="veiwTeacher"),
    path('addcourses',addcourses,name="addcourses"),
    path('addcourses2',addcourses2,name="addcourses2"),
    path('veiwcourses',veiwcourses,name="veiwcourses"),
    path('veiwcourses2',veiwcourses2,name="veiwcourses2"),
    path('addbranch',addbranch,name="addbranch"),
    path('viewbranch',viewbranch,name="veiwbranch"),
    path('deletecours/<pid>',deletecours,name="deletecours"),
    path('deletebranch/<pid>',deletebranch,name="deletebranch"),
    path('deleteTeacher/<pid>',deleteTeacher,name="deleteTeacher"),
    path('updatedcourses/<pid>',updatedcourses,name="updatedcourses"),
    path('updatebranch/<pid>',updatebranch,name="updatebranch"),
    path('teacherregister',teacherregister,name="teacherregister"),
    path('veiwPendingTeacher',veiwPendingTeacher,name="veiwPendingTeacher"),
    path('updateTeacherstatus/<pid>',updateTeacherstatus,name="updateTeacherstatus"),
    path('addquestion',addquestion,name="addquestion"),
    path('addquestion2',addquestion2,name="addquestion2"),
    path('veiwquestion/<pid>',veiwquestion,name="veiwquestion"),
    path('veiwquestion2/<pid>',veiwquestion2,name="veiwquestion2"),
    path('updateQuestion/<pid>',updateQuestion,name="updateQuestion"),
    path('updateQuestion2/<pid>',updateQuestion2,name="updateQuestion2"),
    path('checkpending',checkpending,name="checkpending"),
    path('deleteQuestion/<pid>',deleteQuestion,name="deleteQuestion"),
    path('deleteQuestion2/<pid>',deleteQuestion2,name="deleteQuestion2"),
    path('studentregister',studentregister,name="studentregister"),
    path('loginstudent/',loginstudent,name="loginstudent"),
    path('homestudent',homestudent,name="homestudent"),
    path('logout',Logout,name="logout"),
    path('veiwStudent',veiwStudent,name="veiwStudent"),
    path('studentveiwexam',studentveiwexam,name="studentveiwexam"),
    path('veiwquiz/<pid>',quiz,name="veiwquiz"),
    path('veiwresult',veiwresult,name="veiwresult"),
    path('veiwProfeil',veiwProfeil,name="veiwProfeil"),
    path('veiwProfeilteacher',veiwProfeilteacher,name="veiwProfeilteacher"),
    path('veiwreportcard/',veiwreportcard,name="veiwreportcard"),
    path('updatedProfeil',updatedProfeil,name="updatedProfeil"),
    path('updatedProfeilTeacher',updatedProfeilTeacher,name="updatedProfeilTeacher"),
    path('deleteStudent/<pid>',deleteStudent,name="deleteStudent"),
    path('assigncourses',assigncourses,name="assigncourses"),
    path('veiwreportcardAdmin/<pid>',veiwreportcardAdmin,name="veiwreportcardAdmin"),
    path('viewStudent2',viewStudent2,name="viewStudent2"),
    path('deleteStudent2/<pid>',deleteStudent2,name="deleteStudent2"),
    path('veiwreportcardAdmin2/<pid>',veiwreportcardAdmin2,name="veiwreportcardAdmin2"),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

