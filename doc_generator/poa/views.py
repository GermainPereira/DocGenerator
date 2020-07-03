from django.shortcuts import render
from braces.views import SelectRelatedMixin
from django import forms
from django.views import generic
from . import models


# Create your views here.
class CreatePoA(generic.edit.CreateView):
    model = models.PoA
    fields = "__all__"

    redirect_field_name = 'blog/post_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.request.pk)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    # right idented

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()

        form = super(CreatePoA, self).get_form(form_class)
        form.fields['nome'].label = 'Nome'
        form.fields['nome'].widget = forms.TextInput(attrs={'placeholder': 'Digite o seu nome'})


        form.fields['sobrenome'].label = 'Sobrenome'
        form.fields['sobrenome'].widget = forms.TextInput(attrs={'placeholder': 'Digite o seu sobrenome'})
        return form


class DetailPoA(generic.TemplateView):
    template_name = 'poa/poa_detail.html'  # defines template

    def get_context_data(self, **kwargs):  # defines context
        context = super().get_context_data(**kwargs)
        poa_data = models.PoA.objects.get(pk=context["pk"])
        context['poa'] = poa_data
        print(context)

        return context
