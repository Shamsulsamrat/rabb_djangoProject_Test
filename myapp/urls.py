from django.urls import path
from .views import CustomUserCreateView, CustomUserLoginView, UserDetailView, CustomUserLogoutView,ProductListView,ProductDetailsView
# app_name = 'myapp'

urlpatterns = [
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    path('login/', CustomUserLoginView.as_view(), name='login'),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path('logout/', CustomUserLogoutView.as_view(), name='logout'),
    path('', ProductListView.as_view(), name='product_list'),
    path('product_details/<int:pk>/', ProductDetailsView.as_view(), name='product_details'),
]
