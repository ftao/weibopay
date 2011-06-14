# Create your views here.
from django.http import HttpResponseNotFound,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from eze_auth.helper import get_api_client
from eze_auth.models import EzeUserProfile

from weibopay.shop.models import Product,PurchaseRecord
from weibopay.shop.forms import PostWeiboForm

def pay(request, product_id, template_name = 'pay.html'):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound('product not found')

    after_login = reverse('do_pay', kwargs={'product_id' : product_id})
    context = {'product' : product , 'login_redirect' : after_login}

    return render_to_response(template_name, 
        context, 
        context_instance = RequestContext(request),
    )

def do_pay(request, product_id, template_name = 'do_pay.html'):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('pay', kwargs={'product_id' : product_id}))
        
    try:
        identity = EzeUserProfile.objects.get(user=request.user)
    except EzeUserProfile.DoesNotExist:
        return HttpResponseRedirect(reverse('pay', kwargs={'product_id' : product_id}))

    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponseNotFound('product not found')

    if request.method == 'POST':
        form = PostWeiboForm(request.POST)
        if form.is_valid():
            eze_api_client = get_api_client()
            message = form.cleaned_data['message'] + '  ' + product.tweet_url
            eze_api_client.update_status(identity.identity, message)
            PurchaseRecord.objects.create(product=product, user=request.user, price=message)
            return HttpResponseRedirect(product.download_url)
                
            #return HttpResponseRedirect(reserve('pay_done', kwargs={'product_id' : product_id}))
    else:        
        form = PostWeiboForm({'message' : product.tweet_body})
    context = {'product' : product, 'identity' : identity, 'form' : form}

    return render_to_response(template_name, 
        context, 
        context_instance = RequestContext(request),
    )
