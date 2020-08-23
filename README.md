# GIPHY Scraper

This script will scrape GIFs from GIPHY and save them by video & image type. This script also creates a JSON file with the metadata for the GIFS fetched for each query as well as a CSV file that stores UUID, query, and rank and is used to check for duplicates (and not save them again). GIFs are saved as `[rank]\_[query]\_[id].[ext]`. Each GIF is saved inside `[image type]/[file type]`  (e.g. `original/mp4`).

This script uses the GIPHY Python client from https://github.com/Giphy/giphy-python-client.

## Usage

```sh
python run.py [-q, --queries QUERIES]
			  [-l, --limit LIMIT]
			  [-o, --outdir OUTDIR]
			  [-s, --offset OFFSET]

Arguments:
	-q, --queries QUERIES 		search term(s) to use, separate different terms by comma with NO SPACE, use + signs as spaces for phrases
	-l, --limit LIMIT 		maximum number of gifs to save PER QUERY
	-o, --outdir OUTDIR 		name of the directory under which all gifs will be saved
	-s, --offset OFFSET		max offset of the search, defaults to 0; can be between 0 and 100, but should be a multiple of 25 or a multiple of the limit; e.g. if offset = 50, it gets 25 gifs starting from the 1st result, another 25 starting from the 26th result, and another 25 starting from the 51st result; so total number of results returned is limit + offset
```
Example command:
```sh
python run.py -q "cheese","cheeseburgers","eye+roll" -l 25 -s 50
```
This will search for "cheese," "cheeseburgers," and "eye roll" with a limit of 75 results per query. 
## Requirements

Python 2.7 and 3.4+

```sh
pip install giphy_client
```
