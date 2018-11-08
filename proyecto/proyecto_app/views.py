from django.shortcuts import render
from xmlrpc.client import ServerProxy
from django import forms
from .forms import sumaForm
# Create your views here.

#Llamada a procedimiento remoto, ejemplo simple
def rpcAdd(resquest,a,b):
    client = ServerProxy('http://localhost:8000/rpc/')
    result = client.add(a, b)
    return  render(resquest,'rpcAdd.html',{'result':result})
#vista para el formulario
def get_suma(request):
    #se establece el metodo de respuesta
    if request.method == 'POST':
        #se crea un objeto de sumaForm
        form = sumaForm(request.POST)
        #se verifica que el formulario sea valido
        if form.is_valid():
            #obtiene los datos ingresados por el formulario
            data1 = form.cleaned_data['a']
            data2 = form.cleaned_data['b']
            #Transforma los datos a Flotante
            a=float('0' + data1)
            b=float('0' + data2)
            #{'form':form,'mydata':data1}
            #Crea un objeto remoto
            client = ServerProxy('http://localhost:8000/rpc/')
            #obtiene el resultado de llamar al metodo add
            resulta = client.add(a, b)
            return render(request,'index.html',{'form':form,'resulta':resulta })
    else:
        form = sumaForm()
    arg={'form':form}
    return render(request,'index.html',arg)
