from django.urls import path
from home.views import LandingView, HomeView, ResultView, DownloadPDFView, SearchView, DownloadCSVView

urlpatterns = [
    path("", LandingView.as_view(), name='landing'),
    path("home", HomeView.as_view(), name='home'),
    path("result", ResultView.as_view(), name='result'),
    path('download-pdf/', DownloadPDFView.as_view(), name='download_pdf'),
    path("search", SearchView.as_view(), name='search'),
    path('download-CSV/', DownloadCSVView.as_view(), name='download_CSV'),
]
