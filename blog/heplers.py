from django.utils.text import slugify
import string
import secrets

def generate_random_string(N):
    res=''.join(secrets.SystemRandom().choices(string.ascii_uppercase+string.digits, k=N))
    return res

def generate_slug(text):
    from  .models import BlogModel
    new_slug=slugify(text)
    if BlogModel.objects.filter(slug=new_slug).first():
        return generate_slug(text+ generate_random_string(5))
    return new_slug
