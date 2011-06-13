#coding=utf8
from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Product(models.Model):
    
    seller_name = models.CharField("Name", max_length=100, help_text="Your Name")
    seller_email = models.EmailField("Email", max_length=100, help_text="Your Email")

    filename = models.CharField("Filename", max_length=1000,
                                help_text="This is the name that appears as the descriptive name of your file.")
    download_url = models.URLField("Download URL", verify_exists=False,
                                    help_text="Please enter the direct URL to the file you want to sell. ")

    tweet_body = models.TextField("Tweet Text", max_length=500,
                                  help_text="Enter the text of the Tweet you want the people to post.")
    tweet_url = models.URLField("Tweet URL", verify_exists=False,
                                help_text="Enter the URL that will be attached to every Tweet the people post.")

    def get_absolute_url(self):
        return '/product/%d/' %self.pk

    def get_pay_button_html(self):
        return "<a href=\"%s\">Buy With Tweet</a>" %(self.get_pay_url())
        
    def get_pay_url(self):
        current_site = Site.objects.get_current()
        return 'http://' + current_site.domain + self.get_absolute_url() + 'pay/'


class PurchaseRecord(models.Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(User)
    price = models.CharField(max_length=1000)
    purchase_time = models.DateTimeField(auto_now_add=True)
    

