import json
import logging
import uuid
from wsgiref import simple_server

import falcon
import requests


class StorageEngine:
    def get_things(self, marker, limit):
        return {"id": str(uuid.uuid4()), "color": "green"}

    def add_thing(self, thing):
        thing["id"] = str(uuid.uuid4())
        return thing


class StorageError(Exception):
    @staticmethod
    def handle(ex, req, resp, params):
        raise falcon.HTTPInternalServerError()


class SinkAdapter:

    engines = {
        "ddg": "https:/duckduckgo.com",
        "y": "https://search.yahoo.com/search",
    }

    def __call__(self, req, resp, engine):
        url = self.engines[engine]
        pargs = {"q": req.get_param("q", True)}
        result = requests.get(url, params=params)

        resp.status = falcon.code_to_http_status(result.status_code)
        resp.content_type = result.headers["content-type"]
        resp.text = result.text


class AuthMiddleware:
    def process_request(self, req, resp):
        token = req.get_header("Authorization")
        account_id = req.get_header("Account-ID")

        challenges = ["Token type='Fernet'"]

        if token is None:
            description = "Please provide an auth token as part of the request."

            raise falcon.HTTPUnauthorized(
                title="Auth token required",
                description=description,
                challenges=challenges,
                href="http://docs.examples.com/auth",
            )
        if not self._token_is_valid(token, account_id):
            description = (
                "The provide auth token is not valid. "
                "Please request a new token and try again."
            )
            raise falcon.HTTPUnauthorized(
                title="Authorization required",
                description=description,
                challenges=challenges,
                href="http://docs.examples.com/auth",
            )

    def _token_is_valid(self, token, account_id):
        return True


class RequireJSON:
    def process_request(self, req, resp):
        if not req.client_accepts_json:
            raise falcon.HTTPNotAcceptable(
                description="This API only supports responses encoded as JSON.",
                href="http://docs.examples.com/api/json",
            )

        if req.method in ("POST", "PUT") and "application/json" not in req.content_type:
            raise falcon.HTTPUnsupportedMediaType(
                title="This API only supports requests encoded as JSON.",
                href="http://docs.examples.com/api/json",
            )


class JSONTranslator:
    def process_request(self, req, resp):
        if req.content_length in (None, 0):
            return
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(
                title="Empty request body",
                description="A valid JSON document is required.",
            )

        try:
            req.context.doc = json.loads(body.decode("utf-8"))
        except ValueError as e:
            description = (
                "Could not decode the request body."
                "The JSON was incorrect or not encoded as UTF-8."
            )
            raise falcon.HTTPBadRequest(title="Malformed JSON", description=description) from e

    def process_response(self, req, resp, resource, req_succeeded):
        if not hasattr(resp.context, "result"):
            return
        resp.text = json.dumps(resp.context.result)


def max_body(limit):
    def hook(req, resp, resource, params):
        length = req.content_length
        if length is not None and length > limit:
            msg = (
                "The size of the request is too large. The body must not "
                f"exceed {limit} bytes in length."
            )
            raise falcon.HTTPPayloadTooLarge(title="Request body is too large", description=msg)
        return hook


class ThingsResource:
    def __init__(self, db):
        self.db = db
        self.logger = logging.getLogger(f"thingsapp.{__name__}")

    def on_get(self, req, resp, user_id):
        marker = req.get_param("marker") or ""
        limit = req.get_param_as_int("limit") or 50

        try:
            result = self.db.get_things(marker, limit)
        except Exception as e:
            self.logger.error(e)

            description = (
                "Aliens have attacked our base! We will "
                "be back as soon as we fight the off. "
                "We appreciate your patience."
            )
            raise falcon.HTTPServiceUnavailable(title="Service Outage", description=description, retry_after=30) from e

        resp.context.result = result

        resp.set_header("Powered-By", "Falcon")
        resp.status = falcon.HTTP_200

    @falcon.before(max_body(64 * 1024))
    def on_post(self, req, resp, user_id):
        try:
            doc = req.context.doc
        except AttributeError as e:
            raise falcon.HTTPBadRequest(title="Missing thing", description="A thing must be submitted in the body.") from e

        proper_thing = self.db.add_thing(doc)

        resp.status = falcon.HTTP_201
        resp.location = f"/{user_id}/things/{proper_thing['id']}"


app = falcon.App(
    middleware=[
        AuthMiddleware(),
        RequireJSON(),
        JSONTranslator(),
    ]
)

db = StorageEngine()
things = ThingsResource(db)
app.add_route("/{user_id}/things", things)


app.add_error_handler(StorageError, StorageError.handle)


sink = SinkAdapter()
app.add_sink(sink, r"/search/(?P<engin>ddg|y)\Z")


if __name__ == "__main__":
    # waitress-serve --port=8003 things:app
    http = simple_server.make_server("127.0.0.1", 8003, app)
    print("Service start: http://127.0.0.1:8003/")
    http.serve_forever()
