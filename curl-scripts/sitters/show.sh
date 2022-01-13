#!/bin/bash

curl "http://localhost:8000/sitters/${ID}/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
