#!/bin/bash

# Check if a URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL using curl and store the response body in a temporary file
response=$(curl -s -o temp_response.txt -w "%{size_download}" "$1")

# Display the size of the response body
echo "Size of the response body: $response bytes"

# Clean up temporary file
rm -f temp_response.txt
