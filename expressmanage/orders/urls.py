from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [

# INWARD ORDERS
# ------------------------------------------------------------------------------
    # ex: /orders/in/
    path('in/', views.InwardOrder_IndexView.as_view(), name='in_index'),

    # ex: /orders/in/1/
    path('in/<int:pk>/', views.InwardOrder_DetailView.as_view(), name='in_detail'),

    # ex: /orders/in/new
    path('in/new', views.InwardOrder_CreateView.as_view(), name='in_create'),

    # ex: /orders/in/e/5/
    path('in/e/<int:pk>/', views.InwardOrder_UpdateView.as_view(), name='in_update'),

    # ex: /orders/in/d/5/
    path('in/d/<int:pk>/', views.InwardOrder_DeleteView.as_view(), name='in_delete'),

# OUTWARD ORDERS
# ------------------------------------------------------------------------------
    # ex: /orders/out/
    path('out/', views.OutwardOrder_IndexView.as_view(), name='out_index'),

    # ex: /orders/out/1/
    path('out/<int:pk>/', views.OutwardOrder_DetailView.as_view(), name='out_detail'),

    # ex: /orders/out/new
    path('out/new', views.OutwardOrder_CreateView.as_view(), name='out_create'),


# AJAX HELPER URLS
# ------------------------------------------------------------------------------
    path('ajax/load-inward-orders/', views.load_customer_in_orders, name='load_inward_orders'),
    path('ajax/load-order-olis/', views.load_order_olis, name='load_order_olis'),


# NOT TO BE USED ON UI
# ------------------------------------------------------------------------------
    # ex: /orders/
    # path('', views.Order_IndexView.as_view(), name='order_index'),
    # ex: /order/in/oli
    path('in/oli', views.InOli_IndexView.as_view(), name='in_oli_index'),

    # ex: /order/in/oli/1/
    path('in/oli/<int:pk>/', views.InOli_DetailView.as_view(), name='in_oli_detail'),

    # ex: /order/out/oli
    path('out/oli', views.OutOli_IndexView.as_view(), name='out_oli_index'),

    # ex: /order/out/oli/1/
    path('out/oli/<int:pk>/', views.OutOli_DetailView.as_view(), name='out_oli_detail'),
]