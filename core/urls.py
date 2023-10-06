from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('category/',views.category,name='category'),
    path('category_question/<int:cat>',views.category_question,name="category_question"),
    path('submit_question/<int:cat>/<int:prodt>/',views.submit_question,name="submit_question"),
    path('result/',views.result,name="result"),
    path('certified/<int:cat>/',views.certified,name="certified"),
    path('not_certified/',views.not_certified,name='not_certified'),
    path('view_history/',views.view_history,name="view_history"),
    path('change_password/',views.change_password,name="change_password"),
   
    
    
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
