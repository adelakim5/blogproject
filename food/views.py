from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Comment
from django.utils import timezone
import random
from django.contrib.auth.decorators import login_required

@login_required


# Create your views here.
def home(request):
    food = Food.objects.all()
    return render(request, 'home.html',{'food_posts':food})

def create(request):
    food = Food()
    food.title = request.POST['title']
    food.body = request.POST['body']
    if request.FILES:
        food.image = request.FILES['post_image']
    food.pub_date = timezone.datetime.now()
    food.save() # 저장해주는 기능 
    return redirect('list')

def read(request, post_id):
    post = get_object_or_404(Food, pk=post_id)
    return render(request, "read.html", {'food_post':post})
    
def list(request):
    food = Food.objects.all()
    return render(request,"list.html", {'food_posts':food})

def write(request):
#     # food = Food()
#     # # food.title = request.POST['title']
#     # food.body = request.POST['body']
#     # if request.FILES:
#     #     food.image = request.FILES['image']
#     # food.pub_date = timezone.datetime.now()
#     # food.save()
    return render(request,"write.html")

def update(request, post_id):
    updated_post = get_object_or_404(Food, pk=post_id)
    updated_post.title = request.POST['title']
    updated_post.body = request.POST['body']
    updated_post.save()
    return redirect('/food/'+ str(updated_post.id)) 
    
def renew(request, post_id):
    renew_post = get_object_or_404(Food, pk=post_id)
    return render(request, 'renew.html', {'renew': renew_post})

def delete(request, post_id):
    deleted_post = get_object_or_404(Food, pk=post_id)
    deleted_post.delete()
    return redirect('home')

def create_c(request, post_id):
    comment = Comment()
    comment.username = request.POST['comment_username']
    comment.body = request.POST['comment_body']
    comment.pub_date = timezone.datetime.now()
    comment.post = get_object_or_404(Food, pk=post_id)
    comment.save()

    return redirect('read', post_id=post_id)