from django.shortcuts import render 
from django.views.generic.edit import FormView
from django import forms

import os


class FileForm(forms.Form):
    vtp_file = forms.FileField(label="VTP File:")
    pdb_file = forms.FileField(label="PDB File:", required=False)


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
        if form.cleaned_data['pdb_file']:
            model_file = form.cleaned_data['pdb_file']
            handle_uploaded_file(model_file)
            context['model_file'] = model_file.name
            if model_file.name.endswith('ent'):
                context['model_id'] = model_file.name.split('.ent')[0]
            elif model_file.name.endswith('pdb'):
                context['model_id'] = model_file.name.split('.pdb')[0]
        return render(self.request, 'view3D/index.html', context)