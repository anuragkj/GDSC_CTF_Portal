from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
	path('admin/add', views.addchallenges, name="add"),
	path('postflag/', views.flagsubmit, name="flagsubmit"),
	path('showhint/<str:pk>/', views.showHint, name="showhint"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 