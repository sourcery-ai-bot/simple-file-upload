from django.shortcuts import render, redirect

from uploads.core.forms import DocumentForm
from uploads.core.models import Document


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', {'documents': documents})


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid() and form.files['document'].content_type == 'text/plain':
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {'form': form})
