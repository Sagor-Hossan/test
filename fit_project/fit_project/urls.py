
from django.contrib import admin
from django.urls import path
from fit_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signin, name='signin'),
    path('signin/', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
    path('home/', home, name='home'),
    path('profilepage/', profilepage, name='profilepage'),
    path('addFood/', addFood, name='addFood'),
    path('viewFood/', viewFood, name='viewFood'),
    path('deleteFood/<int:id>/', deleteFood, name='deleteFood'),
    path('editFood/<int:id>/', editFood, name='editFood'),

    path('viewConsumedCalories/', viewConsumedCalories, name='viewConsumedCalories'),
    path('addConsumedCalories/', addConsumedCalories, name='addConsumedCalories'),

    path('restaurantListPage/', restaurantListPage, name='restaurantListPage'),
    path('gymPage/', gymPage, name='gymPage'),
    path('exercisePage/', exercisePage, name='exercisePage'),
    path('restOrSleepPage/', restOrSleepPage, name='restOrSleepPage'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
