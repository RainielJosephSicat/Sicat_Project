from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .models import BreadProduct, BreadPost
from django.shortcuts import render, redirect
from .forms import CustomerMessageForm, CustomerInfoForm

class CustomerMessageView(FormView):
    template_name = 'message.html'
    success_url = '/'  # Redirect to home after successful submission

    def get(self, request, *args, **kwargs):
        customer_form = CustomerInfoForm()
        message_form = CustomerMessageForm()
        return self.render_to_response({
            'customer_form': customer_form,
            'message_form': message_form
        })

    def post(self, request, *args, **kwargs):
        customer_form = CustomerInfoForm(request.POST)
        message_form = CustomerMessageForm(request.POST)

        if customer_form.is_valid():
            customer = customer_form.save()
            if message_form.is_valid():
                message = message_form.save(commit=False)
                message.customer = customer
                message.save()
                return redirect(self.success_url)

        return self.render_to_response({
            'customer_form': customer_form,
            'message_form': message_form
        })

class ProductDetailView(DetailView):
    model = BreadProduct
    template_name = 'product_detail.html'
    context_object_name = 'product'

class BreadPostListView(ListView):
    model = BreadPost
    template_name = 'post.html'
    context_object_name = 'posts'

def home(request):
    products = BreadProduct.objects.all()
    posts = BreadPost.objects.all()
    return render(request, 'home.html', {'products': products, 'posts': posts})

class ProductListView(ListView):
    model = BreadProduct
    template_name = 'product.html'

class ProductCreateView(CreateView):
    model = BreadProduct
    fields = ['name', 'price', 'description', 'image', 'category']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = BreadProduct
    fields = ['name', 'price', 'description', 'image', 'category']
    template_name = 'product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = BreadProduct
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('product-list')
