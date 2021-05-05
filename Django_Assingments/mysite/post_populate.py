import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django, random
django.setup()

from blog.models import Post
from django.contrib.auth.models import User
from faker import Faker

fakegen = Faker()

#data from User database
id = []
user = User.objects.all()
for i in user:
    id.append(i.id)

def populate(N=5):
    for entry in range(N):
        fake_title  = fakegen.text().split('.')[0]
        fake_content = fakegen.text()+' '+fakegen.text()
        lst = fake_title.split()
        fake_slug = '-'.join(lst)

        #for STATUS
        lst_status = [0,1]
        fake_status = random.choice(lst_status)


        #New entry in database
        post = Post.objects.get_or_create(title=fake_title,slug=fake_slug,author_id=id[entry-1],
                                        content=fake_content,status=fake_status)[0]



if __name__ == '__main__':
    print('POPULATING DATABASE')
    populate(4)
    print('Done Populating!!!')
