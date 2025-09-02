from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home (request):
    # return HttpResponse("""<h1>Hey I am Django server.<h1>
    #                     <p> I am Django server.<p>
    #                     <hr>
    #                     <h2 style="color:red" >Hey I am Django sserver.<h2>""")
    return render(request,"index.html")


def success (request):
    print("*" *10)
    return HttpResponse("<h1>Hey I am Django success.<h1>")
