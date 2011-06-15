#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    
    seller_name = models.CharField(_("Name"), max_length=100, help_text=_("Your Name"))
    seller_email = models.EmailField(_("Email"), max_length=100, help_text=_("Your Email"))

    filename = models.CharField(_("Filename"), max_length=1000,
                                help_text=_("This is the name that appears as the descriptive name of your file."))
    download_url = models.URLField(_("Download URL"), verify_exists=False,
                                    help_text=_("Please enter the direct URL to the file you want to sell. "))

    tweet_body = models.TextField(_("Tweet Text"), max_length=500,
                                  help_text=_("Enter the text of the Tweet you want the people to post."))
    tweet_url = models.URLField(_("Tweet URL"), verify_exists=False,
                                help_text=_("Enter the URL that will be attached to every Tweet the people post."))

    def get_absolute_url(self):
        return '/product/%d/' %self.pk

    def get_pay_button_html(self):
        return "<a href=\"%s\">Buy With Tweet</a>" %(self.get_pay_url())
        
    def get_pay_url(self):
        current_site = Site.objects.get_current()
        return 'http://' + current_site.domain + self.get_absolute_url() + 'pay/'


    def __unicode__(self):
        return "<Product %s>" %self.pk

class PurchaseRecord(models.Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    price = models.CharField(max_length=1000)
    purchase_time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return "<PurchaseRecord product=%s user=%s>" %(self.product.pk, self.user.username)
