#!/bin/bash
TOKEN_ENDPOINT='https://accounts.spotify.com/api/token'
SERVICE_ENDPOINT='https://api.spotify.com/v1/browse/new-releases?country=JP&limit=30'

CLIENT_ID=''
CLIENT_SECRET=''

RAW_JSON=$(curl -su "$CLIENT_ID:$CLIENT_SECRET" $TOKEN_ENDPOINT -X POST -d grant_type=client_credentials)
TOKEN=$(echo $RAW_JSON | jq '.access_token' | tr -d '"')

NEWRELEASES_JSON=$(curl ${SERVICE_ENDPOINT} -X GET -H "Authorization: Bearer $TOKEN")
FILE_NAME=$(date "+%Y_%m_%d")

echo $NEWRELEASES_JSON | jq '.albums.items | map({name: .name, artist: .artists[].name, date: .release_date})' >./datasets/$FILE_NAME.json
