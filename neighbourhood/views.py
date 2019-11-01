from django.shortcuts import render,redirect

from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import *
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required(login_url='/accounts/login/') 
def news_today(request):
    date = dt.date.today()
    images= Neighbour.objects.all()
    current_user=request.user
    myprof=Profile.objects.filter(id=current_user.id).first()
    
    if request.method == 'POST':
        form = uploadimageForm(request.POST)
        if form.is_valid():
            print('valid')
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('news_today')

    else:
        form = uploadimageForm()
    return render(request, 'home.html', {"date": date,"images":images,"myprof":myprof,"letterForm":form})


@login_required(login_url='/accounts/login/')       
def article(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-news/article.html", {"article":article})
# @login_required(login_url='/accounts/login/')
# def new_article(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = uploadimageForm(request.POST, request.FILES)
#         if form.is_valid():
#             article = form.save(commit=False)
#             article.editor = current_user
#             article.save()
#         return redirect(news_today)

#     else:
#         form = uploadimageForm()
#     return render(request, 'new_article.html', {"form": form})

@login_required(login_url='/accounts/login/')
def mine(request,username=None):
    current_user=request.user
    pic_images=Neighbour.objects.filter(user=current_user)
    # profile=Profile.objects.filter(user=current_user).first()
    if not username:
      username=request.user.username
      images = Neighbour.objects.filter(name=username)
      user_object = request.user
    
      businesses = Business.objects.filter( location= user).all()
      emergencies = Contact.objects.filter( contacts= user).all()
      neighborhoods = Neighbour.objects.all()
  
    return render(request, 'myprofile.html', locals(),{"pic_images":pic_images})

@login_required(login_url='/accounts/login/')
def edit(request):
    current_user=request.user
    profile = Profile.objects.filter(user=current_user)
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            last_name=form.save(commit=False)
            last_name.user=current_user
            last_name.save()
            return redirect('mine')
    else:
         form =ProfileForm()

    businesses = Business.objects.filter( location= user).all()
    emergencies = Contact.objects.filter( contacts= user).all()
    neighborhoods = Neighbour.objects.all()

    return render(request,'edit.html',{"form":form,"businesses":businesses,"emergencies":emergencies," neighborhoods": neighborhoods})

@login_required(login_url='/accounts/login/')
def user(request, user_id):
    user_object = get_object_or_404(User, pk=user_id)
    if request.user == user_object:
        return redirect('myaccount')
    following = user_object.profile not in request.user.profile.follows
    user_images = user_object.profile.posts.all()
   
    return render(request, 'profile.html', locals())

def business(request):
    user = User.objects.filter(id = request.user.id).first()
    profile = Profile.objects.filter(user = user).first()
    if request.method == 'POST':
        form = AddBusinessForm(request.POST)
        if form.is_valid():
            business = Business(name = request.POST['name'],owner = user,business_neighborhood = profile.neighborhood,email=request.POST['email'])
            business.save()
        return redirect('mine')
    else:
         form = AddBusinessForm()
    return render(request,'business.html',{'form':form})






def search_results(request):

    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = Profile.search(search_term)
        # message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"users": searched_users})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
