from django.conf.urls import url, patterns
from django.conf import settings



urlpatterns = patterns('',
    #user auth urls
    url(r'^$', 'album.views.home', name="index"),
    url(r'^registerUser/$', 'album.views.registerUser', name = "register"),
    url(r'^loginUser/$', 'album.views.loginUser', name = "login"),
    url(r'^profile/$', 'album.views.profile', name = "profile"),
    url(r'^profile/getAlbums/$', 'album.views.getAllAlbums', name = "getAlbums"),
    url(r'^profile/albumName/$', 'album.views.saveAlbumInfo', name = "albumName"),

    url(r'^profile/uploadImages/$', 'album.views.uploadImages', name = "upload"),
    url(r'^profile/getPhotoCount/$', 'album.views.getPhotoCount', name = "getPhoto"),
    url(r'^logout/$', 'album.views.logout', name = "logout"),
    url(r'^user_images/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        })
)