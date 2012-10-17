from django.db import models
import django.dispatch
from django.contrib.auth.hashers import check_password, make_password

"""Links a hashed IP address to a 2-character 'username' """
class Tweeter(models.Model):
    username = models.CharField(max_length=2, unique=True)
    ip = models.CharField(max_length=128, unique=True)

    class Meta:
        db_table = 'tweeters'
        verbose_name = 'Tweeter'
        verbose_name_plural = 'Tweeters'
    
    def __unicode__(self):
        return "%s [%s]" % (self.username, self.ip)

    def save(self, *args, **kwargs):
	    self.ip = make_password(self.ip, salt="0")
	    super(Tweeter, self).save(*args, **kwargs)
