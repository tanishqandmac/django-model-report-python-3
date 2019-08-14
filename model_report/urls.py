from django.urls import path
from model_report.views import report, report_list


urlpatterns = [
    path('', report_list, name='model_report_list'),
    path('<slug>/', report, name='model_report_view'),
]
