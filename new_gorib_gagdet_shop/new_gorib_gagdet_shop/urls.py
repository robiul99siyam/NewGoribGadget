from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("cover/And/glass/",include("coverAndglass.urls")),
    path("camara/",include("cemera.urls")),
    path("loptob/And/desktop/",include("loptobAnddesktop.urls")),
    path("phone/And/tablet/",include("phoneAndtablet.urls")),
    path("power/And/accessorie",include("powerAndaccessories.urls")),
    path("smart/Watch/",include("smartWatch.urls")),
    path("sound/And/equipment/",include("soundAndequipment.urls")),
    path("blog/",include("blog.urls")),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
