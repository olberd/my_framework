from lazypage import Application
import views


url = {
    '/': views.index_view,
    '/about/': views.about_view,
}


def secret_controller(request):
    request['secret_key'] = 'SECRET'


controllers = [
    secret_controller
]

application = Application(url, controllers)

# Запуск
# uwsgi --http :8000 --wsgi-file main.py