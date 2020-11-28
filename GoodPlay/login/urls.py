from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index.html'),
    path('consolas/', views.consolas, name='consolas.html'),
    path('juegos/', views.juegos, name='juegos.html'),
    path('computacion/', views.computacion, name='computacion.html'),
    path('accesorio/', views.accesorio, name='accesorio.html'),
    path('juegos/<str:pk>',views.JuegoDetailView.as_view(), name='juegos-detail'),
    path('juego_list/', views.JuegoListView.as_view(), name='juego_list'),
    path('juego/<int:pk>', views.JuegoListView.as_view(), name='juego-detail'),
    path('compañia/<str:pk>',views.CompañiaDetailView.as_view(), name='compañia-detail'),
    path('compañia_list/', views.CompañiaListView.as_view(), name='compañia_list'),
    path('compañia/<int:pk>', views.CompañiaListView.as_view(), name='compañia-detail'),
    path('producto/<str:pk>',views.ProductoDetailView.as_view(), name='producto-detail'),
    path('producto_list/', views.ProductoListView.as_view(), name='producto_list'),
    path('producto/<int:pk>', views.ProductoListView.as_view(), name='producto-detail'),
    
            ]


urlpatterns+=[
    path('juegos/create/', views.JuegoCreate.as_view(), name='juego_create'),
    path('juegos/<str:pk>/update/', views.JuegoUpdate.as_view(), name='juego_update'),
    path('juegos/<str:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),
    path('compañia/create/', views.CompañiaCreate.as_view(), name='compañia_create'),
    path('compañia/<str:pk>/update/', views.CompañiaUpdate.as_view(), name='compañia_update'),
    path('compañia/<str:pk>/delete/', views.CompañiaDelete.as_view(), name='compañia_delete'),
    path('producto/create/', views.ProductoCreate.as_view(), name='producto_create'),
    path('producto/<str:pk>/update/', views.ProductoUpdate.as_view(), name='producto_update'),
    path('producto/<str:pk>/delete/', views.ProductoDelete.as_view(), name='producto_delete'),

]