import os
import requests
import csv
import json
import xml.etree.ElementTree as ET



url = "https://api.ebay.com/ws/api.dll"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    "X-EBAY-API-COMPATIBILITY-LEVEL": "967",
    "X-EBAY-API-DEV-NAME": "2049a9dd-15bc-430c-92c8-1184afa2904e",
    "X-EBAY-API-APP-NAME": "kaidenxu-Analytic-PRD-c246ab0a7-42d9aad7",
    "X-EBAY-API-CERT-NAME": "PRD-246ab0a79154-d85b-43f4-97e9-47b7",
    "X-EBAY-API-CALL-NAME": "GetItem",
    "X-EBAY-API-SITEID": "1",
    "Content-Type": "text/xml"}

xml_request = '''<?xml version="1.0" encoding="utf-8"?>
<GetItemRequest xmlns="urn:ebay:apis:eBLBaseComponents">
  <RequesterCredentials>
  <eBayAuthToken>1lehi8h*****shsi</eBayAuthToken>  
  </RequesterCredentials>
  <ItemID>{item_id}</ItemID>
  <IncludeTaxTable>true</IncludeTaxTable>
</GetItemRequest>'''


# xml_data.format()
# .format(item_id=372437558608)
# for each in link_list:

def ebay_api_getItem(item_id=173686504702):
    xml_data = xml_request.format(item_id=item_id)
    item_response = requests.post(url, headers=headers, data=xml_data)
    item_xml_res = item_response.text
    print(item_xml_res)

    # item_json = item_response.json()
    # print(item_json.fieldnames)
    return item_xml_res


def xml_to_json(xml_res):
    item = {}
    root = ET.fromstring(xml_res)
    for each in root.iter():
        item_key = each.tag.rsplit("}")[-1]
        item[item_key] = each.text
    return item


def save_item_info(root_dir, item_links=[]):
    out_path = os.path.join(root_dir, "data_set/item_info.csv")
    with open(out_path, "w+", newline="") as item_csv:
        fieldnames = []
        csv_writer = csv.DictWriter(item_csv, fieldnames=fieldnames)
        csv_writer.writeheader()
        for item_id in item_links:
            xml_res = ebay_api_getItem(item_id)
            item_json = xml_to_json(xml_res)
            csv_writer.writerow(item_json)        