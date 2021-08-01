from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, ListView
from pesados_el_norte.core_app.models.receipt import Receipt


# User = get_user_model()


class CajaListView(LoginRequiredMixin, ListView):
    model = Receipt
    queryset = Receipt.objects.all()


caja_list_view = CajaListView.as_view()
