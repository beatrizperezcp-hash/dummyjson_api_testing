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

@step("performance method and validate the status code {status_code}")
def performance_method(context, status_code):
    get_poo = Get_method(context)
    response = str(get_poo.performance_method_and_get_status_code())
    assert status_code == response, f"Something went wrong with the status code {response}"
