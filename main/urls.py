from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.home, name='home'),

    # Auth system
    path('accounts/login/',
         LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='auth/login.html'), name='logout'),

    # User management
    path('users-management/new/', views.createUser, name='createUser'),

    # Clinical analysis
    path('clinical-analysis/', views.clinicalAnalysis, name='clinicalAnalysis'),
    path('clinical-analysis/new/', views.newClinicalAnalysis,
         name='newClinicalAnalysis'),
    path('clinical-analysis/delete/<int:analysisId>/',
         views.deleteClinicalAnalysis, name="deleteAnalysis"),
    path('clinical-analysis/edit/<int:analysisId>',
         views.editClinicalAnalysis, name='editAnalysis'),

    # Pacients
    path('pacients/', views.pacients, name='pacients'),
    path('pacients/new/', views.newPacient, name='newPacient'),
    path('pacients/delete/<int:pacientId>/',
         views.deletePacient, name="deletePacient"),
    path('pacients/edit/<int:pacientId>',
         views.editPacient, name='editPacient'),

    # Results
    path('results/new/', views.newResult, name='newResult'),

    # Lab
    path('analysis-done/<int:analysisId>/',
         views.setAnalysisDone, name='analysisDone'),
]
