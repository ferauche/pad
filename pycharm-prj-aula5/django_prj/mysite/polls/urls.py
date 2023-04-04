from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'polls'
router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename="questions")

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', include(router.urls)),
]
