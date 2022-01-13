#!/bin/bash

curl "http://localhost:8000/mangos/" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "sitter": {
      "first_name": "'"${FIRSTNAME}"'",
      "last_name": "'"${LASTNAME}"'",
      "email": "'"${EMAIL}"'",
      "zipcode": "'"${ZIPCODE}"'"
      "supersitter": "'"${SUPERSITTER}"'"
      "pricing": "'"${PRICING}"'"
      "pricing": "'"${PRICING}"'"
      "numReviews": "'"${NUMREVIEWS}"'"
      "rating": "'"${RATING}"'"
    }
  }'

echo