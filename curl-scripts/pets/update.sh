#!/bin/bash

curl "http://localhost:8000/pets/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "pet": {
      "name": "'"${NAME}"'",
    }
  }'

echo
