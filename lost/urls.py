from django.urls import path
from . import views

urlpatterns = [
    path('lost/', views.lost, name="lost"),

    path('lost_person/<int:id>/', views.lost_person_details, name='lost_person_details'),
    path('lost_item/<int:id>', views.lost_item_details, name='lost_item_details'),

    path('create_lost_person/', views.create_lost_person, name='create_lost_person'),
    path('create_lost_item/', views.create_lost_item, name='create_lost_item'),

    path('lost_person/<int:id>/update/', views.lost_person_update, name='lost_person_update'),
    path('lost_item/<int:id>/update/', views.lost_item_update, name='lost_item_update'),

    path('lost_person/<int:id>/delete', views.lost_person_delete, name='lost_person_delete'),
    path('lost_item/<int:id>/delete', views.lost_item_delete, name='lost_item_delete'),

]