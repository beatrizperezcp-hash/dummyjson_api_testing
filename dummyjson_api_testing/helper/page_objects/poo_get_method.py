import requests as req
import os
import json

class Get_method:
    def __init__(self, context):
         self.context = context

    def prepare_uri(self, file_name, endpoint):
        uri = ""
        ruta = f"{os.getcwd()}/configuration/{file_name}.json"
        with open(ruta, "r") as e:
            data = json.load(e)
            for clave, valor in data.items():
                if clave == "uri":
                    uri = valor
            self.context.get_uri = f"{uri}{endpoint}"

    def prepare_header(self, header):
        self.context.header = header

    def performance_method_and_get_status_code(self):
     self.context.get_method = req.get(url=self.context.get_uri, headers=self.context.header)
     return self.context.get_method.status_code

