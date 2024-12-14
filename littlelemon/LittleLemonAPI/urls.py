from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
  path('', views.index, name='home'),
  path('menu-items/', views.MenuItemsView.as_view(), name='menu'),
  path('menu-items/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
  path('message/', views.msg),
  path('api-token-auth/', obtain_auth_token),
  path('booking/', include(router.urls)),
]