from django.shortcuts import render,redirect
from django.http import JsonResponse
import random
from django.contrib.auth import authenticate, login
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .models import *

def landingpage(request):
    return render(request,'landing_page.html')










# ======================= >  TUTOR SECTION  <===========================#

def tutor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Tutor_Registration.objects.filter( username=username, password=password, status = '1').exists():
            tutor = Tutor_Registration.objects.get(username = request.POST['username'],password = request.POST['password'])
            request.session['Tutor_id'] = tutor.id
            return redirect('tutor_dashboard')
        else:
            return render(request,'tutor/tutor_login.html',{'error':'INVALID CREDENTIALS'})
    else:

        return render(request,'tutor/tutor_login.html')

def TutorSignUp(request):
    return render(request,'tutor/tutor_signup.html')


def signup_ajax(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otpnumber = random.randint(1000, 9999)


        sender_email = 'anwarsadik.disk1@gmail.com'
        receiver_email = email
        password = 'ogxemcnlxvvbflhx'
        subject = 'TUTOR SIGNUP'
        message = 'Hi '
        message = 'TUTOR MARKETPLACE SIGNUP OTP.\n\n'
        message += 'OTP: ' + str(otpnumber)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print('Email sent successfully!')
        except Exception as e:
            print(f'An error occurred while sending the email: {str(e)}')
        finally:
            server.quit()


        response = {'otpnumber': otpnumber}
        return JsonResponse(response)



def email_authentication(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')

        t = Tutor_Registration()
        t.fullname = name
        t.email = email
        t.mobile = phone
        t.city = city
        t.save()
        print(t.id)
        response_data = {'id': t.id}
        return JsonResponse(response_data)

    response_data = {'message': 'Invalid AJAX request'}
    return JsonResponse(response_data, status=400)
    

def tutor_createprofile(request,id):
    tutor = Tutor_Registration.objects.filter(id=id)
    grades = Grades.objects.all()
    subs = Subjects.objects.all()
    return render(request,'Tutor/tutor_create_profile.html',{'tutor':tutor,'grades':grades,'subs':subs})


def tutor_profilesave(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        gender = request.POST['gender']
        dob = request.POST['dob']
        adress = request.POST['adress']
        state = request.POST['state']
        contry = request.POST['contry']
        username = request.POST['username']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_pic', False)

        qualification = request.POST['qualification']
        qualification_cirt = request.FILES.get('qualification_pic', False)


        grade_1 = request.POST.getlist('grades[]')
        subject_1 = request.POST.getlist('subjects[]')


        t = Tutor_Registration.objects.get(id=id)
        t.name = name
        t.email = email
        t.phone = phone
        t.city = city
        t.gender = gender
        t.dateofbirth = dob
        t.address = adress
        t.state = state
        t.country = contry
        t.username = username
        t.password = password
        t.photo = profile_picture
        t.qualification = qualification
        t.qualification_cirt = qualification_cirt
        t.save()

        tg = Tutor_Registration.objects.get(id=t.id)
        for i in grade_1:
            Tutor_Grades.objects.create(tutor=tg,grade=i)
        for s in subject_1:
            Tutor_Subjects.objects.create(tutor=tg,subject=s)
        return redirect('tutor_login')



def tutor_navbar(request):
    if 'Tutor_id' in request.session:
        if request.session.has_key('Tutor_id'):
            Tutor_id = request.session['Tutor_id']
        else:
            return redirect('/')

        tutor = Tutor_Registration.objects.filter(id=Tutor_id)

        return render(request,'tutor/tutor_navbar.html',{'tutor':tutor})
    else:
        return redirect('tutor_login')

def tutor_dashboard(request):
    if 'Tutor_id' in request.session:
        if request.session.has_key('Tutor_id'):
            Tutor_id = request.session['Tutor_id']
        else:
            return redirect('/')
        tutor = Tutor_Registration.objects.filter(id=Tutor_id)
        return render(request,'tutor/tutor_dashboard.html',{'tutor':tutor})
    else:
        return redirect('tutor_login')

















































# ======================= >  STUDENT SECTION  <===========================#


def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if Student_Registration.objects.filter( username=username, password=password).exists():
            student = Student_Registration.objects.get(username = request.POST['username'],password = request.POST['password'])
            request.session['Std_id'] = student.id
            return redirect('student_dashboard')
        else:
            return render(request,'Student/student_login.html',{'error':'INVALID CREDENTIALS'})
    else:
        return render(request,'Student/student_login.html')


def student_signup(request):

    grades = Grades.objects.all()
    return render(request,'Student/student_signup.html',{'grades':grades})



def student_signup_ajax(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otpnumber = random.randint(1000, 9999)


        sender_email = 'anwarsadik.disk1@gmail.com'
        receiver_email = email
        password = 'ogxemcnlxvvbflhx'
        subject = 'Student SIGNUP'
        message = 'Hi '
        message = 'TUTOR MARKETPLACE STUDENT SIGNUP OTP.\n\n'
        message += 'OTP: ' + str(otpnumber)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print('Email sent successfully!')
        except Exception as e:
            print(f'An error occurred while sending the email: {str(e)}')
        finally:
            server.quit()


        response = {'otpnumber': otpnumber}
        return JsonResponse(response)
    



def student_email_authentication(request):
    if request.method == 'POST':
        studentName = request.POST.get('studentName')
        parentName = request.POST.get('parentName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        gradeis = request.POST.get('gradeis')


        s = Student_Registration()
        s.fullname = studentName
        s.parentfullname = parentName
        s.email = email
        s.mobile = phone
        s.city = city
        s.grade = gradeis
        s.save()
        print(s.id)
        response_data = {'id': s.id}
        return JsonResponse(response_data)

    response_data = {'message': 'Invalid AJAX request'}
    return JsonResponse(response_data, status=400)
    


def student_createprofile(request,id):
    student = Student_Registration.objects.filter(id=id)
    grades = Grades.objects.all()
    subs = Subjects.objects.all()
    return render(request,'Student/student_create_profile.html',{'student':student,'grades':grades,'subs':subs})



def student_profilesave(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        gender = request.POST['gender']
        dob = request.POST['dob']
        adress = request.POST['adress']
        state = request.POST['state']
        contry = request.POST['contry']
        username = request.POST['username']
        password = request.POST['password']
        profile_picture = request.FILES.get('profile_pic', False)

        p_name = request.POST['pname']
        p_email = request.POST['pemail']
        p_phone = request.POST['pphone']
        p_city = request.POST['pcity']

        school = request.POST['institution']
        grade = request.POST['grade']



        s = Student_Registration.objects.get(id=id)
        s.name = name
        s.email = email
        s.phone = phone
        s.city = city
        s.gender = gender
        s.dateofbirth = dob
        s.address = adress
        s.state = state
        s.country = contry
        s.username = username
        s.password = password
        s.photo = profile_picture
        s.p_name = p_name
        s.p_email = p_email
        s.p_phone = p_phone
        s.p_city = p_city
        s.institution = school
        s.grade = grade
        s.save()

        return redirect('student_login')




def student_navbar(request):
    if 'Std_id' in request.session:
        if request.session.has_key('Std_id'):
            Std_id = request.session['Std_id']
        else:
            return redirect('/')
        std = Student_Registration.objects.filter(id=Std_id)
        return render(request,'Student/student_navbar.html',{'std':std})
    else:
        return redirect('tutor_login')

def student_dashboard(request):
    if 'Std_id' in request.session:
        if request.session.has_key('Std_id'):
            Std_id = request.session['Std_id']
        else:
            return redirect('/')

        std = Student_Registration.objects.filter(id=Std_id)
        return render(request,'Student/student_dashboard.html',{'std':std})
    else:
        return redirect('tutor_login')












