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
from .models import Appoint, Contact

# Create your views here.
def confirmation(request):
    #create a bite stream buffer
    buf = io.BytesIO()
    #create a canvas
    c = canvas.Canvas(buf,pagesize=((1200,1600)),bottomup=0)
    #create text
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",12)
    #Lines of text
    lines = [
          "Our terms and conditions do not affect your statutory rights as a consumer.",

"We are a professional limousine company and not a Taxi service.",
"These terms have been designed to safeguard our business ethics and to help us maintain an efficient and professional service for our clients.",

"Some of our services like Proms, Weddings, or special events may require our clients to fill out a bonding contract. Proof of signature and credit card deposit are required as well.",

"These terms apply whether the contract was made in writing or verbally. Please note that all bookings must be made during an office visit or over the phone. You may only place reservations and communicate with us in English. All contracts between us will be finalized in English.",

"By making a booking with Ignite Car Service and paying the deposit amount(s); the clients acknowledge and expressly agree to the following policies, terms, and conditions and further expressly authorize Ignite Car Service to charge your credit card in full or part amounts relating to your booking including but not limited to charging your credit card in full for the reservation should you be considered a no-show. Service is deemed rendered, whether you enter the vehicle or not when the cancellation period is reached. All bookings must be secured with a credit card on file.",

"We reserve the right not to proceed where proceeding may place the vehicle and/or its patrons in an unsafe situation.",



"Payment:",
"All bookings are confirmed by the payment in advance of a non-refundable deposit. A deposit of 30%-50% of the total price and a signed contract are required to hold the vehicle. Deposits are non-refundable since many of our vehicles are booked a year in advance.The balance due is the amount outstanding net of any deposit paid. The balance is due for payment at the time and place of the first pick-up on the day of hire.We do not accept cheques, debit cards, credit cards, or foreign currency as final payment on the day of the hire unless agreed in advance. Settlement of the agreed price in advance by cheque or electronic transfer must allow adequate time for funds to be cleared before the date of travel. Credit card payments are subject to a 5% surcharge on the transaction amount."

"Cancellation of booking:",
"Canceling a reservation ",

"Should you cancel your booking then the deposit paid is non-refundable. Additionally where jobs are canceled with less than 14 (fourteen) days notice the full agreed price becomes due and owing. In the event of cancellation between 90 (ninety) days and 14 (fourteen) days of the date of travel 50% (fifty percent) of the total agreed price is due and owing. To cancel a reservation please call the office directlyPLEASE NOTE – if you fail to show up or/and do not notify us of a cancellation, we will charge you for the full price agreed plus petrol and driver costs. This will be charged to your credit card on fileCancellation By Us- We reserve the right to cancel the limousine hire contract between us if:the client doesn’t accept our terms and conditions and/or refuses to make a deposit payment and/or the deposit fail to clear,we do not operate in your area, or one or more of the limos you have booked no longer will be able to cover your reservation.If we do cancel your limo hire contract we will notify you by e-mail or phone and we will re-credit your account with any sum deducted from your credit card as soon as possible, but in any event within 30 days of your reservation. We will not be obliged to offer any additional compensation for the disappointment suffered.",



"Damages:",
"Damages, subsequent costs of repairs of such damage are to the limousines hired as used by you the customer, and/or your guests howsoever caused is your responsibility. Additionally, in the event that one of the parties is sick or soils in the limousine we will charge $300.00 to make the vehicle good. Where the booking was secured using a credit/charge card, you the customer here agree that the amount will be charged to that card for the damages as they have arisen. In the event that a credit/charge card was not used for securing the booking, we will invoice you directly should the additional payment be not made on the spot.",

"Additional Charges/Overtime:",
"Overtime charges begin immediately after the end of the grace period. Under this agreement, the overtime rate per hour or part thereof is $150.00. Payment of all overtime charges must be settled before the end of the hire. We do not accept cheques, debit cards, credit cards, or foreign currency as payment on the day of the hire. In the event that payment of overtime charges cannot be made on the day of the hire, the customer agrees that the amounts) will be charged to the credit/debit card with which the booking deposit was paid. Credit card payments) are subject to a 5% (five percent) surcharge on the transaction amount.",


"Vehicle supplied:",
"We will endeavor to provide the vehicle requested by you. In the unlikely event that we are unable to do so, we reserve the right to provide a substitute vehicle of a similar type and capacity. You will be informed of this.",
"Airport Drop Offs / Pick-ups:",
"Full flight details help us to give you punctual service. We will make reasonable attempts to monitor incoming flight times; however, we are unable to access reliable information until shortly before departure or scheduled arrival times. If your flight is delayed, either outbound or inbound you should make contact immediately with Ignite Car Service to notify us, so that we can adjust our schedules and rearrange drivers. We will endeavor to accommodate delayed flights times, but cannot be held liable should circumstances prevent us from being able to respond to changes.",

"In the event we are not reasonably notified of delays, we reserve the right to make additional charges for subsequent collection.,"

"Lost Property:",
"We are not responsible for articles lost, stolen, damaged, or left in our vehicles. You expressly waive any and all notice from Ignite Car Service regarding any lost, stolen, damaged, or belongings left in our vehicles, or the disposal of same. Please check for your belongings before leaving the vehicle.",

"Breakdown:",
"In the unlikely event of a breakdown or the car being rendered unserviceable (for example, in the event of collision) we will use our best endeavors to provide a backup vehicle or vehicles as quickly as possible. However, we cannot be held liable for any consequential loss incurred as a result of vehicle breakdown or similar unavailability",

"Ignite CAR SERVICE’S SMOKING, DRUG & ALCOHOL POLICY:",
"WE ARE A NON-SMOKING ORGANISATION, REGULAR ‘STOPS’ WILL BE MADE FOR SMOKERS UPON REQUEST.",

"As a responsible Operator of Limousine Services, we at Ignite Car Service are committed to ZERO tolerance on Drugs & Alcohol.",

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

        # if password != confirmPassword:
        #     messages.error(request, "Passwords not Matching!")
        #     return redirect(request, 'register')

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

def appoint(request):
    if request.method == "POST":
        appointname = request.POST.get("appointname",'')
        appointemail = request.POST.get("appointemail",'')
        appointdate = request.POST.get("appointdate",'')
        appointmentfor = request.POST.get("appointmentfor",'')
        appoint = Appoint(appointemail=appointemail,appointdate=appointdate,appointmentfor=appointmentfor)
        appoint.save()
    return render(request,"authentication/appoint.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            firstName = User.first_name
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
        city=request.POST.get('city','')
        contact = Contact(firstname=firstname,lastname=lastname,email=email,message=message,city=city)
        contact.save()
    return render(request,"authentication/contact.html")

def error(request):
    return render(request,"authentication/error.html")

def feedback(request):
    return render(request,'authentication/feedback.html')