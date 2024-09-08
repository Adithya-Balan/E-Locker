from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('sign-up', views.sign_up, name = 'registration'),
    path('profile', views.profile, name = 'profile'),
    path('document-imp', views.imp_documents, name ='imp-doc'),
    path('Recent', views.recent, name = 'recent'),
    
    path('upload/<str:category>', views.upload_view, name = 'upload_view'),
    # path('uploads', views.uploads, name='uploads'),
]
