from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return render(request, "login/login.html")
"""
def registroUsuario(request):

    if request. method== 'POST':
        nombreUsuario=request.POST['nombreUsuanio']
        Email= request.POST[ ' correo']
        pwd= request.POST['password']
        nuevoUsuario(nombreUsuario=nombreUsuario, Email=Email, pwd=pwd).save()
        messages.success(request, 'Elusuario'+request.POST['nombreUsuario']+'se registro exitosamente')
        return render(request,'registro.html')

    else:
        return render (request,'registrarse. html')
def paginaLogin(request):
    if request.method==' POST':
        try:
            detalleUsuario=nuevoUsuario.objects.get(Email=request.POST['correo'],pwd=request.POST['password'])
            print("Usuario=",detalleUsuario)
            request.session['Email']=detalleUsuario.Email
            return render(request,'index.html')
        except nuevoUsuario.DoesNotExist as e:
            messages.success(request,'Nombre de usuario o Password no es correcto..!')
    return render (request,'login.html')

"""
def registro(request):
        return render(request, "login/registro.html")