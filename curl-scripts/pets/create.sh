#!/bin/bash

curl "http://localhost:8000/pets/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "pet": {
      "name": "'"${NAME}"'"
    }
  }'

echo
