from django.contrib import admin
from django.urls import path
from BigMacIndexes.views import home, table, graph, team, contact_us, calculator
from django.views.static import serve
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home),
    path("table/", table),
    path("graph/", graph),
    path("team/", team),
    path("contact_us/", contact_us),
    path("calculator/", calculator),
]

urlpatterns += staticfiles_urlpatterns()
