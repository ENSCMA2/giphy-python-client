import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import sys
import argparse
import json
import os
import numpy as np
import pandas as pd
import requests
def create_metadata(api_response):
  data = api_response.data
  pagination = api_response.pagination
  meta = api_response.meta
  to_json = [[]]
  for item in data:
    dictionary = {'type': item.type, 'id': item.id, 'slug': item.slug, 'url': item.url, 'bitly_gif_url': item.bitly_gif_url, 
    'embed_url': item.embed_url, 'username': item.username, 'source': item.source, 'rating': item.rating, 'tags': item.tags, 'source_tld': item.source_tld, 'source_post_url': item.source_post_url, 'is_hidden': item.is_hidden, 
    'is_removed': item.is_removed, 'is_community': item.is_community, 'is_anonymous': item.is_anonymous, 
    'is_featured': item.is_featured, 'is_realtime': item.is_realtime, 'is_indexable': item.is_indexable, 'is_sticker': item.is_sticker, 
    'update_datetime': item.update_datetime, 'create_datetime': item.create_datetime, 'import_datetime': item.import_datetime, 
    'trending_datetime': item.trending_datetime, 'images': {}}
    images = {}
    images['fixed_height'] = {'url': item.images.fixed_height.url, 'width': item.images.fixed_height.width, 'height': item.images.fixed_height.height, 
    'size': item.images.fixed_height.size, 'mp4': item.images.fixed_height.mp4, 'mp4_size': item.images.fixed_height.mp4_size, 'webp': item.images.fixed_height.webp, 
    'webp_size': item.images.fixed_height.webp_size}
    images['fixed_height_still'] = {'url': item.images.fixed_height_still.url, 'width': item.images.fixed_height_still.width, 
    'height': item.images.fixed_height_still.height}
    images['fixed_height_downsampled'] = {'url': item.images.fixed_height_downsampled.url, 'width': item.images.fixed_height_downsampled.width, 
    'height': item.images.fixed_height_downsampled.height, 'size': item.images.fixed_height_downsampled.size, 'webp': item.images.fixed_height_downsampled.webp, 
    'webp_size': item.images.fixed_height_downsampled.webp_size}
    images['fixed_width'] = {'url': item.images.fixed_width.url, 'width': item.images.fixed_width.width, 'height': item.images.fixed_width.height, 
    'size': item.images.fixed_width.size, 'mp4': item.images.fixed_width.mp4, 'mp4_size': item.images.fixed_width.mp4_size, 'webp': item.images.fixed_width.webp, 
    'webp_size': item.images.fixed_width.webp_size}
    images['fixed_width_still'] = {'url': item.images.fixed_width_still.url, 'width': item.images.fixed_width_still.width, 
    'height': item.images.fixed_width_still.height}
    images['fixed_width_downsampled'] = {'url': item.images.fixed_width_downsampled.url, 'width': item.images.fixed_width_downsampled.width, 
    'height': item.images.fixed_width_downsampled.height, 'size': item.images.fixed_width_downsampled.size, 'webp': item.images.fixed_width_downsampled.webp, 
    'webp_size': item.images.fixed_width_downsampled.webp_size}
    images['fixed_height_small'] = {'url': item.images.fixed_height_small.url, 'width': item.images.fixed_height_small.width, 'height': item.images.fixed_height_small.height, 
    'size': item.images.fixed_height_small.size, 'mp4': item.images.fixed_height_small.mp4, 'mp4_size': item.images.fixed_height_small.mp4_size, 'webp': item.images.fixed_height_small.webp, 
    'webp_size': item.images.fixed_height_small.webp_size}
    images['fixed_height_small_still'] = {'url': item.images.fixed_height_small_still.url, 'width': item.images.fixed_height_small_still.width, 
    'height': item.images.fixed_height_small_still.height}
    images['fixed_width_small'] = {'url': item.images.fixed_width_small.url, 'width': item.images.fixed_width_small.width, 'height': item.images.fixed_width_small.height, 
    'size': item.images.fixed_width_small.size, 'mp4': item.images.fixed_width_small.mp4, 'mp4_size': item.images.fixed_width_small.mp4_size, 'webp': item.images.fixed_width_small.webp, 
    'webp_size': item.images.fixed_width_small.webp_size}
    images['fixed_width_small_still'] = {'url': item.images.fixed_width_small_still.url, 'width': item.images.fixed_width_small_still.width, 
    'height': item.images.fixed_width_small_still.height}; 
    images['downsized'] = {'url': item.images.downsized.url, 'width': item.images.downsized.width, 'height': item.images.downsized.height, 'size': item.images.downsized.size}
    images['downsized_still'] = {'url': item.images.downsized_still.url, 'width': item.images.downsized_still.width, 'height': item.images.downsized_still.height}
    images['downsized_large'] = {'url': item.images.downsized_large.url, 'width': item.images.downsized_large.width, 'height': item.images.downsized_large.height, 
    'size': item.images.downsized_large.size}
    images['downsized_medium'] = {'url': item.images.downsized_medium.url, 'width': item.images.downsized_medium.width, 'height': item.images.downsized_medium.height, 
    'size': item.images.downsized_medium.size}
    images['downsized_small'] = {'mp4': item.images.downsized_small.mp4, 'width': item.images.downsized_small.width, 'height': item.images.downsized_small.height, 
    'mp4_size': item.images.downsized_small.mp4_size}
    images['original'] = {'url': item.images.original.url, 'width': item.images.original.width, 'height': item.images.original.height, 'size': item.images.original.size, 
    'frames': item.images.original.frames, 'mp4': item.images.original.mp4, 'mp4_size': item.images.original.mp4_size, 'webp': item.images.original.webp, 
    'webp_size': item.images.original.webp_size}
    images['original_still'] = {'url': item.images.original_still.url, 'width': item.images.original_still.width, 'height': item.images.original_still.height}
    images['looping'] = {'mp4': item.images.looping.mp4}
    images['preview'] = {'mp4': item.images.preview.mp4, 'mp4_size': item.images.preview.mp4_size, 'width': item.images.preview.width, 'height': item.images.preview.height}
    images['preview_gif'] = {'url': item.images.preview_gif.url, 'width': item.images.preview_gif.width, 'height': item.images.preview_gif.height, 
    'size': item.images.preview_gif.size}
    dictionary['images'] = images
    to_json[0].append(dictionary)
  to_json.append({'offset': pagination.offset, 'total_count': pagination.total_count, 'count': pagination.count})
  to_json.append({'msg': meta.msg, 'status': meta.status, 'response_id': meta.response_id})
  return to_json

