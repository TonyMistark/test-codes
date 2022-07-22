from wsgiref.simple_server import make_server

import falcon


class ThingsResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = (
            '\nTwo things awe me most, the starry sky '
            'above me and the moral law within me.\n'
            '\n'
            '    -Immanuel Kant\n\n'
        )


app = falcon.App()


things = ThingsResource()


app.add_route("/things", things)


if __name__ == "__main__":
    with make_server("", 8002, app) as httpd:
        print("Serving on port http://localhost:8002/")
        httpd.serve_forever()
