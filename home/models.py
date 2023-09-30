# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Itsm-Platform(models.Model):

    #__Itsm-Platform_FIELDS__
    platform_name = models.CharField(max_length=255, null=True, blank=True)

    #__Itsm-Platform_FIELDS__END

    class Meta:
        verbose_name        = _("Itsm-Platform")
        verbose_name_plural = _("Itsm-Platform")


class Vendororg(models.Model):

    #__Vendororg_FIELDS__
    org_name = models.CharField(max_length=255, null=True, blank=True)

    #__Vendororg_FIELDS__END

    class Meta:
        verbose_name        = _("Vendororg")
        verbose_name_plural = _("Vendororg")


class Wllicense(models.Model):

    #__Wllicense_FIELDS__
    license_name = models.CharField(max_length=255, null=True, blank=True)
    license_id = models.CharField(max_length=255, null=True, blank=True)
    license_params = models.CharField(max_length=255, null=True, blank=True)

    #__Wllicense_FIELDS__END

    class Meta:
        verbose_name        = _("Wllicense")
        verbose_name_plural = _("Wllicense")


class Enduserorg(models.Model):

    #__Enduserorg_FIELDS__
    org_name = models.CharField(max_length=255, null=True, blank=True)

    #__Enduserorg_FIELDS__END

    class Meta:
        verbose_name        = _("Enduserorg")
        verbose_name_plural = _("Enduserorg")


class Enduser(models.Model):

    #__Enduser_FIELDS__
    user_full_name = models.CharField(max_length=255, null=True, blank=True)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_type = models.CharField(max_length=255, null=True, blank=True)
    user_role = models.CharField(max_length=255, null=True, blank=True)
    user_email = models.CharField(max_length=255, null=True, blank=True)

    #__Enduser_FIELDS__END

    class Meta:
        verbose_name        = _("Enduser")
        verbose_name_plural = _("Enduser")


class Endorgmetrics(models.Model):

    #__Endorgmetrics_FIELDS__

    #__Endorgmetrics_FIELDS__END

    class Meta:
        verbose_name        = _("Endorgmetrics")
        verbose_name_plural = _("Endorgmetrics")


class Incidents(models.Model):

    #__Incidents_FIELDS__
    incident = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    end_user_org = models.CharField(max_length=255, null=True, blank=True)
    incident_type = models.CharField(max_length=255, null=True, blank=True)

    #__Incidents_FIELDS__END

    class Meta:
        verbose_name        = _("Incidents")
        verbose_name_plural = _("Incidents")


class Wlwebhooks(models.Model):

    #__Wlwebhooks_FIELDS__
    webhook_name = models.CharField(max_length=255, null=True, blank=True)
    webhook_uri = models.CharField(max_length=255, null=True, blank=True)
    webhook_params_template = models.CharField(max_length=255, null=True, blank=True)
    webhook_expect_response = models.CharField(max_length=255, null=True, blank=True)

    #__Wlwebhooks_FIELDS__END

    class Meta:
        verbose_name        = _("Wlwebhooks")
        verbose_name_plural = _("Wlwebhooks")



#__MODELS__END
