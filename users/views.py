from django.shortcuts import render , redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm,UserUpdateform,ProfileUpdateForm,AuthorSearchForm,ContactUsForm
from django.core.mail import send_mail
from django.conf import settings



def user_logout(request):
    logout(request)
    return render(request, 'users/logout.html', {})

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request ,f' Congratulations {username} you are able to login now !')
            return redirect('login')

    else:
        
        form=UserRegistrationForm()
    
    
    return render( request ,'users/register.html' , {'form':form})


@login_required
def user_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username=u_form.cleaned_data.get('username')
            messages.success(request ,f' Congratulations {username} your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    # Check if the 'edit' parameter is set in the GET request
    editing = request.GET.get('edit') == 'true'

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'editing': editing
    }

    return render(request, 'users/profile.html', context)



def user_search(request):
    from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import AuthorSearchForm

def search_by_author(request):
    if request.method == 'POST':
        form = AuthorSearchForm(request.POST)
        if form.is_valid():
            authors = form.cleaned_data.get('authors')
            # Redirect to the page that lists all posts by the selected author
            return redirect('user-posts', username=authors.username)
    else:
        form = AuthorSearchForm()
    return render(request, 'blog/search_author.html', {'form': form})



def ContactUs(request):
    if request.method=='POST':
        form=ContactUsForm(request.POST)
        if form.is_valid():
            # Save the form data
            contact = form.save()

            # Send email
            subject = f"Contact Us message from {contact.name}"
            message = f"Message:\n{contact.message}\n\nFrom: {contact.name}\nEmail: {contact.email}"
            from_email = contact.email  # User's email
            recipient_list = [settings.EMAIL_HOST_USER]  # Host email (your email)
            
            # Send the email
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            # Show success message and redirect
            messages.success(request, 'Thank you for contacting us. We will get back to you soon!')
            return redirect('blog-home')
    else:
        form=ContactUsForm()
    return render(request, 'blog/contacts.html', {'form': form})

        