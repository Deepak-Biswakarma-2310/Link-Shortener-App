from django.shortcuts import render, get_object_or_404, redirect
from .models import Link
from .forms import LinkForm  # Import the form
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def index(request):
    Links = Link.objects.all()
    context = {
        "links": Links  
    }
    return render(request, 'links/index.html', context)

def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    
    # Check if this is an AJAX request
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'clicks': link.clicks})
    
    return redirect(link.url)

def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New link has been created successfully!')
            return redirect('home')  # Redirect to home page after successful link creation
    else:
        form = LinkForm()

    return render(request, 'links/create.html', {'form': form})
