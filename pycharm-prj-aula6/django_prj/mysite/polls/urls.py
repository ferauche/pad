from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

app_name = 'polls'
router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename="questions")

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('', include(router.urls)),
    path('api/token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
