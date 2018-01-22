#!/bin/sh
(crontab -l; echo "0 1 * * 0 python ~/email_scrape/scrape.py https://agents.farmers.com > ~/email_scrape/emails-$(date +%m-%d-%y).txt") | sort - | uniq - | crontab -
