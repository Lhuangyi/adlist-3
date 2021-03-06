from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.AdListView.as_view()),
    path('ads',views.AdListView.as_view(), name = 'ads'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create',views.AdCreateView.as_view(success_url=reverse_lazy('ads')), name='ad_create'),
    path('ad/<int:pk>/update', views.AdUpdateView.as_view(success_url=reverse_lazy('ads')), name='ad_update'),
    path('ad/<int:pk>/delete', views.AdDeleteView.as_view(success_url=reverse_lazy('ads')), name='ad_delete'),

    #path('ad/create',views.AdFormView.as_view(success_url=reverse_lazy('ads')), name='ads_create'),
    #path('ad/<int:pk>/update',views.AdFormView.as_view(success_url=reverse_lazy('ads')), name='ad_update'),

    path('', views.AdListView.as_view(), name='menu_main'),
    path('page1', views.TheView.as_view(), name='menu_page1'),
    path('page2', views.TheView.as_view(), name='menu_page2'),
    path('page3', views.TheView.as_view(), name='menu_page3'),
    ##### picture
    path('ad_picture/<int:pk>', views.stream_file, name='ad_picture'),

    ##### comment
    path('ad/<int:pk>/comment',
         views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/delete',
         views.CommentDeleteView.as_view(success_url=reverse_lazy('ads')), name='comment_delete'),


    ##### favorite
    path('ad/<int:pk>/favorite', views.AddFavoriteView.as_view(), name='ad_favorite'),
    path('ad/<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='ad_unfavorite'),
]
