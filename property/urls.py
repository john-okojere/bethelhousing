from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="property-home" ),
    path('location', views.address, name="address-property" ),
    path('location/info/<int:pk>', views.address_info, name="address-property-info" ),
    path('submit', views.SubmitProperty, name="submit" ),
    path('detail/<uuid:uid>', views.detail, name="property-view" ),
    path('upload/<uuid:uid>', views.file_upload_view, name="upload-view"),
    path('submitBasicInfo/<uuid:uid>', views.SubmitBasicInfo, name="submitBasic" ),
    path('submitLocationInfo/<uuid:uid>', views.SubmitLocationInfo, name="submitLocation" ),
    path('submitDetailedInfo/<uuid:uid>', views.SubmitDetailedInfo, name="submitDetail" ),
    path('submitContactInfo/<uuid:uid>', views.SubmitContactInfo, name="submitContact" ),
    path('submitreview/<uuid:uid>', views.fivestarreview, name="submitreview" ),
    
    path('addComment/<uuid:uid>', views.addcomment, name="addcomment" ),
    path('MessageCustomerCare/<uuid:uid>', views.MessageCustomerCare, name="messagecustomercare" ),

    path('delete_home/<uuid:uid>', views.delete_property_and_go_home, name="delete_home_property" ),
    path('delete_add/<uuid:uid>', views.delete_property_and_add_another, name="delete_add_property" ),
    
    path('approved_add/<uuid:uid>', views.approve_property_and_add_again, name="approved_add_property" ),
    path('approved_home/<uuid:uid>', views.approve_property_and_go_home, name="approved_add_home" ),
]
