#!/bin/sh
sudo pip install beautifulsoup4 html5lib
mkdir -p ~/bin
echo 'export PATH=$PATH:~/bin' >> ~/.bash_profile
cp run.sh ~/bin/scrape_farmers.sh
ln -s ~/bin/scrape_farmers.sh ~/bin/scrape_farmers

#(crontab -l; echo "0 1 * * 0 python ~/email_scrape/scrape.py https://agents.farmers.com > ~/email_scrape/emails-$(date +%m-%d-%y).txt") | sort - | uniq - | crontab -
