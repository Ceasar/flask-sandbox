"""
This module lets us see if there is a difference in content-length between two
objects which otherwise look similar.


The result from running locally is as follows:

    CAESAR-BAUTISTA:~ caesarbautista$ curl localhost:4000/manual --include
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Connection: close
    Server: Werkzeug/0.9.4 Python/2.7.8
    Date: Wed, 12 Nov 2014 01:15:13 GMT

    CAESAR-BAUTISTA:~ caesarbautista$ curl localhost:4000/auto --include
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 0
    Server: Werkzeug/0.9.4 Python/2.7.8
    Date: Wed, 12 Nov 2014 01:15:18 GMT

    curl localhost:4000/json --include
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 2
    Server: Werkzeug/0.9.4 Python/2.7.8
    Date: Wed, 12 Nov 2014 01:19:03 GMT

    {}
"""
from flask import Response, jsonify


def manual_response():
    return Response(200)


def auto_response():
    return "", 200


def json_response():
    return jsonify()
