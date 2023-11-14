from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

"""
URL configuration for wishlist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Config requests to travel_wishlist dir's urls.py if req is not to admin page
    path('', include('travel_wishlist.urls'))
]


# If the app is running in local machine, then add on these media roots in addition. I think the settings.DEBUG is from debug==true, which would only be in dev mode.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
