"""tutor URL Configuration

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
from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landingpage,name="landingpage"),



# ======================= >  TUTOR SECTION  <===========================#
    path('tutor_login',views.tutor_login,name="tutor_login"),
    path('TutorSignUp',views.TutorSignUp,name="TutorSignUp"),
    path('signup_ajax',views.signup_ajax,name="signup_ajax"),
    path('email_authentication',views.email_authentication,name="email_authentication"),
    path('tutor_createprofile/<int:id>',views.tutor_createprofile,name="tutor_createprofile"),

    path('tutor_profilesave/<int:id>',views.tutor_profilesave,name="tutor_profilesave"),

    path('tutor_dashboard',views.tutor_dashboard,name='tutor_dashboard'),



# ======================= >  STUDENT SECTION  <===========================#

    path('student_login',views.student_login,name="student_login"),
    path('student_signup',views.student_signup,name="student_signup"),
    path('student_signup_ajax',views.student_signup_ajax,name="student_signup_ajax"),
    path('student_email_authentication',views.student_email_authentication,name="student_email_authentication"),
    path('student_createprofile/<int:id>',views.student_createprofile,name="student_createprofile"),
    path('student_profilesave/<int:id>',views.student_profilesave,name="student_profilesave"),

    path('student_dashboard',views.student_dashboard,name='student_dashboard'),






]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)