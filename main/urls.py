from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet,GenderViewSet,ProductViewSet,CommentViewSet




router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet,basename='category')
router.register(r'gender',GenderViewSet,basename='gender')
router.register(r'products',ProductViewSet,basename='products')
router.register(r'comment',CommentViewSet,basename='comment')
urlpatterns = router.urls
