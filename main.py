#!/usr/bin/env python3
#
from collections import OrderedDict

import cherrypy
from json2html import json2html
from pylxd import Client
from pylxd.exceptions import ClientConnectionFailed, LXDAPIException


class GetLXDInfo(object):
    @cherrypy.expose
    def index(self):
        return """<html>
        <br></br>
        <br></br>
        <br></br>
        <body align="center">
        To query LXD container status, just enter the IP of host system.
        <br></br>
        <form method="get" action="getInfo">
        <input type="text" value="172.21.18.217" name="IP"/>
        <div>
        <label><input name="level" type="radio" value="0" checked />brief</label>
        <label><input name="level" type="radio" value="1" />detailed</label>
        </div>
        <button type="submit">Query</button>
        </form>
        </body>
        </html>
        """
    @cherrypy.expose
    def getInfo(self, IP=None, level=None):
        client_crt = "/lxd/client.crt"
        client_key = "/lxd/client.key"

        try:
            client = Client(endpoint='https://{}:8443'.format(IP.strip()),
                            cert=(client_crt, client_key),
                            verify=False,
                            timeout=5)
        except ClientConnectionFailed:
            return "Error: host server not valid, check your IP."

        try:
            containers = client.containers.all()
        except LXDAPIException:
            return "Error: not authorized, administrator should update certificate file"

        if not containers:
            return "The server: {} have no LXD container instance running.".format(IP)

        result = dict()
        for x in containers:
            if level == "1":
                state = x.state().__dict__
            else:
                state = OrderedDict()
                state['status'] = x.state().status
                state['network'] = x.state().network['eth0']['addresses']
            result[x.name] = state

        return json2html.convert(json=result)


if __name__ == '__main__':
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.quickstart(GetLXDInfo())
