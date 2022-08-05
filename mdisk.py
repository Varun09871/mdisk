#@markdown <center><img src='https://bit.ly/3bgOQWr' height="80">
#@title <b><center>Enter MDisk-Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper

url = "" #@param {type:"string"}
print("You have Entered:")
print("URL:")
print(url)
print("Generating Direct-Download Link...")
# -------------------------------------------

def mdisk(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "mdisk", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# -------------------------------------------

res = mdisk(url)

print(res)
print("Successfully Generated Direct-Download Link!")