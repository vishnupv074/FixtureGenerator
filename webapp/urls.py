from django.urls import path
from . import views


urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.registartion, name='registration'),  # url for registration
    path('team/<int:id>', views.team_view, name='team_view'),  # Url for viewing the teams
    path('schedule', views.schedule_view, name='schedule'),  # Url for the fixture
    path('login', views.login_view, name='login'),  # Url for login
    path('admin_panel', views.admin_panel, name='admin_panel'),  # Url to the admin panel, login required
    path('match_edit/<int:id>', views.match_edit, name='match-edit'),  # Url to match edit page, login required
    path('logout', views.logout_view, name='logout_view'),  # Url for logout admin
]