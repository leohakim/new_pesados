from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# from pesados_el_norte.users.views import (
#     user_detail_view,
#     user_redirect_view,
#     user_update_view,
# )

app_name = "core"
urlpatterns = [
    path(
        "home/",
        login_required(TemplateView.as_view(template_name="core/home.html")),
        name="home",
    )
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
