from django.urls import path
from .views import (
    company_list,
    company_detail,
    VacancyListAPIView,
    VacancyDetailAPIView,
    TopTenVacanciesAPIView,
    CompanyVacanciesAPIView
)

urlpatterns = [
    path('companies/', company_list),
    path('companies/<int:pk>/', company_detail),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:pk>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten/', TopTenVacanciesAPIView.as_view(), name='top-ten-vacancies'),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view(), name='company-vacancies'),

]