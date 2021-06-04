#from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

# Create your views here.

posts = [
        {
            'title': 'Mont Blac',
            'user': {
                'name': 'Yesica Cortés',
                'picture': 'https://picsum.photos/60/60/?image=1027',
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/800/?image=1036',
        },
       {
            'title': 'Via Lácte',
            'user': {
                'name': 'C. Vander',
                'picture': 'https://picsum.photos/60/60/?image=1005',
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/800/?image=903',
       },

         {
            'title': 'Nuevo auditorio',
            'user': {
                'name': 'Thespianartist',
                'picture': 'https://picsum.photos/60/60/?image=883',
            },
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'photo': 'https://picsum.photos/800/800/?image=1076',
        }
    ]

# def list_posts(request):
#     #posts = [1,2,4]
#     content = []
#     for post in posts:
#         content.append("""
#             <p><strong>{name}</p></strong>
#             <p><small>{user} - <i>{timestamp}</i></p></small>
#             <figure><img src = "{picture}"/></figure>
#         """.format(**post))
#return HttpResponse(str(posts))
    #   return HttpResponse('<br>'.join(content))

def list_posts(request):
    "list existing posts"
    return render(request, 'feed.html', {'posts': posts})