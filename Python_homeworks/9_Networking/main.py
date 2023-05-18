import json
from http.server import HTTPServer, BaseHTTPRequestHandler

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    def do_GET(self):
        USERS_LIST1 = [
            {
                "id": 1,
                "username": "theUser",
                "firstName": "John",
                "lastName": "James",
                "email": "john@email.com",
                "password": "12345",
            }
        ]
        global USERS_LIST
        name = [i for i in USERS_LIST if i["username"] == self.path[6:]]
        if self.path == '/reset':
            USERS_LIST = USERS_LIST if USERS_LIST == USERS_LIST1 else USERS_LIST1
            self._set_response(200, USERS_LIST)
        elif self.path == "/users":
            self._set_response(200, USERS_LIST)
        elif "/user/" in self.path and name:
            self._set_response(200, name[0])
        else:
            self._set_response(400, {"error": "User not found"})

    def do_POST(self):
        data = self._pars_body()
        if type(data) == dict:
            if len(data) != 6 or data['id'] in [i['id'] for i in USERS_LIST]:
                self._set_response(400, {})
                return
            else:
                USERS_LIST.append(data)
                print(data, 3, USERS_LIST)
                self._set_response(201, data)
                return
        else:
            for i in data:
                if len(i) != 6 or i['id'] in [e['id'] for e in USERS_LIST]:
                    self._set_response(400, {})
                    return
            USERS_LIST.extend(data)
            self._set_response(201, data)

    def do_PUT(self):
        if '/user/' in self.path:
            if int(self.path[6:]) in [i['id'] for i in USERS_LIST]:
                data = self._pars_body()
                if len(data) == 5:
                    for i in USERS_LIST:
                        if i['id'] == int(self.path[6:]):
                            i.update(data)
                            self._set_response(200, i)
                else:
                    self._set_response(400, {"error": "not valid request data"})
            else:
                self._set_response(404, {"error": "User not found"})


    def do_DELETE(self):
        if '/user/' in self.path:
            if int(self.path[6:]) in [i['id'] for i in USERS_LIST]:
                for i in USERS_LIST:
                    if i['id'] == int(self.path[6:]):
                        USERS_LIST.remove(i)
                        self._set_response(200, {})
            else:
                self._set_response(404, {"error": "User not found"})


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()