from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home (request):
    return HttpResponse("""<h1>Hey I am Django sserver.<h1>
                        <p> I am Django sserver.<p>
                        <hr>
                        <h1>Hey I am Django sserver.<h1>""")


def success (request):
    print("*" *10)
    return HttpResponse("<h1>Hey I am Django success.<h1>")
