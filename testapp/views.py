from django.shortcuts import render, get_object_or_404, redirect
from .models import ExpenseModel
from .forms import ExpenseForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.
def index(request):
    return render(request, 'index.html')

def expense_list(request):
    expenses = ExpenseModel.objects.all()
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expense_form.html', {'form': form})

@login_required
def expense_edit(request, expense_id):
    expense = get_object_or_404(ExpenseModel, pk=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expense_form.html', {'form': form})
    
    
@login_required 
def expense_delete(request, expense_id):
    expense = get_object_or_404(ExpenseModel, pk=expense_id, user = request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'registration/expense_confirm_delete.html', {'expense': expense})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form':form})
        
        
    
    
    

# Check if the expense with id=1 exists
expense = ExpenseModel.objects.filter(pk=1)
print(expense.exists())  # True if the expense exists, otherwise False


expense = ExpenseModel.objects.get(pk=1)
print(expense.user)  # This will print the user associated with the expense
