from django.shortcuts import render
from webapp import forms
from django.http import HttpResponseRedirect

# Create your views here.
def ThankView(request):
    return render(request,'myapp/THANKYOU.html')

def EmpView(request):
    if request.method=='POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            print("Welcome to Validations")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])
            print(form.cleaned_data['Opinion'])
            return HttpResponseRedirect('/Bye')
    else:
        form = forms.EmpForm()
    return render(request,'myapp/welcome.html', {'form': form})

# Create your views here.
