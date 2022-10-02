from bs4 import BeautifulSoup
import requests, json, os

class main():
    def download(url:str):
        with open("cookies.json", "r", encoding="utf-8") as file:
            cookies = json.loads(file.read())

            cookies = {
                "cf_clearance": cookies["cookies"]["cf_clearance"],
                "csrftoken": cookies["cookies"]["csrftoken"]
            }

        headers = {
            'authority': 'nhentai.net',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0', 
            'referer': 'https://nhentai.net/',
            'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        }

        response = requests.get(url, cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        for i in soup.find_all("a", {"class": "gallerythumb"}):
            response = requests.get("https://nhentai.net" + i["href"], cookies=cookies, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            link = soup.find_all("img")[1]["src"]
            name = link.split("/")

            if os.path.isdir(f"./{name[4]}"):
                response = requests.get(link, cookies=cookies, headers=headers)
                with open(f"./{name[4]}/{name[4]}-{name[5]}", "wb") as file:
                    file.write(response.content)
                print(f"{name[4]}-{name[5]} - Done!")
            else:
                os.mkdir(f"./{name[4]}")
                with open(f"./{name[4]}/{name[4]}-{name[5]}", "wb") as file:
                    file.write(response.content)
                print(f"{name[4]}-{name[5]} - Done!")

        print("Operating Done!" + f" Saved on /{name[4]} folder\n")

if __name__ == "__main__":
    os.system("cls")
    while True:
        nhentai = input("NHentai Link or ID: ")
        if "https://nhentai.net/g/" in nhentai:
            try:
                main.download(nhentai)
            except Exception as err:
                print("Error: ", err)
        else:
            try:
                main.download("https://nhentai.net/g/" + nhentai)
            except Exception as err:
                print("Error: ", err)