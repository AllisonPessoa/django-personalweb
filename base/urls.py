from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path("home/", views.home, name="home"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("pub-full/", views.full_papers, name="pub-full"),
    path("pub-banners/", views.banners, name="pub-banners"),
    path("pub-oral/", views.oral_talks, name="pub-oral"),
    path("cv/", views.cv, name="cv"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
