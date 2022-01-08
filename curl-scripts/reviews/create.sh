#!/bin/bash

curl "http://localhost:8000/mangos/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "review": {
      "review": "'"${REVIEW}"'",
      "rating": "'"${RATING}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo