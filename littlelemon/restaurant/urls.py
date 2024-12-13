from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
  path('', views.index, name='home'),
  path('menu/', views.MenuItemsView.as_view(), name='menu'),
  path('menu-item/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
  path('booking/', include(router.urls)),
]