from django.urls import path

from dashboard.views import (stock_create_view,
    portfolio_view,
    stock_list_view,
    
    single_stock_details,
    )      #render_initial_data, list_view_with_avg_bp, 
    #stock_detail_view, dynamic_lookup_view,


app_name = 'dashboard'
urlpatterns = [
    # path('stock/',stock_detail_view),    
    path('create/', stock_create_view, name='stock_create_view'),
    path('',portfolio_view, name='portfolio'),
    # path('',list_view_with_avg_bp, name='portfolio'),
    path('stocks/',stock_list_view, name='stock_list_view'),
    # path('stocks/<int:my_id>/',dynamic_lookup_view, name='stock'),
    path('stocks/<slug:my_name>/',single_stock_details, name='stock'),

    # path('initial/',render_initial_data),
]