from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView,UpdateView,DeleteView,CreateView,TemplateView
from . import models
from django.urls import reverse_lazy
# Create your views here.
class index_view(TemplateView):
    template_name = 'kelly_app/index.html'

class about_view(ListView):
    model = models.Contact
    context_object_name = 'about_list'
    template_name = 'kelly_app/about.html'

class contact_view(ListView):
    model = models.Contact
    context_object_name = 'contact_list'
    template_name = 'kelly_app/contact.html'

class services_view(ListView):
    model = models.Contact
    context_object_name = 'services_list'
    template_name = 'kelly_app/services.html'

class resume_view(ListView):
    model = models.Contact
    context_object_name = 'resume_list'
    template_name = 'kelly_app/resume.html'

class starter_page_view(ListView):
    model = models.Contact
    context_object_name = 'starter_page_list'
    template_name = 'kelly_app/starter-page.html'

class portfolio_view(ListView):
    model = models.Portfolio
    context_object_name = 'portfolio_list'
    template_name = 'kelly_app/portfolio.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_detail'] = models.Portfolio.objects.all()
        return context

class portfolio_create_view(CreateView):
    model = models.Portfolio
    fields = '__all__'
    template_name = 'kelly_app/portfolio_form.html'
    success_url = '/portfolio/'
    context_object_name = 'portfolio_create'

class portfolio_update_view(UpdateView):
    model = models.Portfolio
    fields = '__all__'
    template_name = 'kelly_app/portfolio_form.html'
    success_url = '/portfolio/'

class portfolio_delete_view(DeleteView):
    model = models.Portfolio
    template_name = 'kelly_app/portfolio_delete_confirm.html'
    context_object_name = 'portfolio_delete'
    success_url = reverse_lazy('kelly_app:portfolio')

class portfolio_details_view(DetailView):
    model = models.Portfolio
    context_object_name = 'portfolio_item'
    template_name = 'kelly_app/portfolio-details.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio_list'] = models.Portfolio.objects.all()
        return context