from django.urls import path
from .views import articleview, detailview, updateview,deleteview, createview
urlpatterns = [
    path('', articleview.as_view(), name='articleview'),
    path('delete/<int:pk>', deleteview.as_view(), name='delete'),
    path('update/<int:pk>', updateview.as_view(), name='update'),
    path('detail/<int:pk>', detailview.as_view(), name='detail'),
    path('new/', createview.as_view(), name='new')
]
