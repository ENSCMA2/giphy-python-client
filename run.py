import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import sys
import argparse
import json
import os
import numpy as np
import pandas as pd
from helpers import *
import time
# create an instance of the API class

api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

def parse_args():
    parser = argparse.ArgumentParser(description="Scrape GIFs from giphy")
    parser.add_argument(
        "-q", "--query", default='cheese', help="Search for the given tag; use + as a space character for phrases")
    parser.add_argument(
        "-l", "--limit", type=int, default=100, help="Scraped GIFs limit; must be between 1 and 100 inclusive")
    parser.add_argument("-o", "--outdir", default='out', help="Name of directory you want to save to")
    return parser.parse_args()

try: 
    # Search Endpoint
    args = parse_args()
    print(args)
    q = args.query
    limit = args.limit
    out_dir = args.outdir
    api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
    make_dirs(out_dir)
    start = time.time()
    to_json = create_metadata(api_response)
    end = time.time()
    print("Took " + str(end - start) + " seconds to create metadata.")
    start = time.time()
    json.dump(to_json, open(out_dir + '/metadata/' + q + '_metadata.json', 'w+'))
    end = time.time()
    print("Took " + str(end - start) + " seconds to dump metadata to json.")
    start = time.time()
    save_files(q, to_json, out_dir)
    end = time.time()
    print("Took " + str(end - start) + " seconds to save gifs.")
    if not os.path.exists(out_dir + '/metadata/info.csv'):
        columns = ["UUID", "Query", "Rank"]
        information_csv = pd.DataFrame(columns=columns)
        rank = 1
        count = 0
        for item in api_response.data:
            information_csv.loc[count, 'UUID'] = item.id
            information_csv.loc[count, 'Query'] = q
            information_csv.loc[count, 'Rank'] = rank
            rank += 1
            count += 1
        information_csv.to_csv(out_dir + '/metadata/info.csv', columns = columns)
    else:
        information_csv = pd.read_csv(out_dir + '/metadata/info.csv')
        columns = ['UUID', 'Query', 'Rank']
        information_csv = information_csv[columns]
        rank = 1
        files_that_already_exist = list(information_csv['UUID'])
        count = len(files_that_already_exist)
        for item in api_response.data:
            if not item.id in files_that_already_exist:
                information_csv.loc[count, 'UUID'] = item.id
                information_csv.loc[count, 'Query'] = q
                information_csv.loc[count, 'Rank'] = rank
                count += 1
            rank += 1
        information_csv.to_csv(out_dir + '/metadata/info.csv', columns = columns)
    print("Found " + str(len(api_response.data)) + " gifs for the query '" + q + ".'")
except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
