import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_uname = fakegen.name().split()[0]
        upassword = fakegen.bothify('??????##')



        #New entry in database

        user = User.objects.get_or_create(username=fake_uname, password=upassword)

if __name__ == '__main__':
    print('POPULATING DATABASE')
    populate()
    print('Done Populating!!!')
