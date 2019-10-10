# -*- coding: utf-8 -*-
# !/bi_team/webscrape
"""
Created on Wed Jan  9 14:47:46 2019

@author: Administrator
"""
import os
import pandas as pd
import requests
from bs4 import BeautifulSoup


first_headers = {"User-Agent":"ozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0"}
#first_cookies = {"nosession":"BAQAAAWgWKMkCAAaAAAgAHFxg8vIxNTQ3MjY1NDkweDE4MjY3NTQ4MDMyNngweDJZADMACV4amXI0MzAwMCxVU0EAygAgZZ9ncjQwMzNiOWJkMTY4MGFhZDA4OTExNDcxMGZmZjg3NTgzAMsAAlw5bRoyMLltYCNPsRLKVu43y0LWekrelDei"}

first_url = "https://www.ebay.com/sch/i.html?_fsrp=1%3F_fsrp%3D1&_from=R40&_sacat=0&_nkw=mopar&rt=nc&_ipg=200&rt=nc&_pgn=1"

cookies = {"nonsession":"BAQAAAWgWKMkCAAaAAAgAHFxhhRQxNTQ3MjgwMDgxeDI3MzUyMDY1NzI3NngweDJZADMACV4bK5Q0MzAwMCxVU0EAygAgZZ/5lDQwMzNiOWJkMTY4MGFhZDA4OTExNDcxMGZmZjg3NTgzAMsAAlw5/x0xODrZxTf6mO7d32aUWtrGyw3ISjBC",
           "dp1":"bu1p/QEBfX0BAX19AQA**5e1b2b95^bl/CN5ffc5f15^pbf/%238000e000008100020000005e1b2b95^",
           "ns1":"BAQAAAWgWKMkCAAaAANgASl4bK5VjNjl8NjAxXjE1NDcyNjUzNTgzNTNeXjFeM3wyfDV8NHw3fDExXl5eNF4zXjEyXjEyXjJeMV4xXjBeMV4wXjFeNjQ0MjQ1OTA3Naf0e44oOWQMjmaPKG8tF5cJN/j2",
           "npii":"btguid/4033b9bd1680aad089114710fff875835e1b2cfd^cguid/4033c42a1680a9cd2c46374ee5f828c55e1b2cfd^",
           "__gads":"ID=5bbb3daeb5b82773:T=1547280086:S=ALNI_MbqalfLJPqCO1sKuXTxHyCMUmvMow",
           "ebay":"%5Esbf%3D%2340%5Ecv%3D15555%5Ejs%3D1%5Epsi%3DAcQBSRa4*%5E",
           "s":"CgAD4ACBcO0mVNDAzM2I5YmQxNjgwYWFkMDg5MTE0NzEwZmZmODc1ODNMOOwu",
           "ak_bmsc":"98DCF0ECFDC0CC7F3C3F609CFF5FA4DFB832576EBF52000026F7395CB1CDDE25~plS/EFjAsSlayACkRVTUvivTYherbUDLNRjhmr8uPzGVmd7hoeGAUQrX4osFq8Cfb3Sjb771+AgCIQpINKHyLNpDwzwI0OIpRwSI1rr+AjGG5eAYnrU+XRZYOqe6VIqRuOtYzJMmIkiOmsGj18Bhx0r4BuTZ6cF7C4CBsxzXW4mF5PqsOn18wdGd6x65wg8GD+xiDy9gSpjbWsF9PjzWDCxkfzOs98QMmI/BIbGvJGQIU=",
           "cssg":"4033b9bd1680aad089114710fff87583",
           "bm_sv":"96404CCE1D5EEB29F26170B3304DCB2F~O85cZWMAS9NPbS8mqrJYz8W4pHJM8gUywaPXeCifnbg9lQWUkqUxboL5zed2MBA+bzQB1KKk7+Np/wazCGrZrZ69HN7YZhvXxElysi+cWADskUfpKinfqLSESBLjIdGRD/pyPp68A1DuehP4F9vJJxKDpCF0Y/KP89JggKsjxHo=",
           "JSESSIONID":"8988039EE1945CA61F8C3A20AFB926B1",
           "AMCV_A71B5B5B54F607AB0A4C98A2%40AdobeOrg":"-1758798782%7CMCIDTS%7C17909%7CMCMID%7C88770067809513492429205471145025671929%7CMCAID%7CNONE%7CMCOPTOUT-1547310087s%7CNONE%7CMCAAMLH-1547907687%7C11%7CMCAAMB-1547907687%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCCIDH%7C1575549283",
           "AMCVS_A71B5B5B54F607AB0A4C98A2%40AdobeOrg":"1",
           "aam_uuid":"88804390521411661519208939697482148676",
           "ds2":"sotr/b8_5azzzzzzz^"}

                 
# part1: download the item-list html page, to extract the item-id 
def get_page_links(page_url="", cookies=cookies):

    item_ids = []
    try:
        res = requests.get(page_url, headers=first_headers, cookies=cookies)
    except:
        print(res.requests.url)
        return None
    else:
        res_cookies = new_cookies(res.cookies)
        
        res.encoding="utf-8"
        soup = BeautifulSoup(res.text, "html.parser")

        page_items = soup.find_all("a", attrs={"class": "srchLnk"})
        for each_item in page_items:
            item_link = each_item["id"]
            item_ids.append(item_link+"_")
        return (item_ids, res_cookies)


"""
part2: solve cookies, but this part not used in this application.
def new_cookies(res_cookies):
    for key in res_cookies.keys():
        if res_cookies.get(key) is None:
            del res_cookies[key]
    return res_cookies


def new_cookies_test():    
    test_res = requests.get(first_url, headers=first_headers, cookies=cookies)
    print(test_res.status_code)
    
    new_cookie = new_cookies(test_res.cookies)
    cookies.update(new_cookie)
"""


# part3: iterate the item-list pages, to get enough item id
def get_item_id(item_id_path):
    df = pd.DataFrame()
    
    url_str = "https://www.ebay.com/sch/i.html?_fsrp=1%3F_fsrp%3D1&_from=R40&_sacat=1&_nkw=mopar&rt=nc&_ipg=200&_pgn={page_num}&rt=nc"
    for i in range(100, 500):    

        page_url = url_str.format(page_num=i)
        
        item_links = get_page_links(page_url=page_url,cookies=cookies)
        if item_links:
            df1 = pd.DataFrame()
            df1["item_id"] = item_links[0]
            df = df.append(df1, ignore_index=True)
            cookies.update(item_links[1])
            print("well {num}th times loop".format(num=i))
        elif item_links is None:
            print("wrong number is {0}".format(i))
            print("wrong links is {0}".format(item_links))
            
    df.to_csv(os.path.join(item_id_path), encoding="gbk", index=False)

    
if __name__ == "__main__":
    root_dir = os.path.pardir(os.path.abspath(__file__))
    get_item_id(os.path.join(root_dir, "data_set/item_id.csv"))