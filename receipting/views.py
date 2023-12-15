from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from .models import Receipt
from .forms import RegisterationForm, ReceiptForm, ReceiptUpdateForm

# Create your views here.

def signup(request):
    if request.method == 'POST':                    
        form = RegisterationForm(request.POST)      #get post method parameteres and check if valid
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created!')
            return redirect('login')
        
    else:       
        form = RegisterationForm() 
    return render (request ,'receipting/signup.html',{'form':form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)    # authenticate function verifies if user credentials are correct then it returns a user object
        if user is not None:
            login(request, user)        #Logs in authenticated user      
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        return render(request, 'receipting/login.html')

def logout_user(request):
     logout(request)                   # Remove session data and user 
     return redirect('login')

def home(request):
    if not request.user.is_authenticated:
     return redirect('login')
    else:
     return render (request, 'receipting/home.html')
    
def receipts(request):
    receipts = Receipt.objects.filter(user=request.user)     #receipts list that the user created
    return render (request, 'receipting/receipts.html',{'receipts':receipts})

def newReceipt(request):                    # new receipt function 
    if request.method == 'POST':
         form = ReceiptForm(request.POST)
         if form.is_valid():
            form.instance.user = request.user           # create authenticated user instance for receipt object
            form.save()
            messages.success(request, f'A new receipt has been added')
            return redirect('receipts')
    else:
        form = ReceiptForm()
    return render (request, 'receipting/newReceipt.html',{'form':form})

def detailsReceipt(request,pk):
    receipt = Receipt.objects.get(id=pk)
    if request.user != receipt.user:          #if the receipt was not added by the logged in user then the user cant access this page
        return HttpResponseForbidden("You do not have permission to view this receipt.")
    return render(request,'receipting/detailsReceipt.html',{'receipt':receipt})

def updateReceipt(request,pk):
    receipt = Receipt.objects.get(id=pk)
    if request.user != receipt.user:                #same as previous one but for update page
        return HttpResponseForbidden("You do not have permission to update this receipt.")
    if request.method == 'POST':
         form = ReceiptUpdateForm(request.POST, instance=receipt)
         if form.is_valid(): 
            form.instance.user = request.user        
            form.save()
            messages.success(request, f'Your receipt has been updated')
            return redirect('receipts')
    else:
        form = ReceiptUpdateForm(instance=receipt, initial={     #setting default values for inputs 
            'store_name': receipt.store_name,
            'date': receipt.date,
            'item_list': receipt.item_list,
            'total': receipt.total,
        })
    return render(request,'receipting/updateReceipt.html',{'form':form})

def deleteReceipt(request,pk):
    receipt = Receipt.objects.get(id=pk)
    if request.user != receipt.user:                #same as previous one but for delete
        return HttpResponseForbidden("You do not have permission to update this receipt.") 
    if request.method == 'POST':
         receipt.delete()
         return redirect('receipts') 
    return render(request, 'receipting/deleteReceipt.html', {'receipt': receipt})


