import email
from email import message
import imp
#from msilib.schema import File
from django.conf import UserSettingsHolder, settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from logsys import settings
from django.core.mail import send_mail

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Contact

# Create your views here.
def confirmation(request):
    #create a bite stream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf,pagesize=letter,bottomup=0)
    #create text
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    #Lines of text
    lines = [
          "Your Appointment has been booked!",
          "Our quality speaks our price",
          "Enjoy our Service!"
    ]
    # user = User.objects.all()
    # lines = []
    # for user in user:
    #     lines.append()
    #     lines.append(user.username)
    #     lines.append(user.email)
    #     # lines.append(user.)
    #     # lines.append(user.)
    #     # lines.append(user.)

    #loop
    for line in lines:
        textob.textLine(line)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename="Ignite.pdf")





def home(request):
    return render(request, "authentication/index.html")


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstName = request.POST["firstName"]
        lastName = request.POST["lastName"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmPassword = request.POST["confirmPassword"]

        #########################validations#####################################

        if User.objects.filter(username=username):
            messages.error(
                request, "UserName already Exists!Please try some other Username!")
            return redirect('register')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists...Please login")
            return redirect('login_user')

        if len(username) > 20:
            messages.error(
                request, "Length of the username must be 0-20 characters only!")
            return redirect(request, 'register')

        if password != confirmPassword:
            messages.error(request, "Passwords not Matching!")
            return redirect(request, 'register')

        if len(password) < 8:
            messages.error(
                request, "Password too short!\nMinimum 8 characters required")
            return redirect('register')

        if len(password) > 20:
            messages.error(
                request, "Password too Long!\nMaximum 20 characters only")
            return redirect('register')

        if not password.isalnum():
            messages.error(
                request, "Password Must contain numbers and letters")
            return redirect('register')

        if not username.isalnum():
            messages.error(
                request, "UserName Must contain numbers and letters")
            return redirect('register')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstName
        myuser.last_name = lastName

        myuser.save()

        messages.success(request, "Account Created Successfully!")

        ############################## WELCOME EMAIL ########################################
        subject = "Account Confirmation Email--Ignite Car Services"
        message = "Hello",myuser.first_name,"!!!\nWohoo! Your Account for Ignite Car Services has been created Successfully! Now you are just one step away from hassle free appointment booking. Click on the link in the email for confirming your Email Address thereby activationg your account.\n\nHappy Servicing!!"
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        send_mail(subject,message,from_email,to_list,fail_silently=True)




        return redirect('login_user')

    return render(request, "authentication/register.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstName = user.first_name
            return render(request, "authentication/mainpg.html", {firstName: 'firstName'})
        else:
            messages.error(request, "")
            return redirect('login_user')

    return render(request, "authentication/login.html")


def signout(request):
    logout(request)
    messages.success(request, "Signed Out Successfully!")
    return redirect(login_user)


def mainpg(request):
    return render(request,'authentication/mainpg.html')
    # return HttpResponse("<h1>Welcome to Home Page!</h1>")

def about(request):
    return render(request,'authentication/about.html')
    # return HttpResponse("<h1>Welcome to About Page!</h1>")

def booking(request):
    return render(request,'authentication/book.html')
    # return HttpResponse("<h1>Welcome to booking Page!</h1>")

# def contact(request):
#     # return HttpResponse("<h1>Welcome to Contact Page!</h1>")
#     return render(request,"authentication/contact.html")

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname','')
        lastname = request.POST.get('lastname','')
        message = request.POST.get('message','')
        email = request.POST.get('email','')
        contact = Contact(firstname=firstname,lastname=lastname,email=email,message=message)
        contact.save()
    return render(request,"authentication/contact.html")

def error(request):
    return render(request,"authentication/error.html")

def feedback(request):
    return render(request,'authentication/feedback.html')