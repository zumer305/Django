from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home (request):
    # return HttpResponse("""<h1>Hey I am Django server.<h1>
    #                     <p> I am Django server.<p>
    #                     <hr>
    #                     <h2 style="color:red" >Hey I am Django sserver.<h2>""")
    peoples=[
       { 'name':'zumer', 'age':16},
       { 'name':'alishba', 'age':17},
       { 'name':'wahab', 'age':25},
       { 'name':'wahib', 'age':27},
       { 'name':'subhan', 'age':29},
    ]
    vegetabales=['banana','orange','apple']
    text=""" The Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus ullam possimus alias quibusdam eos! Nisi veniam qui, officiis, distinctio explicabo rerum omnis suscipit magnam voluptatum excepturi dolore illo vero fugiat molestias. Accusantium excepturi, ducimus esse blanditiis beatae ab eos cum error repellat obcaecati quibusdam exercitationem debitis molestiae. Molestiae, laborum vero."""

    
    return render(request,"home/index.html",context={'page':'Django tutorial','peoples':peoples,'text':text,'vegetables':vegetabales })

def about(request):
    context = {'page': 'about'}
    return render(request, "home/about.html", context)



def contact (request):
 context={'page':'contact'}
 return render(request,"home/contact.html",context)

# def success (request):
#     print("*" *10)
#     return HttpResponse("<h1>Hey I am Django success.<h1>")
