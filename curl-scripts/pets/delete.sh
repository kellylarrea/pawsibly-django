#!/bin/bash

curl "http://localhost:8000/pets/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo