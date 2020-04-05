import random
from django.core.mail import send_mail
import string
from mail.models import EmailSet
from testing.settings import MAIN_ADR

"""
    send_mail(
        'Your confirmation on the Header',
        'To confirm your email click the link {}'.format(url),
        'dsrepup@mail.ru',
        ['{}'.format(mail)]
    )
"""


def random_str(func):
    def mail(email, passw):
        url = func(email, passw)
        EmailSet.objects.create(email=email, url=url, passw=passw)
        send_mail(
        'Your confirmation on the Header',
        'To confirm your email click the link {}'.format(MAIN_ADR + 'confirm/' + url),
        'dsrepup@mail.ru',
        ['12dsender12@gmail.com']
        )
    return mail


@random_str
def send_confirmation(email, passw):
    str = ''.join(random.choice(string.ascii_letters) for i in range(12))
    return str

