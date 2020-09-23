from django.urls import path
from Employees import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('displaydata/',views.displaydata,name="displaydata"),
    path('delete/<str:id>',views.delete,name="delete"),
    path('edit/<str:id>',views.edit,name="edit"),
    path('update/<str:id>',views.update,name="update")
]