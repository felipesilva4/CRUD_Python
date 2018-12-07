from django.urls import path
from .views import AlunosCreate
from .views import AlunosList
from .views import AlunosDetail
from .views import AlunosUpdate
from .views import AlunosDelete



urlpatterns = [
    path ('create/',AlunosCreate.as_view(),name = 'alunos_create' ),
    path ('list/', AlunosList.as_view(), name = 'alunos_list' ),
    path ('detail/<int:pk>/', AlunosDetail.as_view(), name = 'alunos_detail' ),
    path ('update/<int:pk>/', AlunosUpdate.as_view(), name = 'alunos_update'),
    path ('delete/<int:pk>/', AlunosDelete.as_view(), name = 'alunos_delete'),
]