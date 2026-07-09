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

    def perform_method_and_get_status_code(self):
     self.context.get_method = req.get(url=self.context.get_uri, headers=self.context.header)
     return self.context.get_method.status_code

    def verify_field_in_body(self, key, field=None):
        json = self.context.get_method.json()
        if field is None:
          if key not in json:
            raise ValueError(f"Key {key} is missing in the body")
        else:
            for x in json[field]:
                if key not in x:
                 raise ValueError(f"Key {key} is missing in the body")

        return json

    def verify_main_in_body(self):
        json = self.context.get_method.json()
        return json




