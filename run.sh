#!/bin/bash
mkdir -p ~/scraped_emails
python scrape.py https://agents.farmers.com > ~/scraped_emails/emails_$(date +%m-%d-%y_agents.farmers.com.txt)
