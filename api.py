




import requests
from django.contrib.auth import authenticate, login

def consumir_api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Realiza una solicitud POST a la API con los datos de inicio de sesión
        url = 'http://127.0.0.1:8000/api/'
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url, data=data , auth=(username, password))
        if response.status_code == 200:
            # Parsear la respuesta y extraer los datos del usuario
            user_data = response.json()
            username = user_data['username']
            # Usar la función login de Django para iniciar sesión con el usuario
            user = authenticate(username=username, password=request.POST.get('password'))
            login(request, user)
            return redirect('home')
        else:
            # Mostrar un mensaje de error en caso de que la respuesta no sea exitosa
            return render(request, 'log/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'log/login.html')



    ##############################################################################################




    from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import FormView
# from.forms import LoginForm
import requests
import json



# class LoginView(FormView):
#     template_name = 'log/login.html'
#     form_class = LoginForm

#     def form_valid(self, form): 
#         #Obtén los datos del formulario de inicio de sesión
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         # Haz una solicitud POST a la API con los datos de inicio de sesión
#         url = 'http://127.0.0.1:8000/api/'
#         data = {
#             "username": username,
#             "password": password
#         }
#         response = requests.post(url, data=data , auth=(username, password))
#         if response.status_code == 200:
#             res = response.json()
#             print(res)
#             is_staff = res['is_staff']
#             if is_staff == True:
#                 return redirect('dash')
#             else:
#                 return redirect('home')
#         else :#Muestra un mensaje de error en el formulario de inicio de sesión
#             return render(self.request, 'log/login.html', {'form': form,'error': 'Usuario o contraseña incorrectos'})





# def home(request):
#     return render(request, 'home.html')


# def dash(request):
#     return render(request, 'dashboard.html')




# views.py

# from django.shortcuts import render, redirect
# import requests

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         # Realiza una solicitud POST a la API con los datos de inicio de sesión
#         url = 'http://127.0.0.1:8000/api/'
#         data = {
#             "username": username,
#             "password": password
#         }
#         response = requests.post(url, data=data , auth=(username, password))
#         if response.status_code == 200:
#             user_data = response.json()
#             username = user_data['username']
#             user = authenticate(username=username, password=request.POST.get('password'))
#             login(request, user)
#             return HttpResponseRedirect(reverse('home'))
#         else :
#             return render(request, 'log/login.html', {'error': 'Usuario o contraseña incorrectos'})

#     return render(request, 'log/login.html')


import requests
from django.contrib.auth import authenticate, login

def consumir_api_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Realiza una solicitud POST a la API con los datos de inicio de sesión
        url = 'http://127.0.0.1:8000/api/'
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url, data=data,auth=(username, password))
        if response.status_code == 200:
            user_data = response.json()
            username = user_data['username']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                print("cueck")
        else:
            return render(request, 'log/login.html', {'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'log/login.html')




def home(request):
    return render(request, 'home.html')


def dash(request):
    return render(request, 'dashboard.html')
