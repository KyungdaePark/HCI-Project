from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('detect', views.detect, name='detect'),
    path('english-study', views.english_study, name='english_study'),
    path('draw', views.draw, name='draw'),
    path('quiz', views.quiz, name='quiz'),
    path('game', views.game, name='game'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
