import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template, render_to_string
from django.utils.html import strip_tags

from Quiz_Management.models import *
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Create your views here.
from twilio.rest import Client

def messageq(msg,data):
    contact = '+917974037363'
    mysms="Hey " + data.user.first_name + " " +data.user.last_name + '! Your Quiz marks is '+ str(msg) + " check email for more  detail."
    account_sid = 'AC43522dbb2e3eca42423f6a5962905af3'
    auth_token = '89a79a41c4b474762bd1ccfda94c77fd'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        messaging_service_sid='MGee65cb762d9f5b1ac0b2e808c30fdc2b',
        body=mysms,
        to=contact
    )

    print(message.sid)

def home(request):
    if request.user.is_authenticated:
       user=request.user
       try:
           user=Student.objects.get(user=user)
           return redirect('homestudent')
       except:
           try:
               user = Teacher.objects.get(user=user)
               return redirect('hometeacher')
           except:
               return redirect('adminHome')


    return render(request, 'home.html')


def sendemail(user, score):
    sender = 'Quiz Execution System'
    toemail = str(user.email)
    toname = user.username
    fromemail = "upscpriyanshu06@gmail.com"
    subject = "Report Card"
    data = Student.objects.get(user=user)
    q = Quiz.objects.filter(student=data)
    Dict={'data':data,'q':q}
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = subject
    html_content = render_to_string('vreportcard.html', Dict)
    # html_content = strip_tags(html_message)
    sender = {"name": sender, "email": fromemail}
    to = [{"email": toemail, "name": toname}]
    headers = {"Some-Custom-Name": "unique-id-1234"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
def sendemailF(data, score):
    sender = 'Quiz Execution System'
    toemail = str(data.father_email)
    toname = data.user.username
    fromemail = "upscpriyanshu06@gmail.com"
    subject = "Report Card"
    data = Student.objects.get(user=data.user)
    q = Quiz.objects.filter(student=data)
    Dict={'data':data,'q':q}
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = subject
    html_content = render_to_string('vreportcard.html', Dict)
    # html_content = strip_tags(html_message)
    sender = {"name": sender, "email": fromemail}
    to = [{"email": toemail, "name": toname}]
    headers = {"Some-Custom-Name": "unique-id-1234"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, headers=headers, html_content=html_content, sender=sender, subject=subject)
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)



