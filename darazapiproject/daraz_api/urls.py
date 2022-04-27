from django.urls import path
from . import views
urlpatterns = [
    path("create",views.ProductCreateAPIView.as_view(),name="create"),
    path("list",views.ProductListAPIView.as_view(),name="list"),
    path("det/<int:pk>",views.ProductDetailAPIView.as_view(),name="detail")
]