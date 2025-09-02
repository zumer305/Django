from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home (request):
    # return HttpResponse("""<h1>Hey I am Django server.<h1>
    #                     <p> I am Django server.<p>
    #                     <hr>
    #                     <h2 style="color:red" >Hey I am Django sserver.<h2>""")
    peoples=[
       { 'name':'zumer', 'age':21},
       { 'name':'alishba', 'age':20},
       { 'name':'wahab', 'age':25},
       { 'name':'wahib', 'age':27},
       { 'name':'subhan', 'age':29},
    ]
    
    return render(request,"home/index.html",context={'peoples':peoples})



def success (request):
    print("*" *10)
    return HttpResponse("<h1>Hey I am Django success.<h1>")
