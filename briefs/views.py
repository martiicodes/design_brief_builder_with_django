from django.shortcuts import render, redirect
from .forms import DesignBriefForm

def create_brief(request):
    if request.method == 'POST':
        form = DesignBriefForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('briefs:success')
    else:
        form = DesignBriefForm()
    return render(request, 'briefs/create_brief.html', {'form': form})

def success(request):
    return render(request, 'briefs/success.html')

