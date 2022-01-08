#!/bin/bash

curl "http://localhost:8000/bookings/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
