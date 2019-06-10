+++
title = "Import JSON to Elasticsearch using jq"
date = "2016-02-16"
slug = "2016/02/16/import-json-to-elasticsearch-using-jq"
Categories = ["Elasticsearch"]
+++

This is based on http://kevinmarsh.com/2014/10/23/using-jq-to-import-json-into-elasticsearch.html

Install jq first on Mac

```
brew install jq
```

Import the JSON file to Elasticsearch index

```
cat file.json | jq -c '.[] | {"index": {"_index": "bookmarks", "_type": "bookmark", "_id": .id}}, .' | curl -XPOST localhost:9200/_bulk --data-binary @-
```

Check for the list of indexes http://localhost:9200/_cat/indices?v

See the list of records http:/localhost:9200//bookmarks/_search
