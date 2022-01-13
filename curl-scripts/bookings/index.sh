#!/bin/bash

curl "http://localhost:8000/bookings/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
