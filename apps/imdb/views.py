from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from bootstrap_datepicker_plus.widgets import DatePickerInput

from apps.imdb.models import Movie


class MovieListView(ListView):
    model = Movie

