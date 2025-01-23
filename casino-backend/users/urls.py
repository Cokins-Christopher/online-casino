from django.urls import path
from .views import RegisterUserView, LoginUserView

urlpatterns = [
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('login/', LoginUserView.as_view(), name='login'),
]
