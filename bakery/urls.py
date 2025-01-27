from django.urls import path
from . import views
from .views import CustomerMessageView, MessageListView, MessageUpdateView, MessageDeleteView

urlpatterns = [
    path('', views.home, name='home'),
    path('messages/', MessageListView.as_view(), name='message-list'),
    path('messages/<int:pk>/edit/', MessageUpdateView.as_view(), name='message-edit'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message-delete'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/new/', views.ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('posts/', views.BreadPostListView.as_view(), name='post-list'),
    path('message/', CustomerMessageView.as_view(), name='message'),
]
