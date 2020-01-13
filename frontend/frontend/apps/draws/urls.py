from django.urls import path

from . import views
app_name = 'draws'
urlpatterns = [
    # path('draw/', views.draw, name = 'draw'),
    path('', views.index, name='index'),
    path('<int:draw_id>', views.detail, name='detail'),


]