def loginAdmin(request):
    if request.method == "POST":
        username = request.POST.get("Email")
        password = request.POST.get("Password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect("adminHome")
        else:
            messages.success(request, "Invalid user")

    return render(request, 'login.html', locals())


def adminHome(request):
    t = Teacher.objects.all()
    t = t.count()
    pd = Teacher.objects.filter(status="pending")
    pd = pd.count();
    tc = Courses.objects.all();
    tc = tc.count();
    ts=Student.objects.all();
    ts=ts.count()
    return render(request, "adminHome.html", locals())


def addcourses(request):
    e = Branch.objects.all()
    if request.method == "POST":
        f = request.POST['cname']
        t = request.POST['time']
        b = request.POST['bid']
        branch = Branch.objects.get(id=b)
        Courses.objects.create(courses_name=f, branch_name=branch,time=t)
        messages.success(request, 'Created Successfully')
        return redirect('veiwcourses')
    return render(request, 'addcourses.html', locals())

def addcourses2(request):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if not t:
        return redirect("checkpending")
    data = Teacher.objects.get(user=request.user)
    e = Branch.objects.all()
    if request.method == "POST":
        f = request.POST['cname']
        b = request.POST['bid']
        t=request.POST['time']
        branch = Branch.objects.get(id=b)
        Courses.objects.create(courses_name=f, branch_name=branch,time=t)
        messages.success(request, 'Created Successfully')
        return redirect('veiwcourses2')
    return render(request, 'addcourses2.html', locals())


def veiwcourses(request):
    e = Courses.objects.all()
    return render(request, 'veiwcourses.html', locals())

def veiwcourses2(request):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if not t:
        return redirect("checkpending")
    data = Teacher.objects.get(user=request.user)
    e = Courses.objects.all()
    return render(request, 'veiwcourses2.html', locals())


def addbranch(request):
    if request.method == "POST":
        f = request.POST['bname']
        Branch.objects.create(branch_name=f)
        messages.success(request, 'added Successfully')
        return redirect('veiwbranch')
    return render(request, 'addbranch.html', locals())


def viewbranch(request):
    e = Branch.objects.all()
    return render(request, 'veiwbranch.html', locals())


def deletecours(request, pid):
    d = Courses.objects.get(id=pid)
    d.delete()
    return redirect('veiwcourses')


def deletebranch(request, pid):
    d = Branch.objects.get(id=pid)
    d.delete()
    return redirect('veiwbranch')


def updatedcourses(request, pid):
    data = Courses.objects.get(id=pid)
    e = Branch.objects.all()
    if request.method == "POST":
        f = request.POST['cname']
        t = request.POST['time']
        b = request.POST['bid']
        branch = Branch.objects.get(id=b)
        Courses.objects.filter(id=pid).update(courses_name=f, time=t, branch_name=branch)
        messages.success(request, 'Updated Successfully')
        return redirect('veiwcourses')
    return render(request, 'updatedcourses.html', locals())


def updatebranch(request, pid):
    data = Branch.objects.get(id=pid)
    if request.method == "POST":
        f = request.POST['bname']
        Branch.objects.filter(id=pid).update(branch_name=f)
        messages.success(request, 'Updated Successfully')
        return redirect('veiwbranch')
    return render(request, "updatebranch.html", locals())


def teacherregister(request):
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        p = request.POST['pwd']
        mb = request.POST['mb']
        add = request.POST['add']
        img = request.FILES['img']
        user = User.objects.create_user(first_name=f, last_name=l, email=e, password=p, username=e)
        Teacher.objects.create(user=user, mobile_number=mb, address=add, image=img, status="pending");
        messages.success(request, 'Created Successfully')
    return render(request, "teacherregister.html")


def loginteacher(request):
    if request.method == "POST":
        username = request.POST.get("Email")
        password = request.POST.get("Password")
        user = authenticate(username=username, password=password)
        t = Teacher.objects.filter(user=user, status="approved")

        if user:
            login(request, user)
            messages.success(request, "Login Successfull")
            print(t)
            if t:
                return redirect("hometeacher")
            else:
                return redirect("checkpending")
        else:
            messages.success(request, "Invalid user")

    return render(request, 'loginteacher.html', locals())


def hometeacher(request):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if not t:
        return redirect("checkpending")
    data = Teacher.objects.get(user=request.user)
    t = Teacher.objects.all()
    t = t.count()
    pd = Teacher.objects.filter(status="pending")
    pd = pd.count();
    tc = Courses.objects.all();
    tc = tc.count();
    ts=Student.objects.all()
    ts=ts.count();

    return render(request, 'hometeacher.html',locals())


def veiwTeacher(request):
    e = Teacher.objects.filter(status="approved")
    return render(request, 'veiwTeacher.html', locals())


def veiwPendingTeacher(request):
    e = Teacher.objects.filter(status="pending")
    return render(request, 'veiwTeacher.html', locals())


def updateTeacherstatus(request, pid):
    data = Teacher.objects.get(id=pid)
    if request.method == "POST":
        f = request.POST['status']
        s = request.POST['salary']
        Teacher.objects.filter(id=pid).update(status=f, salary=s)
        messages.success(request, 'Updated Successfully')
        return redirect('veiwTeacher')
    return render(request, "updateTeacherstatus.html", locals())


def deleteTeacher(request, pid):
    d = Teacher.objects.get(id=pid)
    u=d.user
    u.delete()
    return redirect('veiwTeacher')


def addquestion(request):
    e = Courses.objects.all()
    if request.method == "POST":
        q = request.POST['qname']
        b = request.POST['bid']
        m = request.POST['m']
        o1 = request.POST['o1']
        o2 = request.POST['o2']
        o3 = request.POST['o3']
        o4 = request.POST['o4']
        ans = request.POST['ans']
        courses = Courses.objects.get(id=b)
        Questions.objects.create(courses=courses, question_name=q, marks=m, option1=o1, option2=o2, option3=o3,option4=o4, ans=ans)
        question = Questions.objects.filter(courses=courses)
        c = question.count()
        marks=0
        for i in question:
            marks=marks+int(i.marks)
        Courses.objects.filter(id=b).update(total_question=c,total_marks=marks)
        messages.success(request, 'Created Successfully')
        return redirect('veiwcourses')
    return render(request, 'addquestion.html', locals())

def addquestion2(request):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if not t:
        return redirect("checkpending")
    data = Teacher.objects.get(user=request.user)
    e = Courses.objects.all()
    if request.method == "POST":
        q = request.POST['qname']
        b = request.POST['bid']
        m = request.POST['m']
        o1 = request.POST['o1']
        o2 = request.POST['o2']
        o3 = request.POST['o3']
        o4 = request.POST['o4']
        ans = request.POST['ans']
        courses = Courses.objects.get(id=b)
        Questions.objects.create(courses=courses, question_name=q, marks=m, option1=o1, option2=o2, option3=o3,option4=o4, ans=ans)
        question = Questions.objects.filter(courses=courses)
        c = question.count()
        marks=0
        for i in question:
            marks=marks+int(i.marks)
        Courses.objects.filter(id=b).update(total_question=c,total_marks=marks)
        messages.success(request, 'Created Successfully')
        return redirect('veiwcourses2')
    return render(request, 'addquestion2.html', locals())


def veiwquestion(request, pid):
    c = Courses.objects.get(id=pid)
    e = Questions.objects.filter(courses=c)
    return render(request, "veiwquestion.html", locals())
def veiwquestion2(request, pid):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if not t:
        return redirect("checkpending")
    data = Teacher.objects.get(user=request.user)
    c = Courses.objects.get(id=pid)
    e = Questions.objects.filter(courses=c)
    return render(request, "veiwquestion2.html", locals())


def updateQuestion(request, pid):
    data = Questions.objects.get(id=pid)
    e = Courses.objects.all()
    if request.method == "POST":
        q = request.POST['qname']
        b = request.POST['bid']
        m = request.POST['m']
        o1 = request.POST['o1']
        o2 = request.POST['o2']
        o3 = request.POST['o3']
        o4 = request.POST['o4']
        ans = request.POST['ans']
        c = Courses.objects.get(id=b)
        Questions.objects.filter(id=pid).update(courses=c, question_name=q, marks=m, option1=o1, option2=o2, option3=o3,
                                                option4=o4, ans=ans)
        messages.success(request, 'Updated Successfully')
        return redirect('veiwquestion',b)
    return render(request, 'updateQuestion.html', locals())
def updateQuestion2(request, pid):
    data = Questions.objects.get(id=pid)
    e = Courses.objects.all()
    if request.method == "POST":
        q = request.POST['qname']
        b = request.POST['bid']
        m = request.POST['m']
        o1 = request.POST['o1']
        o2 = request.POST['o2']
        o3 = request.POST['o3']
        o4 = request.POST['o4']
        ans = request.POST['ans']
        c = Courses.objects.get(id=b)
        Questions.objects.filter(id=pid).update(courses=c, question_name=q, marks=m, option1=o1, option2=o2, option3=o3,
                                                option4=o4, ans=ans)
        messages.success(request, 'Updated Successfully')
        return redirect('veiwquestion2',b)
    return render(request, 'updateQuestion2.html', locals())


def checkpending(request):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if t:
        return redirect("hometeacher")
    return render(request, 'checkpending.html')

def deleteQuestion(request, pid):
    d = Questions.objects.get(id=pid)
    cid = d.courses.id
    d.delete()
    return redirect('veiwquestion',cid)

def deleteQuestion2(request, pid):
    d = Questions.objects.get(id=pid)
    cid = d.courses.id
    d.delete()
    return redirect('veiwquestion2',cid)

def Logout(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect("/")

def loginstudent(request):
    if request.method == "POST":
        username = request.POST.get("Email")
        password = request.POST.get("Password")
        user = authenticate(username=username, password=password)
        t = Student.objects.filter(user=user)

        if user:
            login(request, user)
            messages.success(request, "Login Successfull")
            return redirect("homestudent")
        else:
            messages.success(request, "Invalid user")

    return render(request, 'loginstudent.html', locals())

def studentregister(request):
    e=Branch.objects.all()
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        fn = request.POST['fn']
        fe = request.POST['fe']
        e = request.POST['email']
        p = request.POST['pwd']
        mb = request.POST['mb']
        b = request.POST['bid']
        b= Branch.objects.get(id=b)
        add = request.POST['add']
        img = request.FILES['img']
        user = User.objects.create_user(first_name=f, last_name=l, email=e, password=p, username=e)
        Student.objects.create(user=user, mobile_number=mb, address=add, image=img,branch_name=b,father_name=fn,father_email=fe);
        messages.success(request, 'Created Successfully')
        return redirect('loginstudent')
    return render(request, "studentregister.html",locals())

def homestudent(request):
    data = Student.objects.get(user=request.user)
    t = Teacher.objects.all()
    t = t.count()
    pd = Teacher.objects.filter(status="pending")
    pd = pd.count();
    tc = Courses.objects.all();
    tc = tc.count();
    ts = Student.objects.all()
    ts = ts.count();
    return render(request, 'homestudent.html',locals())

def veiwStudent(request):
    e = Student.objects.all()
    return render(request, 'veiwStudent.html', locals())

def viewStudent2(request):
    t = Teacher.objects.filter(user=request.user, status="approved")
    if not t:
        return redirect("checkpending")
    data = Teacher.objects.get(user=request.user)
    e = Student.objects.all()
    return render(request, 'viewStudent2.html', locals())

def studentveiwexam(request):
    data=Student.objects.get(user=request.user)
    e=Courses.objects.filter(branch_name=data.branch_name)
    return render(request,'studentveiwexam.html',locals())

def quiz(request,pid):
    q = Courses.objects.get(id=pid)
    t=(q.time).split(':')
    hr=int(t[0])
    mn=int(t[1])
    se=int(t[2])
    countDownDate = datetime.datetime.now() + datetime.timedelta(hours=hr) + datetime.timedelta(minutes=mn)
    for_js = countDownDate.timestamp() * 1000
    print(for_js)
    e = Questions.objects.filter(courses=q)
    quiz = Quiz.objects.filter(courses=q, student__user=request.user)
    if quiz:
        messages.success(request, "Already Given Quiz.")
        return redirect('studentveiwexam')
    if request.method == "POST":
        answer = []
        question = []
        marks = 0
        for i in e:
            option = request.POST.get('option-'+str(i.id))
            if i.ans == option:
                marks += int(i.marks)
            answer.append(option)
            question.append(i.question_name)
        data = Student.objects.get(user=request.user)
        quiz = Quiz.objects.create(student=data, courses=q, question=question, answer=answer, marks=marks)
        course=Courses.objects.filter(branch_name=data.branch_name)
        q=Quiz.objects.filter(student=data)
        if course.count() == q.count():
            quiz.marks=0;
            course.marks=0;
            for i in q:
                quiz.marks+= int(i.marks)
            for i in course:
                course.marks += int(i.total_marks)
            quiz.marks=(quiz.marks *100) /  course.marks
            sendemail(request.user, quiz.marks)
            sendemailF(data, quiz.marks)
            messageq(quiz.marks,data)
        return redirect('studentveiwexam')
    return render(request, 'veiwquiz.html', locals())

def veiwresult(request):
    data=Student.objects.get(user=request.user)
    e=Quiz.objects.filter(student=data);
    return render(request, 'veiwresult.html', locals())

def veiwProfeil(request):
    data = Student.objects.get(user=request.user)
    return render(request,'veiwProfeil.html',locals())
def veiwProfeilteacher(request):
    data = Teacher.objects.get(user=request.user)
    return render(request,'veiwProfeilteacher.html',locals())

def veiwreportcard(request):
    data = Student.objects.get(user=request.user)
    q = Quiz.objects.filter(student=data)
    return render(request, "veiwreportcard.html", locals())

def updatedProfeil(request):
    data = Student.objects.get(user=request.user)
    e=Branch.objects.all()
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        fn = request.POST['fn']
        fe = request.POST['fe']
        mb = request.POST['mb']
        b = request.POST['bid']
        b = Branch.objects.get(id=b)
        add = request.POST['add']
        try:
            img = request.FILES['img']
            data.image = img
            data.save()
        except:
            pass

        user = User.objects.filter(id=data.user.id).update(first_name=f, last_name=l)
        data.mobile_number=mb
        data.address=add
        data.branch_name=b
        data.father_name=fn;
        data.father_email=fe;
        data.save()
        messages.success(request, 'Updated Successfully')
        return redirect('veiwProfeil')
    return render(request,'updatedProfeil.html',locals())

def updatedProfeilTeacher(request):
    data = Teacher.objects.get(user=request.user)
    e=Branch.objects.all()
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        mb = request.POST['mb']

        add = request.POST['add']
        try:
            img = request.FILES['img']
            data.image = img
            data.save()
        except:
            pass

        user = User.objects.filter(id=data.user.id).update(first_name=f, last_name=l)
        data.mobile_number=mb
        data.address=add
        data.save()
        messages.success(request, 'Updated Successfully')
        return redirect('veiwProfeilteacher')
    return render(request,'updatedProfeilTeacher.html',locals())

def deleteStudent(request, pid):
    d = Student.objects.get(id=pid)
    u1=d.user
    d.delete()
    return redirect('veiwStudent')
def deleteStudent2(request, pid):
    d = Student.objects.get(id=pid)
    u1=d.user
    d.delete()
    return redirect('viewStudent2')
def veiwreportcardAdmin(request,pid):
    data = Student.objects.get(id=pid)
    q = Quiz.objects.filter(student=data)
    return render(request, "veiwreportcardAdmin.html", locals())

def veiwreportcardAdmin2(request,pid):

    data2 = Student.objects.get(id=pid)
    q = Quiz.objects.filter(student=data2)
    return render(request, "veiwreportcardAdmin2.html", locals())

def assigncourses(request):
    t =Teacher.objects.all()
    e = Courses.objects.all()
    if request.method == "POST":
        t= request.POST['tname']
        c= request.POST['cname']
        teacher=Teacher.objects.get(id=t)
        course=Courses.objects.get(id=c)
        Assigncourses.objects.create(teacher=teacher,courses=course)
        return redirect("veiwStudent")
    return render(request,"assigncourses.html",locals())

