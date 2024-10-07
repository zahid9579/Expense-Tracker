from django.urls import path
from testapp import views

urlpatterns = [
    path('', views.expense_list, name='expense_list'),
    path('create/', views.expense_create, name='expense_create'),
    path('<int:expense_id>/edit/', views.expense_edit, name='expense_edit'),
    path('<int:expense_id>/delete/', views.expense_delete, name='expense_delete'),
    path('register/', views.register, name='register',)

    # path('', views.index, name='index'),
]
