from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('project/<int:id>',views.project_view,name='project'),
    path('contact',views.contact_us,name='contact_us'),
    
]
