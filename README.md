# GIPHY Scraper

This script will scrape GIFs from GIPHY and save them by video & image type. This script also creates a JSON file with the metadata for the GIFS fetched for each query. GIFs are saved as [rank]_[query]_[id].[ext]. Each GIF is saved inside [image type]/[file type]  (e.g. 'original/mp4').

This script uses the GIPHY Python client from https://github.com/Giphy/giphy-python-client.

# Usage

Run run.py. Arguments:

```sh
python run.py [-q, --query QUERY]
			  [-l, --limit LIMIT]
			  [-o, --outdir OUTDIR]

Arguments:
	-q, --query QUERY 			search term to use
	-l, --limit LIMIT 			maximum number of gifs to save
	-o, --outdir OUTDIR 		name of the directory under which all gifs will be saved
```
## Requirements.

Python 2.7 and 3.4+

## Installation

```sh
pip install giphy_client
```