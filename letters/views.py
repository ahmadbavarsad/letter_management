from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from .models import IncomingLetter, OutgoingLetter
from .forms import IncomingLetterForm, OutgoingLetterForm

def incoming_letter_list(request):
    letters = IncomingLetter.objects.all()
    return render(request, 'incoming_letter_list.html', {'letters': letters})

def incoming_letter_create(request):
    if request.method == 'POST':
        form = IncomingLetterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('incoming_letter_list')
    else:
        form = IncomingLetterForm()
    return render(request, 'incoming_letter_form.html', {'form': form})

def incoming_letter_download(request, pk):
    letter = get_object_or_404(IncomingLetter, pk=pk)
    return FileResponse(open(letter.document.path, 'rb'))

# Similar views for outgoing letters
def outgoing_letter_list(request):
    letters = OutgoingLetter.objects.all()
    return render(request, 'letters/outgoing_letter_list.html', {'letters': letters})

def outgoing_letter_create(request):
    if request.method == 'POST':
        form = OutgoingLetterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('outgoing_letter_list')
    else:
        form = OutgoingLetterForm()
    return render(request, 'letters/outgoing_letter_form.html', {'form': form})

def outgoing_letter_download(request, pk):
    letter = get_object_or_404(OutgoingLetter, pk=pk)
    return FileResponse(open(letter.document.path, 'rb'))

