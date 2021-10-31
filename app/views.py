from django.shortcuts import render


async def index(request):
    return render(request, 'app/index.html')
