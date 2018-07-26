from django.conf.urls import url, include

urlpatterns = [
    url(r'^time_display/', include('apps.time_display.urls')),

    url(r'^gold/', include('apps.gold.urls')),

    url(r'^random_word/', include('apps.random_word.urls')),

    url(r'^books/', include('apps.books.urls')),

    url(r'^blogs/', include('apps.blogs.urls')),

    url(r'^session_words/', include('apps.session_words.urls')),

    url(r'^amadon/', include('apps.amadon.urls')),
    
    url(r'^', include('apps.standard.urls')),
]
