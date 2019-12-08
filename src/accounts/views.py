from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from pprint import pprint
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        refresh = request.POST['refresh']

        user = auth.authenticate(username=username, password=password)
        data = {'error_message': '', 'success_message': ''}

        if user is not None:
            auth.login(request, user)
            if refresh == 'no':
                
                return JsonResponse(data)
            else:
                return redirect('my_profile')
        else:
            if refresh == 'no':
                data['error_message'] = 'Password or Username incorrect!'
                return JsonResponse(data)
            else:
                messages.error(request, 'Password or Username incorrect!')
                return JsonResponse({'get': 'get'})
    else:
        return JsonResponse({'get': 'get'})


def register(request):
    data = {'success_message': '', 'error_message': ''}

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        refresh = request.POST['refresh']

    # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                if refresh == 'yes':
                    messages.error(request, 'That username is taken')
                    return redirect('register')
                else:
                    data['error_message'] = 'A user with this username already exists!'
                    return JsonResponse(data)
            else:
                if User.objects.filter(email=email).exists():
                    if refresh == 'yes':
                        messages.error(request, 'That email is being used')
                        return redirect('register')
                    else:
                        data['error_message'] = 'That email is being used!'
                        return JsonResponse(data)
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register

                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    auth.login(request, user)

                    if refresh == 'yes':
                        return redirect('my_profile')
                    else:
                        data['success_message'] = 'You are now registered! Redirecting to index page.'
                        return JsonResponse(data)
        else:
            if refresh == 'yes':
                messages.error(request, 'Passwords do not match')
                return redirect('register')
            else:
                data['error_message'] = 'Passwords do not match!'
                return JsonResponse(data)
    else:
        return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')


@login_required
def my_profile(request):
    return render(request, 'accounts/my_profile.html')
