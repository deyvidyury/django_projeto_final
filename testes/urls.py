from django.conf.urls import url
from testes import views

urlpatterns = [
	url(r'^$', views.index)
]