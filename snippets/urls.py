from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views

# Создайте маршрутизатор и зарегистрируйте в нем наши наборы представлений.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename="snippet")
router.register(r'users', views.UserViewSet, basename="user")
# URL-адреса API теперь автоматически определяются маршрутизатором.
urlpatterns = [
    path('', include(router.urls)),
]
