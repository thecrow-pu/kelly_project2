from django.urls import path
from kelly_app import views
app_name = 'kelly_app'
urlpatterns = [
    path('', views.index_view.as_view(), name='index'),
    path('', views.index_view.as_view(), name='index'), # This will now be the root URL
    path('about/', views.about_view.as_view(), name='about'),
    path('contact/', views.contact_view.as_view(), name='contact'),
    path('services/', views.services_view.as_view(), name='services'),
    path('resume/', views.resume_view.as_view(), name='resume'),
    path('starter-page/', views.starter_page_view.as_view(), name='starter-page'),
    path('portfolio/', views.portfolio_view.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', views.portfolio_details_view.as_view(), name='portfolio-details'),
    path('portfolio/create/', views.portfolio_create_view.as_view(), name='portfolio_create'),
    path('portfolio/<int:pk>/update/', views.portfolio_update_view.as_view(), name='portfolio_update'),
    path('portfolio/<int:pk>/delete/', views.portfolio_delete_view.as_view(), name='portfolio_delete'),

]