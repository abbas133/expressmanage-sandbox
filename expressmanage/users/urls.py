from django.urls import path

from expressmanage.users.views import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
    # user_logout_view,
) 

app_name = "users"
urlpatterns = [
    path("", view=user_list_view, name="list"),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    # path("logout/", view=user_logout_view, name="logout"),
]