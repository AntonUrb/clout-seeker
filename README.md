## Implementation of "Passive"
### What is OSINT

OSINT stands for Open Source Intelligence. It refers to the process of collecting and analyzing publicly available information from open sources, such as websites, social media, news articles, and government records, to gather intelligence and insights. OSINT is often used by various entities, including law enforcement agencies, government organizations, businesses, and individuals, for purposes such as security assessments, threat analysis, investigations, and competitive intelligence.

### How to use

Install requirements with ``pip install -r requirements. txt``. You need latest Chrome installed (122).
This script has 3 main features: 
 - **Full name search** <br>
Use command ``py passive.py -fn "Jean Dupont"`` to search for first and lastname. This goes into online phonebooks to parse results.
 - **IP Search** <br>
Use command `py passive.py -ip 127.0.0.1` to search IP address info. Uses free & publicly available JSON API.
 - **Username checker**
Use command ``py passive.py -u "@user01"`` to check username availability across 5 sites. Checks availabilities via APIs and by directly visiting website. For example Twitter shows the userpage very briefly if it exists, otherwise shows permanent "User not found" page.

### How does it work

Script parses info from publicly available websites using http requests and Chrome Selenium automation. Overuse may trigger bot protection services.

You can check video here: [DropBox](https://www.dropbox.com/scl/fi/ivms0nn3hzw6uxgoqe5am/passive.mkv?rlkey=iyw4i62ni0uwdn5vmg41j28gg&dl=0)<br>
Audit questions are here: [Audit](https://github.com/01-edu/public/tree/master/subjects/cybersecurity/passive/audit)