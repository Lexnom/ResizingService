from django.urls import path
from Download_file.views import mainSite, upload_file, rdrct, ImageView

urlpatterns = [

    path('', mainSite),
    path('api/',upload_file),
    path('info/',rdrct),
    path('api/<int:pk>', ImageView.as_view())
]