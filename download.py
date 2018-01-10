"""プリズムストーンの画像をダウンロードするスクリプト"""
import json
import os
import logging
import time
import requests

IMG_DIR = 'img/'

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(os.path.basename(__file__))

    with open('prismstone_with_brand.json') as f:
        stones = json.load(f)

    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)

    for stone in stones:
        img_url = stone['img_url']
        basename = os.path.basename(img_url)
        filename = os.path.join(IMG_DIR, basename)
        if os.path.exists(filename):
            continue
        r = requests.get(img_url)
        with open(filename, 'bw') as f:
            f.write(r.content)
            logger.info('Saved: {}'.format(img_url))
        time.sleep(0.1)