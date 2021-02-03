from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'Customer/main.html')

def notif(request):
    return render(request, 'Customer/notif.html')

def graph(request):
    return render(request, 'Customer/graph.html')

def model(request):
    return render(request, 'Customer/model.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            Customer.objects.create(
                user=user,name = user.username, phone = None, email = user.email
            )
            messages.success(request, 'Account was created for ' + user.username)
            return redirect('/login')
    context = {'form':form}
    return render(request, 'Customer/register.html', context)
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'Customer/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'Customer/user_settings.html', context)
