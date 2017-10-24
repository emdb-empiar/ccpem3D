from django.shortcuts import render 
from django.views.generic.edit import FormView
from django import forms

import os

class FileForm(forms.Form):
    vtp_file = forms.FileField(label="VTP File:")


def handle_uploaded_file(f):
    with open(os.path.join(os.path.dirname(__file__), 'static', 'view3D', 'images', f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class Index(FormView):
    form_class = FileForm
    template_name = 'view3D/index.html'
    success_url = '/'
    
    def form_valid(self, form):
        image_file = form.cleaned_data['vtp_file']
        handle_uploaded_file(image_file)
        context = self.get_context_data()
        context['form'] = form
        context['image_file'] = image_file.name
        return render(self.request, 'view3D/index.html', context)