from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('media/', views.media_view, name='media'),
    path('give/', views.give_view, name='give'),
    path('kids/', views.kids_view, name='kids'),
    path('store/', views.store_view, name='store'),
    path('contact/', views.contact, name='contact'),
    path('what-to-expect/', views.what_to_expect_view, name='wte'),
    path('who-we-are/', views.who_we_are_view, name='wwa'),
    path('messages-u_/', views.msg1, name='msg01'),
    path('messages-_t/', views.msg2, name='msg02'),
    path('messages_/', views.msg3, name='msg03'),
    path('messages__/', views.msg4, name='msg04'),
    path('kids-messages-u_/', views.kids_msg1, name='kids1'),
    path('kids-messages-_t/', views.kids_msg2, name='kids2'),
    path('kids-messages_/', views.kids_msg3, name='kids3'),
    path('kids-messages__/', views.kids_msg4, name='kids4'),
    path('kids-messages-v_/', views.kids_stry1, name='kidstry1'),
    path('kids-messages-_a/', views.kids_stry2, name='kidstry2'),
    path('kids-messages_b/', views.kids_stry3, name='kidstry3'),
    path('kids-messages_c/', views.kids_stry4, name='kidstry4'),
    path('privacy/', views.privacy, name='privacy'),
    path('coming-soon/', views.coming_soon, name='cs'),
]
