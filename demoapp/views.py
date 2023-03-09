from django.shortcuts import render

# Create your views here.
def dis(request):
    return render(request, 'Demoapp/abc.html')