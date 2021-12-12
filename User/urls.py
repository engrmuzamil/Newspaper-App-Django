from django.urls import reverse, path
from .views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup')
]
