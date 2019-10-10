import os
import pandas as pd
from extract_item_id import get_item_id
from item_info_api import save_item_info


root_dir = os.path.pardir(os.path.abspath(__file__))


def run_spider():
    item_id_path = os.path.join(root_dir, "data_set/item_id.csv")
    get_item_id(item_id_path)
    item_df = pd.read_csv(item_id_path, encoding="gbk", dtype="str")
    item_links = item_df["item_id"]
    save_item_info(root_dir, item_links=item_links)
    

if __name__ == "__main__":
    run_spider()