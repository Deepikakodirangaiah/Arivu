from django.shortcuts import render, redirect
from .models import SpiritualTalk
from .forms import SpiritualTalkForm

def spiritual_talks(request):
    talks = SpiritualTalk.objects.all().order_by('-date')
    form = SpiritualTalkForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('spiritual_talks')  # Redirect to clear form

    return render(request, 'spiritual_talks.html', {
        'talks': talks,
        'form': form,
    })