#!/usr/bin/env bash

cat prismstone.json | ramda 'sort-by prop \id' | md-table > prismstone.md
cat brand.json | ramda 'sort-by prop \id' | md-table > brand.md
cat prismstone_with_brand.json | ramda 'sort-by prop \id' 'project <[id name brand category series img_url]>' | md-table > prismstone_with_brand.md