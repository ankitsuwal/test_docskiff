from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product


class Browse(LoginRequiredMixin, ListView):
    template_name = 'product/index.html'
    paginate_by = 25

    def get_queryset(self):
        queryset = Product.objects.filter(user=self.request.user)
        return queryset
