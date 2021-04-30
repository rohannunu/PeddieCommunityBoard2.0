from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name="postDetail"),
    path('addPost/', views.AddPostView.as_view(), name="addPost"),
    path('post/edit/<int:pk>', views.EditPostView.as_view(), name="editPost"),
    path('post/<int:pk>/delete', views.DeletePostView.as_view(), name="deletePost"),
    path('addCategory/', views.AddCategoryView.as_view(), name="addCategory"),
    path('category/<str:cats>/', views.CategoryView, name="category"),
    path('category-list/',views.CategoryListView, name="categoryList"),
    path('like/<int:pk>', views.LikeView, name='likePost'),
    path('termsConditions/', views.termsConditionsView, name='termsConditions'), 
    path('aboutUs/', views.aboutView, name='about'),
    path('post/<int:pk>/comment', views.AddCommentView.as_view(), name='addComment'),


]