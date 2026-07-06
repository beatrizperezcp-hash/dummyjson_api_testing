from contextlib import nullcontext

from behave import step
from helper.page_objects.poo_get_method import Get_method
import requests as req


@step("prepare uri from the file {file_name} and the endpoint {endpoint}")
def prepare_uri_step(context, file_name, endpoint):
    """This function prepares uri from json file and adds endpoint from .feature file"""
    get_poo = Get_method(context)
    get_poo.prepare_uri(file_name, endpoint)


@step("prepare header with the following data")
def prepare_header(context):
    header = {}
    for i, x in enumerate(context.table, start=0):
        value = x["value"]
        key = x["key"]
        header[key] = value
    get_poo = Get_method(context)
    get_poo.prepare_header(header)


@step("performa method and validate the status code {status_code}")
def performance_method(context, status_code):
    get_poo = Get_method(context)
    response = str(get_poo.perform_method_and_get_status_code())
    assert status_code == response, f"Something went wrong with the status code {response}"


@step("verify the key {key} with the following conditions")
def validate_items_in_body(context, key):
    get_poo = Get_method(context)
    response = get_poo.verify_field_in_body(key)

    for x in context.table:
        key_table = x["key"]
        condition = x["condition"]
        value = x["value"]
        if response[key]:
         for x in response[key]:
            if condition == ">":
              if x[key_table] > int(value):
                 pass
            elif condition == "not" and value == any:
                if not value(x[key_table]):
                  pass
            elif condition == ">=":
                if x[key_table] >= int(value):
                    pass
            elif condition == "not":
                if x[key_table] is not None:
                    pass
            else:
                raise ValueError(f"Something went wrong {[key_table]}")

@step("validate {key} is not duplicated")
def validate_key_is_not_duplicated(context, key):
    get_poo = Get_method(context)
    response = get_poo.verify_field_in_body(key)
    keys = []
    for x in response["products"]:
       if x[key] not in keys:
           keys.append(x[key])
       else:
           raise ValueError(f"Something went wrong in {x[key]}")




