from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views
from . views import  index,about_View ,text_View,refund_View,quote_View,page_Temp_View,sucess_View,mybookings_View,thankyou_View,mypayments_View,locations_View,profile_View,booking_View,services_View,terms_View,privary_View,payment_View,contact_View

urlpatterns  = [
	path('', index.as_view(), name='index' ),
	# path('close',  TemplateView.as_view(template_name='close.html'), name='close' ),
	path('about', about_View.as_view(), name='about' ),
	path('profile', profile_View.as_view(), name='profile' ),
	path('locations', locations_View.as_view(), name='locations' ),
	path('mybookings', mybookings_View.as_view(), name='mybookings' ),
	path('mypayments', mypayments_View.as_view(), name='mypayments' ),
	path('testing123', text_View.as_view(), name='testing123' ),
	path('services', services_View.as_view(), name='services' ),
	path('contact', contact_View.as_view(), name='contact' ),
	path('terms', terms_View.as_view(), name='terms' ),
	path('privacy', privary_View.as_view(), name='privacy' ),
	path('refund', refund_View.as_view(), name='refund' ),
	path('quote/<str:Id>', quote_View.as_view(), name='quote/' ),
	path('payment', payment_View.as_view(), name='payment' ),
	path("chk_email/",views.checkemail,name = 'chk_email'),
	path("get_email/",views.getemailtoken,name = 'get_email'),
	path("post_register/",views.pregister_view,name = 'post_register'),
	path("post_login/",views.pLogin_view,name = 'post_login'),
	path("post_preset/",views.pReset_view,name = 'post_preset'),
	path('reset/<str:uidb64>/<str:token>', views.activate, name='reset'),
	path("post_forgot/",views.pForgot_view,name = 'post_forgot'),
	path("post_contact/",views.pContact_view,name = 'post_contact'),
	path('logout', views.logout_view , name='logout'),
	path('logoutsocial', views.logout_social , name='logoutsocial'),

	path('service/<str:Id>', views.service_View, name='service' ),
	path("servicelist/",views.serviceList_View,name = 'servicelist'),
	path("add_section/",views.addSection_view,name = 'add_section'),
	path("add_aboutservice/",views.addAboutServ_view,name = 'add_aboutservice'),
	path("add_Descservice/",views.addDescrServ_view,name = 'add_Descservice'),
	path("add_adonservservice/",views.addadonservServ_view,name = 'add_adonservservice'),
	path("add_offerservice/",views.addofferServ_view,name = 'add_offerservice'),
	path("add_choiceservice/",views.addchoicServ_view,name = 'add_choiceservice'),
	path("add_randchoice/",views.randChoice_view,name = 'add_randchoice'),
	path("add_hourrate/",views.add_hourrate_view,name = 'add_hourrate'),
	path("add_localservice/",views.addlocalServ_view,name = 'add_localservice'),
	path("add_internalservice/",views.addinternalServ_view,name = 'add_internalservice'),
	path("add_advanceservice/",views.addadvanceServ_view,name = 'add_advanceservice'),
	path("add_dateservice/",views.adddateServ_view,name = 'add_dateservice'),
	path("get_servsection/",views.getservSection,name = 'get_servsection'),
	path("get_aboutsection/",views.getaboutSection,name = 'get_aboutsection'),
	path("get_descsection/",views.getdescSection,name = 'get_descsection'),
	path("get_offersection/",views.getofferSection,name = 'get_offersection'),
	path("get_choicesection/",views.getchoiceSection,name = 'get_choicesection'),
	path("get_randomsection/",views.getRandomSection,name = 'get_randomsection'),
	path("get_hoursection/",views.get_hoursectionSection,name = 'get_hoursection'),
	path("get_addonsection/",views.getaddonSection,name = 'get_addonsection'),
	path("get_localaddrsection/",views.getLocaladdrSection,name = 'get_localaddrsection'),
	path("get_interaddrsection/",views.getInteraddrSection,name = 'get_interaddrsection'),
	path("get_servicesection/",views.getServiceSection,name = 'get_servicesection'),
	path("get_Datesection/",views.getDateSection,name = 'get_Datesection'),
	path("get_AppartList/",views.getApprtView,name = 'get_AppartList'),
	path("get_AppartcatList/",views.getApprtCatView,name = 'get_AppartcatList'),
	path("invoice_savePdf/",views.invoice_savePdf_View,name = 'invoice_savePdf'),
	path("invoice_sendPdf/",views.invoice_sendPdfView,name = 'invoice_sendPdf'),
	path("get_LocalAddressList/",views.getLocalAddressView,name = 'get_LocalAddressList'),
	path("get_InternAddressList/",views.getInternAddressView,name = 'get_InternAddressList'),
	path('service/<str:Id>/book-online/job-details', booking_View.as_view(), name='book-online' ),

	path("image_upload/",views.Imgupload_view,name = 'image_upload'),

	path("get_profile/",views.getuserDetails,name = 'get_profile'),
	path("update_profile/",views.profile_update_view,name = 'update_profile'),
	path("get_locations/",views.getlocationDetails,name = 'get_locations'),
	path("get_payments/",views.getpaymentDetails,name = 'get_payments'),
	path("get_bookings/",views.getbookingsDetails,name = 'get_bookings'),
	path("get_countrylist/",views.getcountries,name = 'get_countrylist'),
	path("add_address/",views.addaddresslist,name = 'add_address'),
	path("del_address/",views.deladdresslist,name = 'del_address'),
	path("update_address/",views.updateaddresslist,name = 'update_address'),
	path("create_paymentLink/",views.create_paylink,name = 'create_paymentLink'),
	path('payment/sucess/<str:Id>/', sucess_View.as_view(), name='sucess' ),
	path("webhooks/acme/fsferstrtr55677",views.webhook_endpoint,),
	path("check_payment/",views.checkpayment,name = 'check_payment'),
	path("booking_confirm/",views.booking_confirmview,name = 'booking_confirm'),
	path("cancel_booking/",views.cancel_bookingview,name = 'cancel_booking'),
	path('service/<str:Id>/book-online/confirmation/<str:Id1>/', thankyou_View.as_view(), name='book-online' ),
	]