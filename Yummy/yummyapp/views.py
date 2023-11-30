
from django.shortcuts import render, redirect
# from yummyapp.forms import EmpForm
from yummyapp.models import Member
from django.http import HttpResponse
import requests
from yummyapp.credentials import MpesaC2bCredential, MpesaAccessToken, LipanaMpesaPpassword
from requests.auth import HTTPBasicAuth


# Create your views here.
def register(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        member.save()
        return redirect('/hero')
    else:
        return render(request, 'register.html')

def login(request):
    return redirect('/hero')
    return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def chefs(request):
    return render(request, 'chefs.html')

def gallery(request):
    return render(request, 'gallery.html')


def contact(request):
    return render(request, 'contact.html')


def order(request):
    return render(request, 'book_a_table.html')

def token(request):
    consumer_key = 'jGwhIUHzBuLqsMmE4Y9KE0OC2Lfh6c1w'
    consumer_secret = 'tFgqczyjiayK16Hp'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
    return render(request, 'pay.html')

def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Kelcho Tech",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse(response)


#
# def show(request):
#     employees = Employee.objects.all()
#     return render(request, 'show.html', {'employees': employees})
#
#
# def delete(request, id):
#     emp = Employee.objects.get(id=id)
#     emp.delete()
#     return redirect('/show')
#
#
# def edit(request, id):
#     emp = Employee.objects.get(id=id)
#     return render(request, 'edit.html', {'emp': emp})
#
#
# def update(request, id):
#     emp = Employee.objects.get(id=id)
#     form = EmpForm(request.POST, instance=emp)
#     if form.is_valid():
#         form.save()
#         return redirect('/show')
#     else:
#         return render(request, 'edit.html', {'emp': emp})
#
#
# def employee(request):
#     if request.method == 'POST':
#         form = EmpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/")
#     else:
#         form = EmpForm()
#     return render(request, 'employee.html', {'form': form})