from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from django.http import HttpResponse

from .models import CustomUser, Product, Category


class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


class CustomUserLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('home')


class UserDetailView(LoginRequiredMixin, DetailView):

    model = CustomUser  # Replace with your custom user model
    template_name = 'user_profile.html'
    context_object_name = 'user'  # This is the name you'll use in the template to access the user object

    def get_object(self, queryset=None):
        return self.request.user  # Retrieve the currently logged-in user


class CustomUserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


class ProductListView(ListView):
    context_object_name= 'product_list'
    model=Product
    template_name = 'index.html'

    def get_context_data(self, **kwargs):


        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["product_list"] = Product.objects.all()

        context["category"] = Category.objects.all()
        return context





class ProductDetailsView(DetailView):
    context_object_name = 'product_details'
    model = Product
    template_name = 'product_details.html'

    # def get_queryset(self):
    #     return Product.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["product_details"] = Product.objects.get(id=self.kwargs['pk'])
    #
    #     context["category"] = Category.objects.get(id=self.kwargs['pk'])
    #     return context





