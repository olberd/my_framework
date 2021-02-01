from lazypage import render


def index_view(request):
    secret = request.get('secret_key', None)
    return '200 OK', render('index.html', secret=secret)


def about_view(request):
    return '200 OK', "About"


