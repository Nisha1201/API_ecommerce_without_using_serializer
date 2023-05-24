# from django.urls import path
# from .views import (
#     category_list, category_detail,
#     customer_list, customer_detail,
#     products_list, products_detail,
#     order_list, order_detail,
# )

# urlpatterns = [
#     # Category URLs
#     path('categories/', category_list, name='category-list'),
#     path('categories/<int:pk>/', category_detail, name='category-detail'),

#     # Customer URLs
#     path('customers/', customer_list, name='customer-list'),
#     path('customers/<int:pk>/', customer_detail, name='customer-detail'),

#     # Products URLs
#     path('products/', products_list, name='products-list'),
#     path('products/<int:pk>/', products_detail, name='products-detail'),

#     # Order URLs
#     path('orders/', order_list, name='order-list'),
#     path('orders/<int:pk>/', order_detail, name='order-detail'),
# ]



from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    CustomerListCreateAPIView,
    CustomerRetrieveUpdateDestroyAPIView,
    ProductsListCreateAPIView,
    ProductsRetrieveUpdateDestroyAPIView,
    OrderListCreateAPIView,
    OrderRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),

    # Customer URLs
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-detail'),

    # Product URLs
    path('products/', ProductsListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductsRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),

    # Order URLs
    path('orders/', OrderListCreateAPIView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order-detail'),
]