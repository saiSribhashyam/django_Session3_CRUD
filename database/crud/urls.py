from django.urls import path
from .views import home,insert_emp,display_all,update_emp,delete_emp
urlpatterns = [
    path('',home,name="home"),
    path('insert/',insert_emp,name="create"),
    path('displayall/',display_all,name="retrieve_all"),
    path('update/<int:id>/',update_emp,name="update"),
    path('delete/<int:id>/',delete_emp,name="delete"),


]