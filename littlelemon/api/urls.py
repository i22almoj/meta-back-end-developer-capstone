from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('menu-items/', views.MenuItemsView.as_view(), name='menu'),
  path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-detail'),
  path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('bookings/', views.BookingView.as_view(), name='bookings'),
  path('bookings/<int:pk>', views.SingleBookingView.as_view(), name='booking-detail'),
  path('bookings/<int:pk>/', views.SingleBookingView.as_view(), name='booking-detail'),
  path('message/', views.msg),
  path('api-token-auth/', obtain_auth_token),
]