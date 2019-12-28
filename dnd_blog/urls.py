from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from accounts import urls as accounts_urls
from blog import urls as blog_urls
from blog.views import post_list
from database import urls as database_urls
from tips import urls as tips_urls
from tools import urls as tools_urls

from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', post_list, name='index'),
    url(r'^blog/', include(blog_urls)),
    url(r'^database/', include(database_urls)),
    url(r'^tips/', include(tips_urls)),
    url(r'^tools/', include(tools_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^user/', include(accounts_urls)),
    url(r'^accounts/', include(accounts_urls)),
]
