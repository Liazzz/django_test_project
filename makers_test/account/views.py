from django.contrib.auth.models import User
from django.views.generic import CreateView

from makers_test.account.forms import RegistrationForm


class Regiterview(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'account/registration.html'
