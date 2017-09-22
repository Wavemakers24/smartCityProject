from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Users
from django.views import generic
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import registrationForm


#def index(request):
    #all_user = Users.objects.all()
    #return render(request, 'smartcity/userlist.html', {'all_user': all_user})

'''class register(View):
    form_class = registrationForm
    template_name = 'smartcity/register.html'
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            # cleaned  (normalised) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            firstname = form.cleaned_data['firstname']
            middlename = form.cleaned_data['middlename']
            lastname = form.cleaned_data['lastname']
            gender = form.cleaned_data['gender']
            dob = form.cleaned_data['dob']
            unit = form.cleaned_data['unit']
            street = form.cleaned_data['street']
            suburb = form.cleaned_data['suburb']
            state = form.cleaned_data['state']
            postcode = form.cleaned_data['postcode']
            phoneNumber = form.cleaned_data['phoneNumber']
            email = form.cleaned_data['email']
            userType = form.cleaned_data['userType']
            user.save()

            #return User objects if credentials are correct
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('smartcity:index')'''



def userprofile(request, user_id):
    #return HttpResponse("<h2>Detail for userID:" + str(user_id) + "</h2>")
    user = get_object_or_404(Users, pk=user_id)
    return render(request, 'smartcity/userprofile.html', {'user': user})

def editinfo(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    Users.save()
    return render(request, 'smartcity/userprofile.html', {'user': user})
def welcome(request):
    return render(request, 'smartcity/welcome.html')

def template(request):
    return render(request, 'smartcity/template.html')

def profile(request):
    return render(request, 'smartcity/profile.html')

def login(request):
    return render(request, 'smartcity/login.html')

def account(request):
    return render(request, 'smartcity/account.html')

def register(request):
    return render(request, 'smartcity/register.html')


#def test(request):
    #template = loader.get_template('smartcity/test.html')
    #return HttpResponse(template.render(request))
    #return HttpResponse("<h1>Userprofile:" + str(Users.username) + "</h1>")



