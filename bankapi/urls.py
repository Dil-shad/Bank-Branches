

from django.contrib import admin
from django.urls import path
from .views import BankDetailView,GetBranchDetails,AllBanksView
from .csv_importer import csv_importer

urlpatterns = [
  path('csv_importer',csv_importer,name="csv_importer"),
  path('bank/', BankDetailView.as_view(), name='bank-detail'), 
  path('Get-Branch-details/', GetBranchDetails.as_view(), name='Get-Branch-details'),
  path('all-Banks-View/', AllBanksView.as_view(), name='all-Banks-View'),
]
