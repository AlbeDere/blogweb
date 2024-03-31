from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from blog.models import BlogPost, Comment
from blog.forms import CommentForm, BlogPostForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test


def blog_index(request):
    posts = BlogPost.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = BlogPost.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if not request.user.is_authenticated:
                return render(request, 'blog/login.html', {'error': 'You need to login or register to comment.'})
            comment = Comment(
                author=request.user,  # Assign the currently logged-in user as the author of the comment
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/post.html", context)


def about(request):
    return render(request, "blog/about.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Construct email message
        subject = 'New Contact Form Submission'
        message_body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        sender_email = settings.EMAIL_HOST_USER
        receiver_email = 'a.derevski@outlook.com'

        # Send email
        try:
            send_mail(subject, message_body, sender_email, [receiver_email])
            # set up email in settings. Change EMAIL_HOST_USER and EMAIL_HOST_PASSWORD
            return render(request, 'blog/contact.html', {'msg_sent': True})
        except Exception as e:
            print(e) 
            return render(request, 'blog/contact.html', {'msg_sent': True})
            # return HttpResponse('Error sending email. Please try again later.', status=500 - This what it should really do not the line above.

    else:
        return render(request, 'blog/contact.html', {'msg_sent': False})
    

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            # Handle password mismatch error
            return render(request, 'blog/register.html', {'error': 'Passwords do not match'})

        # Check if username is already taken
        if User.objects.filter(username=username).exists():
            # Handle username already exists error
            return render(request, 'blog/register.html', {'error': 'Username already exists'})

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password1)

        # Log in the user after registration
        login(request, user)

        # Redirect to the home page
        return redirect('blog_index')
    else:
        return render(request, 'blog/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog_index')
        else:
            # Display an error message if login fails
            return render(request, 'blog/login.html', {'error': 'Invalid username or password. Please try again.'})
    else:
        return render(request, 'blog/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('blog_index')

@user_passes_test(lambda u: u.is_superuser)
def create_blogpost(request):
    form = BlogPostForm(request.POST)
    if form.is_valid():
        blog_post = form.save(commit=False)
        blog_post.author = request.user 
        blog_post.save()
        form.save_m2m()
        return redirect('blog_index')
    else:
        form = BlogPostForm()
    return render(request, 'blog/make-post.html', {'edit': False, 'form': form})


@user_passes_test(lambda u: u.is_superuser)
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    return redirect('blog_index')  # Redirect to home page or any other appropriate page


@user_passes_test(lambda u: u.is_superuser)
def edit_blogpost(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=post.pk)  # Redirect to home page or any other appropriate page
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog/make-post.html', {'edit': True, 'form': form, 'img_url': post.img_url})
