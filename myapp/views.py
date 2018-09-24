from django.shortcuts import render
from myapp.forms import MyForm
def index(request):
    return render(request,'index.html')

def userForm(request):
    form = MyForm()
    return render(request,'form.html',{'uform':MyForm})
