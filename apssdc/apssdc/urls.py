"""apssdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Student import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nemo/',v1.home, name="home"),
    path('home/',v1.home2, name="home1"),
    path('nemo1/<str:name>/<int:id>/',v1.home1, name="home1"),
    path('registration/',v1.register,name="register"),
    path('login/',v1.login,name="login"),
    path('Employees/',include('Employees.urls')),
    path('counter/',v1.counter,name="counter"),
    path('about/',v1.about,name="about"),
    path('faculty/',v1.FacDataShow,name="facdatashow"),
    path('<int:id>/',v1.tables,name="tables"),
]
