from django.urls import path
from Tollywood import views
urlpatterns=[
	path('',views.index,name="index"),
	path('register/',views.register,name="register"),
	path('showdata/',views.showdata,name="showdata"),
	path('edit/<int:id>',views.edit,name='edit'),
	path('edit2/<int:id>',views.edit2,name='edit2'),
	path('delete/<int:id>',views.delete,name='delete'),
	path('contact/',views.contact,name='contact'),
]