from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/<user>/<email>', views.createUser, name='createUser'),
    path('<user>', views.getEmail, name='getEmail'),
    path('<user>/edit/<new_email>', views.editEmail, name='editEmail'),
    path('<user>/delete/', views.deleteUser, name='deleteUser'),
]
