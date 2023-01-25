from django.urls import path
from .views import UserRecordView, ArtistRecordView

app_name = 'api'
urlpatterns = [
    path('user/', UserRecordView.as_view(), name='users'),
    path('artist/', ArtistRecordView.as_view(), name='artists')
]
