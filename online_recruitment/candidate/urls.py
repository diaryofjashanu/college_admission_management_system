from django.urls import path
from . import views

urlpatterns = [
    path("", views.landingPage, name="landingPage"),
    path("about/", views.aboutPage, name="aboutPage"),
    path("category/", views.categoryPage, name="categoryPage"),
    path("contact/", views.contactPage, name="contactPage"),
    path("jobdetail/<str:id>/", views.jobdetailPage, name="jobdetail"),
    path("joblist/", views.joblistPage, name="joblistPage"),
    path("testimonial/", views.testimonialPage, name="testimonialPage"),
    path("registration_form/", views.registrationform, name="registrationForm"),
    path("resume_upload/", views.resume_upload, name="resumeUpload"),
    path("dashboard/", views.dashboardPage, name="dashboardPage"),
    path("api/application_link/", views.applyJob, name="application_link"),
]
