from django.urls import path
from .views import TecherAllView, TecherDetailView, TecherCreateView, TecherUpdateView, TecherDeleteView    

urlpatterns = [
    path('teachers/', TecherAllView.as_view()),
    path('teachers/<int:id>/', TecherDetailView.as_view()),
    path('teachers/create/', TecherCreateView.as_view()),
    path('teachers/<int:id>/update/', TecherUpdateView.as_view()),
    path('teachers/<int:id>/delete/', TecherDeleteView.as_view()),
]