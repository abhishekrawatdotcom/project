from django.shortcuts import render
from app.models import Users,Games

# Create your views here.
def gamepro(request):
    return render(request,'index.html')


def searchmatch(query, item):
    if query in item.Game_name  :
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    prot = Games.objects.all()
    prod=[item for item in prot if searchmatch(query,item)]

    return render(request,'search.html',{'prod':prod})
