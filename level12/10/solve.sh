curl -X 'GET' "http://www.bulldoghax.com/secret/codes" --cookie "timelock=$(curl -s http://www.bulldoghax.com/secret/spinner | grep number | cut -b 23-32)"
