#!/bin/bash

chmod 777 executable.sh

python Python/scrape_aliexpress_reviews.py

echo "Scraping URLs done"

node scraped_data/scraping_code.js

echo "JavaScript script completed."
