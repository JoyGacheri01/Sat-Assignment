from django.shortcuts import render, redirect

from .models import Quote

# Create your views here.

def home(request):
    return render(request, 'home.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def projects(request):
    return render(request, 'projects.html')

def insert_quote(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        quote = Quote(
            name=name,
            email=email,
            phone=phone,
            message=message)

        quote.save()
        return redirect('/venture/view_quote/')
    return render(request, 'home.html')

def view_quote(request):
    quotes = Quote.objects.all()
    return render(request, 'view_quote.html', {'quotes': quotes})

def update_quote(request):
    quote = Quote.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        quote.name = name
        quote.email = email
        quote.phone = phone
        quote.message = message

        quote.save()
        return redirect('/')
    return render(request, 'view_quote.html', {'quote': quote})
