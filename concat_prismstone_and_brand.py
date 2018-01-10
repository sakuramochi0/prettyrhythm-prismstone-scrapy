import json


def main():
    with open('prismstone.json') as p, open('brand.json') as b:
        ps = json.load(p)
        bs = json.load(b)

    # Load prismstones
    prismstones = {}
    for p in ps:
        prismstones[p['id']] = p

    # Load brand
    brands = {}
    for b in bs:
        brands[b['id']] = b

    # Set brand (None if its brand does not exist
    for id, stone in prismstones.copy().items():
        item = brands.get(id)
        if item:
            brand =  item['brand']
        else:
            brand = None
        prismstones[id]['brand'] = brand

    # Write out json
    with open('prismstone_with_brand.json', 'w') as f:
        json.dump(list(sorted(prismstones.values(), key=lambda x: x['id'])), f, ensure_ascii=False)


if __name__ == '__main__':
    main()
