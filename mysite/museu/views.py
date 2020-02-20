from django.shortcuts import render

messages = [
    {
        'title': 'this is the first message',
        'content': 'how are u?'
    },
    {
        'title': 'this is the second message',
        'content': 'how come?'
    },
    {
        'title': 'this is the third message',
        'content': 'hello'
    }
]


def index(request):
    return render(request, 'museu/index.html')


def check_db(request):
    return render(request, 'museu/check_db.html', {'messages': messages})
