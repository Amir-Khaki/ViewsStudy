from django.shortcuts import render
from django.views import generic
from .models import Person
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.shortcuts import redirect
from .forms import LoginForm
from django.urls import reverse_lazy, reverse


class HomeView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.order_by("-username")


class DetailView(generic.DetailView):
    model = User
    template_name = 'detail.html'
   

class DeleteView(generic.DeleteView):
    model = Person
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


class UpdataView(generic.UpdateView):
    model = User
    template_name = 'update.html'
    fields = ['username', 'email']
    # context_object_name = 'user'

    def get_success_url(self) -> str:
        return reverse('detail', args=[self.object.pk])


class SignUp(generic.CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'signup.html'
    # success_url = reverse_lazy('home')
    initial = {
        'username':'default-value-field'
        }
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_users'] = context.get('form')  
        return context
    
    def get_success_url(self) -> str:
        '''
        when use of this function that we want siwtch to e.x [detial-view]
        and send a 'pk' or 'id' for him.
        '''
        return reverse('detail', args=[self.object.pk])


class LoginView(View):

    def post(self,request):
        
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            messages.success(request, 'you was login on your account')
            return redirect('home')
        else:
            messages.success(request, 'There is a problem')
            return redirect('login')

    def get(self,request):
        form = LoginForm()
        context = {'form':form}
        return render(request, 'login.html', context=context)
