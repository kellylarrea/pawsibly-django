#!/bin/bash

curl "http://localhost:8000/bookings/${ID}/" \
  --include \
  --request PATCH \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "mango": {
      "start_date": "'"${START_DATE}"'",
      "end_date": "'"${END_DATE}"'",
    }
  }'

echo
