from django.urls import path
from .views import HomepageView, AboutpageView, FooterpageView

urlpatterns = [
    path('', HomepageView.as_view(), name='home'),
    path('about/', AboutpageView.as_view(), name='about'),
path('footer/', FooterpageView.as_view(), name='footer'),
]