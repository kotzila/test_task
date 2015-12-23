from django.forms import ValidationError
import urllib2


def validate_url(url):
    if not url.startswith('https'):
        raise ValidationError('Enter url that starts with https')
    try:
        response = urllib2.urlopen(url)
    except Exception:
        raise ValidationError('No answer from given url')
    else:
        if response.code != 200:
            raise ValidationError('No answer from given url')