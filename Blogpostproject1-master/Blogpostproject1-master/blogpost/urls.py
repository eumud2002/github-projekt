from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from posts.views import Əsas, post, Haqqımda, search, postlist, allposts, Əlaqə

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Əsas, name = 'Əsas'),
    path('post/<slug>/', post, name = 'post'),
    path('Haqqımda/', Haqqımda,name = 'Haqqımda' ),
    path('Əlaqə/', Əlaqə,name = 'Əlaqə' ),
    path('search/', search, name = 'search'),
    path('postlist/<slug>/', postlist, name = 'postlist'), 
    path('posts/', allposts, name = 'allposts'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
