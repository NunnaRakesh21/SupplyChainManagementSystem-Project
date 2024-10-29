from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.indexfunction,name="index"),

    path("registration",views.registration,name="registration"),
    path("login",views.login,name="login"),
    path("checkuserlogin",views.checkuserlogin,name="checkuserlogin"),
    path("home",views.home,name="home"),
    path("services", views.services, name="services"),
    path("about", views.about, name="about"),
    path('logout',views.logout,name='logout'),
    path('product_list',views.product_list,name='product_list'),
    path('add_product',views.add_product,name='add_product'),
    path('customer_list',views.customer_list,name='customer_list'),
    path('order_create',views.order_create,name='order_create'),
    path('order_list',views.order_list,name='order_list'),
    path('base',views.basic,name='base'),
    path('',views.basic,name='base'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('checkadminlogin',views.checkadminlogin,name="checkadminlogin"),
    path('adminlogout',views.adminlogout,name='adminlogout'),
    path('createsupplier',views.createsupplier,name='createsupplier'),
    path('supplierlogin',views.supplierlogin,name='supplierlogin'),
    path("supplieruserlogin",views.supplieruserlogin,name="supplieruserlogin"),
    path('supplierlogout',views.supplierlogout,name='supplierlogout'),
    path("deletecustomer/<int:uid>",views.deletecustomer,name="deletecustomer"),
    path('createseller',views.createseller,name="createseller")
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)