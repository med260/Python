from  django.urls import path 
from . import views # from . means the current directory 

urlpatterns = [ 
    path("", views.index , name= "index" ),
    path("salah", views.salah , name= "salah" ),
    path("<str:name>" , views.greet , name ="greeting" )
]
