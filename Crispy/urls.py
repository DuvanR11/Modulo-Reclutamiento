from django.contrib import admin
from django.urls import include, path
from appCrispy import views
from Crispy import settings
from django.conf.urls.static import static

admin.site.site_header = 'Crispy'
admin.site.index_title = 'ADMINISTRAÇÃO'

urlpatterns = [
    #Admin
    path ('admin/', admin.site.urls),
    #Fontend
    path ('', views.home, name='home'),
    path ('register', views.register, name='register'),
    path ('login/', include('django.contrib.auth.urls')),
    
    #Backend
    path ('backend', views.backend, name='backend'), 
    path ('<int:id>/', views.engineer, name='engineer'), 
    
      
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


