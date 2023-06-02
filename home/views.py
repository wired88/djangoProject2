from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.http import request
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, DeleteView, CreateView, DetailView
from home.models import Groceries, UsersRecipesCreate  # , ProductList


# LISTVIEW lässt rendert alle eingabemöglichkeiten auf der Website als liste
# DETAILVIEW rendert ein element auf der liste nachdem es angeklickt wurde
# zB viele rezepte werden durch listview gerendert.. sobald man eines anklickt, wird dieses eine angezeigt

# Create your views here.


class RecipeDetailView(DetailView):
    model = UsersRecipesCreate
    template_name = 'home/recipe_detail_view.html'















class RegisterView(FormView):    #for user registration
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.save()  # wenn die form valid ist, wird sie gespeichert.
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        if user := authenticate(  # wenn der user authentifizert ist...
                self.request, username=username, password=password
        ):
            login(self.request, user)  # wird der user eingelogged,
            return redirect(self.get_success_url())  # er wird zum sucess_url weitergeleitetr.
        else:
            messages.error(self.request, 'Invalid input')  # ansonsten erhält der user diese Fhelermeldung
            return super().form_invalid(form)  # und diese


class UserLoginView(FormView): # for user login
    form_class = AuthenticationForm
    template_name = 'home/login.html'
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')  # der Benutzername wird gespeichert
        password = form.cleaned_data.get('password')
        if user := authenticate(
                request, username=username, password=password
        ):
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, 'Invalid E-Mail or Password')  # ansonsten erhält der user diese Fhelermeldung
            return super().form_invalid(form)





class UsersRecipesCreateView(CreateView): # for user create a recipe
    model = UsersRecipesCreate  # das model wird ausgewählt
    fields = ['title', 'recipe_picture', 'body']  # die textfelder wrden in 3 verschiedene Spaslten aufgeteilt
    template_name = 'home/user_create_recipe.html'  # in welchem template die form dargestellt werdfen soll
    success_url = reverse_lazy('home:index')

    def form_valid(self, form):
        form.instance.author = self.request.user  # wenn die form valid ist, wird der benutzer der diese form erstellt hat, automatisch hinzugefügt.
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Oups... Invalid input! Please try again.')
        return super().form_invalid(form)


class UsersRecipesView(ListView):  # all recipes that thre user creaTEd LISTED VIEW
    model = UsersRecipesCreate
    template_name = 'home/users_recipes.html'




class HomeView(CreateView, ListView): # von diesen 2 Klassen wird geerbt wenn im gleichen html file eine get und post anfrage gebraucht wird.
    template_name = 'home/base.html'
    success_url = reverse_lazy('home:index')
    model = Groceries
    fields = ['name']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Oups... Invalid input! Please try again.')
        return super().form_invalid(form)


def index(request):
    if request.method == 'POST':
        print("data: ", request.POST['product_name'], "received!!!")
        Groceries.objects.create(name=request.POST['product_name'])  # später noch is_valid abfrage hinzufügen
    groceries = Groceries.objects.all()  # diese variabel speichert alle geseneten produkte der Klasse. Wenn auf Sie in zB einer for scleife zugegriffen werden muss, muss dieser varibelnam benutz werden.
    return render(request, 'home/base.html', {'groceries': groceries})


class DeleteObjectView(DeleteView):
    model = Groceries
    success_url = reverse_lazy('home:index')
    template_name = 'home/base.html'

    def post_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groceries'] = Groceries.objects.all()
        return context


class DescriptionView(TemplateView):
    template_name = 'home/description.html'


def logout_view(request):
    logout(request)
    return redirect(reverse('home:index'))


class ProfileView(TemplateView):
    template_name = 'home/profile.html'


class SettingsView(TemplateView):
    template_name = 'home/settings.html'


def delete_view(request, pk):
    product = get_object_or_404(Groceries,
                                id=pk)  # ein Element aus Groceries wird in roduct gespeichert. Die id des Elements wird als Paramet übergeben damit das gelöschte Objekt zufällig ausgewählt werden kann
    product.delete()  # das ausgewählte Produkt wird gelöscht
    return redirect(reverse('home:index'))  # der user wird zur home-page weitergeleitet.


# immer darauf achten, dass im urls file das parameter mit übergeben werden muss. (siehe urls.py)


# searchbox


# 1 =  Django hat schon ein fertiges Template für die Registrierung vorgeschrieben. Dieses benutzen wir hier.
# Bedeutet soviel wie: Wenn der Benutzer die auf den logggedin klickt wird dieses Template geladen. afür müssen wir zunächst aber noch  schritte ausführen.
# Zum einen müssen wir die definierte variable natürlih noch in unse register.html- File einbauen. das tun wir wie folgt:
# {{ regiter_form.as_p }} - mit .as_p damit geben wir die Felder als paragraph aus(die daten werden, gerendert.)
# als nchsten schritt müssen wir natürlich auch die url festlegen. Dafür gehst du in das app (in diesem fall home) -File urls file und
# diefinierst du einfach die url



# - User kann selbstständig Rezepte hochladen
# - Profile-Page: create your own recipe!


''' Function based view:
def register_view(request):
    register_form = UserCreationForm()  # 1
    if request.method == "POST":  # zuerst wird überprüft, ob eine POST anfrage an den Server geschickt wurde
        register_form = UserCreationForm(
            request.POST)  # in diesem Fall wird die UserCreationForm einer variabel als Post anfrage übergeben
        if register_form.is_valid():  # es wird geprüft, ob die eingebenen Werte den Bedingungen entsprechen
            register_form.save()  # der neue Benutzer wird angelegt sofern alles stimmt.
            username = register_form.cleaned_data.get('username')  # der Benutzername wird gespeichert
            password = register_form.cleaned_data.get('password1')  # das pw ebenso
            if user := authenticate(
                    request, username=username, password=password
            ):
                login(request, user)  # der user wird authentifizirert und in seinen neu erstellte account eingelogged.
                return redirect(
                    reverse('home:index'))  # sobald sich der user registriert hat, wird er zur hoempage weitergeleitet
            else:
                messages.error(request, 'Invalid E-Mail or Password')
    return render(request, 'home/register.html', {'register_form': register_form})


class UserLogoutView(LogoutView):
    success_url = 'home:index'

    def get_redirect_url(self):
        return redirect(reverse('home:index'))



def login_view(request):
    authentication_form = AuthenticationForm()
    if request.method == "POST":
        authentication_form = AuthenticationForm(data=request.POST)
        if authentication_form.is_valid():
            username = authentication_form.cleaned_data.get('username')  # der Benutzername wird gespeichert
            password = authentication_form.cleaned_data.get('password')  # das pw ebenso
            if user := authenticate(
                    request, username=username, password=password
            ):
                login(request, user)
                return redirect(reverse('home:index'))
        else:
            messages.error(request, 'Invalid E-Mail or Password')
    return render(request, 'home/login.html', {'authentication_form': authentication_form})
'''



'''
class CreateRecipe(FormView):
    model = UsersRecipesCreate
    template_name = 'home/user_create_recipe.html'
    success_url = reverse_lazy('home:index')
'''




'''
class HomeView(ListView):
    model = Groceries
    template_name = 'home/base.html'


class HomeCreateView(CreateView):
    model = Groceries
    template_name = 'home/base.html'
    fields = ['name']



    def form_valid(self, form):
        form.save()
        print('received!!!!!!!!!!!!!!!!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Oups... Invalid input! Please try again.')
        return super().form_invalid(form)



'''
