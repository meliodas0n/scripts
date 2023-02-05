#!/usr/bin/bash

page=1
while [ $page -lt 85 ];
do
  curl -s "https://wallhaven.cc/api/v1/search?q=4k&page=$page" | jq '.data[].path' | xargs -I{} wget {};
  page=$((page+1));
done
