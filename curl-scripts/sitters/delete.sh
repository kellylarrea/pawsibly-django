#!/bin/bash

curl "http://localhost:8000/sitters/${ID}/" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
