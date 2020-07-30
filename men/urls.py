from django.urls import path, include


from . import views

urlpatterns = [
    path('',views.man_list),
    path('<int:id>',views.man_detail)
]
