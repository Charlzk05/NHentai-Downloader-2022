## NHentai Downloader 2022
- [Also check out NHentai Scraper](https://github.com/Charlzk05/NHentai-Scraper-2022)

NHentai Downloader that uses requests and cookies to bypass cloudflare

### Installation
1. Clone the repository ``git clone https://github.com/Charlzk05/NHentai-Downloader-2022.git``
2. Install requirements ``pip install -r requirements.txt``

### Usage
1. Go to your cloned repo folder
2. Get your **cf_clearance** and **csrftoken** cookie on [nhentai.net](https://nhentai.net/)

  ![image](https://user-images.githubusercontent.com/104715127/193413180-2271c533-4964-4969-bbbe-3afd71e9a623.png)
  ![image](https://user-images.githubusercontent.com/104715127/193413192-3ee30ce7-62f9-47ed-a49e-59c23fd17c39.png)

3. Replace **cf_clearance** and **csrftoken** on cookie.json with your cookies
4. Run the main.py with ``py main.py``
5. Your downloaded manga will be saved on the same folder with the name of the manga ID
