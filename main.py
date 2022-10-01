import os.path

from bs4 import BeautifulSoup
import requests, json

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
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117',
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

        print("operation done!")

if __name__ == "__main__":
    main.download("https://nhentai.net/g/369508/")