from django.urls import path
from .views import ArticleAPIDetails, ArticleAPIView, GenericAPIView 
urlpatterns = [
    #path('article/', article_list),
    #path('detail/<int:pk>', article_detail),
    path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>', ArticleAPIDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),

]
