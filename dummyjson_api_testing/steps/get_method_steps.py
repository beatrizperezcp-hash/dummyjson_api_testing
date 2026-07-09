import json
import os
from behave import step
from helper.page_objects.poo_get_method import Get_method


@step("prepare uri from the file {file_name} and the endpoint {endpoint}")
def prepare_uri_step(context, file_name, endpoint):
    """This function prepares uri from json file and adds endpoint from .feature file"""
    get_poo = Get_method(context)
    get_poo.prepare_uri(file_name, endpoint)


@step("prepare header with the following data")
def prepare_header(context):
    """This function prepares header from .feature file"""
    header = {}
    key = ""
    for i, x in enumerate(context.table, start=0):
        value = x["value"]
        key = x["key"]
        header[key] = value
    get_poo = Get_method(context)
    get_poo.prepare_header(header)
    ruta = f"{os.getcwd()}/configuration/{x['value']}.json"
    with open(ruta, "r") as e:
        data = json.load(e)
        header[x["key"]] = data[key]


@step("perform method and validate the status code {status_code}")
def perform_method(context, status_code):
    """This function perform method and validates stats code"""
    get_poo = Get_method(context)
    response = get_poo.perform_method_and_get_status_code()
    assert int(status_code) == response, f"Something went wrong with the status code {response}"


@step("verify the key {key} with the following conditions")
def validate_items_in_body(context, key):
    """This function validates key, condition and value"""
    get_poo = Get_method(context)
    response = get_poo.verify_field_in_body(key)

    for x in context.table:
        key_table = x["key"]
        condition = x["condition"]
        value = x["value"]
        if response[key]:
         for x in response[key]:
            if condition == ">":
              if x[key_table] <= int(value):
                 raise ValueError(f"The following condition was not met {condition}")
            elif condition == "not" and value == any:
                if value(x[key_table]):
                    raise ValueError(f"The following condition was not met {value(x[key_table])}")
            elif condition == ">=":
                if x[key_table] < int(value):
                    raise ValueError(f"The following condition was not met {condition}")
            elif condition == "not":
                if x[key_table] is None:
                    raise ValueError(f"The following condition was not met {condition}")


@step("verify the following keys in the body")
def validate_items_in_body(context):
    """This function validates values"""
    get_poo = Get_method(context)
    response = get_poo.verify_main_in_body()

    for x in context.table:
        key_table = x["key"]
        if key_table not in response:
           raise ValueError(f"Key {key_table} is missing in the body")

@step("validate {key} is not duplicated in {field}")
def validate_key_is_not_duplicated(context, key, field):
    """This function validates is the indicated key is not duplicated"""
    get_poo = Get_method(context)
    response = get_poo.verify_field_in_body(key, field)
    keys = []
    for x in response[field]:
       if x[key] not in keys:
           keys.append(x[key])
       else:
           raise ValueError(f"Something went wrong in {x[key]}")




