from django.urls import path, include


from . import views


urlpatterns = (
    # urls for Product
    path('',views.home_view,name='home'),
    path('product/allProducts', views.ProductListView.as_view(), name='Product_product_list'),
    path('product/detail/<slug:slug>/', views.ProductDetailView.as_view(), name='Product_product_detail'),
        path('product/product_search/', views.product_search, name='product_search'),


    # urls for order
    path('orders/', views.OrderListView.as_view(), name='Product_order_list'),
    path('order/conformed/', views.order_conform, name='Product_order_conform'),
    path('order/create/<slug:slug>', views.OrderCreateView.as_view(), name='Product_order_create'),
    path('order/detail/<slug:slug>/', views.OrderDetailView.as_view(), name='Product_order_detail'),

)

