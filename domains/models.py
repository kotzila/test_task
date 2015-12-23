from django.db import models
from domains.validators import validate_url


class Domain(models.Model):
    url = models.URLField(max_length=250, validators=[validate_url])

    def __unicode__(self):
        return self.url