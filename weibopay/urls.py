from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.views.generic.create_update import create_object
from django.views.generic.list_detail import object_detail
from django.conf import settings
from shop.models import Product

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:

    url(r'^$', direct_to_template,{'template': 'index.html'}, name='home'),
    url(r'^sell/$', create_object, 
        {'model' : Product, 'template_name' : 'sell.html', 'post_save_redirect' : '/product/%(id)s/'},
        name='sell'),
    url(r'^product/(?P<object_id>\d+)/$', object_detail,
        {'queryset' : Product.objects.all(), 'template_name': 'product.html'},
        name='product_detail'),

    url(r'^product/(?P<object_id>\d+)/pay/$', object_detail,
        {'queryset' : Product.objects.all(), 'template_name': 'pay.html'},
        name='pay'),
    #(r'^pay/(?P<object_id>\d+)/done/$', object_detail, {'template': 'pay_done.html',}),

    # (r'^weibopay/', include('weibopay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
