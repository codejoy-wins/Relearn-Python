from django.conf.urls import url, include

urlpatterns = [
    url(r'^time_display/', include('apps.time_display.urls')),

    url(r'^gold/', include('apps.gold.urls')),

    url(r'^random_word/', include('apps.random_word.urls')),

    url(r'^books/', include('apps.books.urls')),

    url(r'^blogs/', include('apps.blogs.urls')),

    url(r'^session_words/', include('apps.session_words.urls')),

    url(r'^amadon/', include('apps.amadon.urls')),

    url(r'user_login/', include('apps.user_login.urls')),

    url(r'dojo_ninjas/', include('apps.dojo_ninjas.urls')),

    url(r'book_authors/', include('apps.book_authors.urls')),

    url(r'like_books/', include('apps.like_books.urls')),

    url(r'semi_restful/', include('apps.semi_restful.urls')),
    
    url(r'^', include('apps.standard.urls')),
]