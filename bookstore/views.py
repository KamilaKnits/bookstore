from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

# define a function view called login_view that takes a request
# from a user.
def login_view(request):
    error_message = None
    form = AuthenticationForm()

    # when user hits 'login' button, then POST reqeust is generated
    if request.method =='POST':

        # read the data sent by the form via POST request
        form = AuthenticationForm(data=request.POST)

        # check if form is valid
        if form.is_valid():
        
            username = form.cleaned_data.get('username') # read username
        
            password = form.cleaned_data.get('password') # read password

            # use Django authenticate function to validate the user
            user = authenticate(username=username, password=password)
        
            # if user is authenticated then use pre-definded Django function
            # to log in.
            if user is not None:
                login(request, user)
                return redirect('sales:records') # sends the user to desired page
            
        else:
            error_message = 'oops...something went wrong'
    
    # prepare data to send from view to template
    context ={
        'form': form,
        'error_message': error_message
    } 
    # load the login page using 'contect' information 
    return render(request, 'auth/login.html', context)  


# define a function view called logout_view that takes a request from user

def logout_view(request):
    logout(request) # the use pre-defined Django function to logout
    return redirect('login')  # after logging out go to login form    