#!/bin/bash

curl "http://localhost:8000/pets/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo