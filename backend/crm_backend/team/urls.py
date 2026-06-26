from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, get_my_team, add_member, UserDetail, get_invite_code, join_team_by_code

router = DefaultRouter()
router.register('teams',TeamViewSet,basename='teams')

urlpatterns = [
    # Ruta personalizata este prima
    path('teams/member/<int:pk>', UserDetail.as_view(), name='userdetail'),
    path('teams/get_my_team/',get_my_team, name='get_my_team'),
    path('teams/add_member/',add_member, name='add_member'),
    path('teams/generate_invite_code/',get_invite_code,name='generate_invite_code'),
    path('teams/join_team_by_code/',join_team_by_code,name='join_team_by_code'),
    path('',include(router.urls)),

]