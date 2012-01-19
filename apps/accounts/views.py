import hashlib
import time
from django.contrib.auth import login, logout, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import update_object, delete_object
from .mail import async_send_mail
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.http import Http404
from django.core.mail import send_mail
from .forms import RegisterForm, LoginForm
from profiles.models import Bookmark, Profile
from profiles.forms import ProfileCoreForm, ProfileOptionalForm
from companies.models import Position
from settings import common

# account crud operations
def account_detail(request):
    return direct_to_template(request, "accounts/account_detail.html")

def account_update(request):
    profile = get_object_or_404(Profile, id_booster=request.user.username)
    
    if request.method == 'POST':
        form = ProfileOptionalForm(request.POST, instance=profile)
        
        if form.is_valid():
            profile.description = form.cleaned_data['description']
            profile.linkedin_url = form.cleaned_data['linkedin_url']
            profile.viadeo_url = form.cleaned_data['viadeo_url']
            profile.facebook_url = form.cleaned_data['facebook_url']
            profile.twitter_url = form.cleaned_data['twitter_url']
            profile.save()
            return redirect('accounts-detail')
    else:
        form = ProfileOptionalForm(instance=profile)
    
    context = {'form':form}
    
    return direct_to_template(request, "accounts/account_form.html", extra_context=context)

def account_logout(request):
    logout(request)
    return redirect("/")

def account_login(request):
    if request.user.is_authenticated():
        return redirect('accounts-detail')
    
    register_form = RegisterForm()
    login_form = LoginForm()
    
    if request.method == "POST":
        if "register" in request.POST.values():
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                
                # set the key as a password, so we can match this user when he comes back
                id_booster = register_form.cleaned_data['id_booster']
                str = "%s%s%s" % (time.time(), id_booster, common.SECRET_KEY)
                key = hashlib.sha1(str).hexdigest()
                user = User.objects.create_user(id_booster, id_booster+"@supinfo.com", key)
                user.is_active = False
                user.save()
                
                # send mail with the key (unhashed !)
                full_url = "http://%s%s"  % (Site.objects.get_current().domain, reverse('accounts-register-complete', args=[id_booster, key]))
                
                subject = "Registration confirmation"
                content = "To complete your registration on the supalumni network, follow this link : " + full_url  
                content += "\n\n Thank you"
                      
                to = user.email

                #async_send_mail(subject, content, None, [to])
                send_mail(subject, content, None, [to])
                return redirect("accounts-register-initiate")   

                             
        elif "login" in request.POST.values():
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user = login_form.save()
                user_auth = authenticate(username=login_form.cleaned_data['id_booster'], password=login_form.cleaned_data['password'])
                login(request, user_auth)
                return redirect("accounts-detail")
                
    
    context = {'register_form': register_form, 'login_form': login_form}
    return direct_to_template(request, "accounts/login.html", extra_context=context)

def register_initiate(request):
     return direct_to_template(request, "accounts/register_initiate.html")
    
def register_complete(request, id_booster, key):
    user = authenticate(username=id_booster, password=key)
    if not user:
        raise Http404
    
    if request.method == "POST":
        form = ProfileCoreForm(request.POST)
        if form.is_valid():
            # User
            user.first_name = form.cleaned_data['first_name'].lower().title()
            user.last_name = form.cleaned_data['last_name'].upper()
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()
            
            # create corresponding profile
            profile = Profile()
            profile.user_id=user.id
            profile.id_booster=user.username
            profile.promotion=form.cleaned_data['promotion']
            profile.set_last_name(user.last_name)
            profile.save()
            
            # log & redirect
            user_auth = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, user_auth)
            
            return redirect("accounts-register-rules")
    else:
        form = ProfileCoreForm()
    
    context =  {'form': form, 'pending_user':user}
    return direct_to_template(request, "accounts/register_complete.html", extra_context=context)

# bookmarks
def bookmarks_add(request, profile_id):
    if profile_id == request.user.username: # can't bookmark yourself
        return redirect('profiles-detail', request.user.username)
    
    my_profile = get_object_or_404(Profile, id_booster=request.user.username)
    my_profile.add_bookmark_on_profile(profile_id)
    
    return redirect('profiles-detail', profile_id=profile_id)
    
def bookmarks_list(request):
    my_profile = Profile.objects.get(id_booster=request.user.username)
    my_bookmarks = my_profile.get_bookmarked_profiles()
    my_bookmarks_profiles = Profile.objects.filter(id_booster__in = my_bookmarks.values('to_profile__id_booster'))
    from profiles.views import get_positions_dict
    context = {'positions' : get_positions_dict(my_bookmarks_profiles) }
    return object_list(request, queryset=my_bookmarks, extra_context=context)
    
def bookmarks_delete(request):
    obj = request.POST['delete']
    get_object_or_404(Bookmark, pk=obj, from_profile=request.user.username)
    return delete_object(request, Bookmark, reverse("accounts-bookmarks-list"), object_id=obj)

def register_rules(request):
    return direct_to_template(request, "accounts/register_rules.html")

def dashboard(request):
    return direct_to_template(request, "accounts/dashboard.html")