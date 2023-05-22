from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse

from home.models import Groceries  # , ProductList


# Create your views here.


def index(request):
    if request.method == 'POST':
        print("data: ", request.POST['product_name'], "received!!!")
        Groceries.objects.create(name=request.POST['product_name']) # später noch is_valid abfrage hinzufügen
    groceries = Groceries.objects.all() # diese variabel speichert alle geseneten produkte der Klasse. Wenn auf Sie in zB einer for scleife zugegriffen werden muss, muss dieser varibelnam benutz werden.
    return render(request, 'home/base.html', {'groceries': groceries})

'''
def save_product_list(request):
    if request.method == 'POST':
        ProductList.objects.create(name=request.POST['product_name']) # später noch is_valid abfrage hinzufügen
    products = ProductList.objects.all()
    return render(request, 'home/base.html', {'products': products})
'''

def description(request):
    return render(request, 'home/description.html')


def register_view(request):
    register_form = UserCreationForm() #1
    if request.method == "POST":   # zuerst wird überprüft, ob eine POST anfrage an den Server geschickt wurde
        register_form = UserCreationForm(request.POST)  # in diesem Fall wird die UserCreationForm einer variabel als Post anfrage übergeben
        if register_form.is_valid():  # es wird geprüft, ob die eingebenen Werte den Bedingungen entsprechen
            register_form.save()   # der neue Benutzer wird angelegt sofern alles stimmt.
            username = register_form.cleaned_data.get('username')  # der Benutzername wird gespeichert
            password = register_form.cleaned_data.get('password1')  # das pw ebenso
            if user := authenticate(
                request, username=username, password=password
            ):
                login(request, user)  # der user wird authentifizirert und in seinen neu erstellte account eingelogged.
                return redirect(reverse('home:index')) # sobald sich der user registriert hat, wird er zur hoempage weitergeleitet

    return render(request, 'home/register.html', {'register_form': register_form})


def logout_view(request):
    logout(request)
    return redirect(reverse('home:index'))


def login_view(request):
    authentication_form = AuthenticationForm()
    if request.method == "POST":
        authentication_form = AuthenticationForm(request.POST)
        if authentication_form.is_valid():
            return redirect(reverse('home:index'))
    return render(request, 'home/login.html', {'authentication_form': authentication_form})

# searchbox




#1 =  Django hat schon ein fertiges Template für die Registrierung vorgeschrieben. Dieses benutzen wir hier.
#Bedeutet soviel wie: Wenn der Benutzer die auf den logggedin klickt wird dieses Template geladen. afür müssen wir zunächst aber noch  schritte ausführen.
#Zum einen müssen wir die definierte variable natürlih noch in unse register.html- File einbauen. das tun wir wie folgt:
# {{ regiter_form.as_p }} - mit .as_p damit geben wir die Felder als paragraph aus(die daten werden, gerendert.)
# als nchsten schritt müssen wir natürlich auch die url festlegen. Dafür gehst du in das app (in diesem fall home) -File urls file und
# diefinierst du einfach die url