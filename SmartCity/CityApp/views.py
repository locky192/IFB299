# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from CityApp.forms import UserForm, UserProfileForm, UpdateProfile
from templates.function import write_func
from CityApp.models import CityInfo, UserProfile
from django.shortcuts import render_to_response



# Create your views here.
def index(request):
    userProfile = UserProfile.objects.all()
    context = {'userProfile': userProfile}
    return render(request, 'CityApp/index.html', context)

def signed (request):
    return render(request, 'CityApp/signed.html')

def login(request):
    return render(request, 'CityApp/login.html')

def admin_login(request, template_name):
    return render(request, 'CityApp/admin_login.html')

def info_page(request):
	userid= request.user.id
	print(userid)
	currentUser=UserProfile.objects.get(id=7)
	cityInfo = CityInfo.objects.all()
	context = {'cityInfo':cityInfo, 'currentUser':currentUser}

	return render(request, 'CityApp/infopage.html', context)

def library_list(request):
	cityInfo = CityInfo.objects.filter("Hotel")
	context = {'cityInfo':cityInfo}
	return render(request, 'CityApp/infopage.html', context)

def xml_page(request):
    response = render_to_response('CityApp/convertcsv.xml')
    response['Content-Type'] = 'application/xml;'
    # return render(request, 'CityApp/convertcsv.xml')
    return response

def show_landmark(request, landmark_name_slug):
    context_dict = {}

    try:
        landmark = CityInfo.objects.get(slug=landmark_name_slug)

        context_dict['landmark']= landmark

    except cityInfo.DoesNotExist:
        context_dict['landmark']= None

    return render(request, 'CityApp/landmark.html', context_dict)

def button(request):
	return render(request, 'CityApp/button.html')

def button_function(request):
	write_func()
	return render(request, 'CityApp/button.html', {})


def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST, instance=request.user)
        # form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/CityApp/')
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'CityApp/update.html', args)


def register (request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
# Save the user's form data to the database.
            user = user_form.save()
# Now we hash the password with the set_password method.
# Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()
# Now sort out the UserProfile instance.
# Since we need to set the user attribute ourselves,
# we set commit=False. This delays saving the model
# until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
# Did the user provide a profile picture?
# If so, we need to get it from the input form and
#put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
# Now we save the UserProfile model instance.
            profile.save()
# Update our variable to indicate that the template
# registration was successful.
            registered = True
        else:
# Invalid form or forms - mistakes or something else?
# Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
# Not a HTTP POST, so we render our form using two ModelForm instances.
# These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()
# Render the template depending on the context.
    return render(request,
    'CityApp/register.html',
    {'user_form': user_form,
    'profile_form': profile_form,
    'registered': registered})
