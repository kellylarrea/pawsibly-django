#!/bin/bash

curl "http://localhost:8000/sitters/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
