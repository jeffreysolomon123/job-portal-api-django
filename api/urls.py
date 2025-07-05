from django.urls import path
from . import views

urlpatterns = [
    path('create-company/', views.create_company),
    path('post-job/', views.post_job),
    path('jobs/', views.list_jobs),
    path('apply/', views.apply_to_job),
    path('applicants/<int:job_id>/', views.get_applicants),
]
