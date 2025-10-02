from django.shortcuts import render

from kelly_app.models import Portfolio


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    accPortfolio = Portfolio.objects.all()
    dic ={
        'accPortfolio': accPortfolio,
        'title': 'Portfolio'
    }
    return render(request, 'portfolio.html',context=dic)

def resume(request):
    return render(request, 'resume.html')

def starter_page(request):
    return render(request, 'starter_page.html')
    
def portfolio_details(request):
    return render(request, 'portfolio-details.html')