def make_dirs(basedir='out'):
  save_types = ['downsized', 'downsized_large', 'downsized_medium', 'downsized_small', 'downsized_still', 
    'fixed_height', 'fixed_height_downsampled', 'fixed_height_small', 'fixed_height_small_still', 
    'fixed_height_still', 'fixed_width', 'fixed_width_downsampled', 'fixed_width_small', 'fixed_width_small_still', 
    'fixed_width_still', 'looping', 'original', 'original_still', 'preview', 'preview_gif']
  save_subtypes = ['fixed_height', 'fixed_height_small', 'fixed_width', 'fixed_width_small', 'original']
  save_some_subtypes = ['fixed_height_downsampled', 'fixed_width_downsampled']
  subtypes = ['url', 'mp4', 'webp']
  some_subtypes = ['url', 'webp']
  url = ['downsized', 'downsized_still', 'downsized_medium', 'downsized_large', 'fixed_height_still', 
  'fixed_height_small_still', 'fixed_width_still', 'fixed_width_small_still', 'original_still', 'preview_gif']
  mp4 = ['downsized_small', 'looping', 'preview']
  if not os.path.isdir(basedir):
    os.mkdir(basedir)
  if not os.path.isdir(basedir + '/metadata'):
    os.mkdir(basedir + '/metadata')
  for item in save_types:
    if not os.path.isdir(basedir+'/'+item):
      os.mkdir(basedir+'/'+item)
      if item in url:
        os.mkdir(basedir+'/'+item+'/'+'url')
      elif item in mp4:
        os.mkdir(basedir+'/'+item+'/'+'mp4')
  for item in save_subtypes:
	  for subtype in subtypes:
	    if not os.path.isdir(basedir+'/'+item+'/'+subtype):
	      os.mkdir(basedir+'/'+item+'/'+subtype)
  for item in save_some_subtypes:
	  for subtype in some_subtypes:
	    if not os.path.isdir(basedir+'/'+item+'/'+subtype):
	      os.mkdir(basedir+'/'+item+'/'+subtype)

def save_file(url, name, folder, basedir='out', base_folder=''):
  r = requests.get(url, allow_redirects = True)
  if base_folder != '':
    open(basedir + '/' + base_folder + '/' + folder + '/' + name, 'wb').write(r.content)
  else: 
    open(basedir + '/' + folder + '/' + name, 'wb').write(r.content)

def save_files(q, to_json, basedir='out'):
  rank = 1
  for item in to_json[0]:
    for image in item['images'].keys():
      types = item['images'][image].keys()
      name = item['images'][image]
      if not 'url' in types and not 'webp' in types:
        save_file(name['mp4'], str(rank) + '_' + q + '_' + item['id'] + '.mp4', 'mp4', basedir, image)
      elif not 'mp4' in types and not 'webp' in types:
        save_file(name['url'], str(rank) + '_' + q + '_' + item['id'] + '.gif', 'url', basedir, image)
      elif 'url' in types and 'webp' in types and not 'mp4' in types:
        save_file(name['url'], str(rank) + '_' + q + '_' + item['id'] + '.gif', 'url', basedir, image)
        save_file(name['webp'], str(rank) + '_' + q + '_' + item['id'] + '.webp', 'webp', basedir, image)
      elif 'url' in types and 'webp' in types and 'mp4' in types:
        save_file(name['url'], str(rank) + '_' + q + '_' + item['id'] + '.gif', 'url', basedir, image)
        save_file(name['webp'], str(rank) + '_' + q + '_' + item['id'] + '.webp', 'webp', basedir, image)
        save_file(name['mp4'], str(rank) + '_' + q + '_' + item['id'] + '.mp4', 'mp4', basedir, image)
    rank += 1
