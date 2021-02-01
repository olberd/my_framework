def add_slash(path):
    if path[-1] != "/":
        return path + "/"
    else:
        return path


class Application:
    def __init__(self, url: dict, controllers: list):
        self.url = url
        self.controllers = controllers

    def __call__(self, env, start_response):
        path = add_slash(env['PATH_INFO'])
        if path in self.url:
            view = self.url[path]
            request = {}
            for controller in self.controllers:
                controller(request)

            code, text = view(request)
            start_response(code, [('Content-Type', 'text/html')])
            return [text.encode('utf-8')]
        else:
            start_response('404 NOT FOUND', [('Content-Type', 'text/html')])
            return [b'Not Found']
