import random
from django.core.mail import send_mail
import string
from mail.models import EmailSet
from testing.settings import MAIN_ADR


def random_str(func):
    def mail(email, passw, old_email=None):
        url = func(email, passw, old_email=None)
        EmailSet.objects.create(email=email, url=url, passw=passw, old_email=old_email)
        send_mail(
        'Your confirmation on the Header',
        'To confirm your email click the link {}'.format(MAIN_ADR + 'confirm/' + url),
        'dsrepup@mail.ru',
        ['12dsender12@gmail.com']
        )
    return mail


@random_str
def send_confirmation(email, passw, old_email=None):
    str = ''.join(random.choice(string.ascii_letters) for i in range(12))
    return str

