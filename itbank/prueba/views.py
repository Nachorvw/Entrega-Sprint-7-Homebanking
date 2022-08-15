from django.shortcuts import render, HttpResponse

# Create your views here.
def prueba(request):
    html_response=('<h1>Bienvenidos a mi primer sitio de purebas con django</h1>')
    for i in range(10):
        html_response+="<p>Linea "+ str(i)+"</P>"
    return HttpResponse(html_response)

def login(request):
    return render(request, "prueba/login.html")

