import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FIRSTPROJECT.settings')
import django
django.setup()

from FIRSTAPPLICATION.models import Info
from faker import Faker
from phone_gen import PhoneNumber

fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name()
        fake_contact = PhoneNumber('USA').get_number(full=False)
        fake_address = fakegen.address()


        #New entry in database
        user = Info.objects.get_or_create(Name=fake_name,
                                    Contact=fake_contact,
                                    Address=fake_address)[0]

if __name__== '__main__':
    print("Populating Database.")
    populate(30)
    print("Done Populating.")