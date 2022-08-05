**Enter AdFly Link Below!**

#@markdown <center><img src='https://bit.ly/3zMaLOK' height="100">
#@title <b><center>Enter AdFly Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper
import re
from base64 import b64decode
from urllib.parse import unquote

# ==========================================

url = "" #@param {type:"string"}
print("You Have Entered:")
print(URL)
print("Checking Link...")
'''
404: Complete exception handling not found :(
'''
print("Bypassing Link...")
# ==========================================

def decrypt_url(code):
    a, b = '', ''
    for i in range(0, len(code)):
        if i % 2 == 0: a += code[i]
        else: b = code[i] + b
    key = list(a + b)
    i = 0
    while i < len(key):
        if key[i].isdigit():
            for j in range(i+1,len(key)):
                if key[j].isdigit():
                    u = int(key[i]) ^ int(key[j])
                    if u < 10: key[i] = str(u)
                    i = j					
                    break
        i+=1
    key = ''.join(key)
    decrypted = b64decode(key)[16:-16]
    return decrypted.decode('utf-8')

# ==========================================

def adfly(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    res = client.get(url).text
    out = {'error': False, 'src_url': url}
    try:
        ysmm = re.findall("ysmm\s+=\s+['|\"](.*?)['|\"]", res)[0]
    except:
        out['error'] = True
        return out
    url = decrypt_url(ysmm)
    if re.search(r'go\.php\?u\=', url):
        url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()
    elif '&dest=' in url:
        url = unquote(re.sub(r'(.*?)dest=', '', url))
    out['bypassed_url'] = url
    return out

# ==========================================

res = adfly(url)

print(res)
print("Successfully Bypassed!")

**Enter GPLinks Link Below!**

#@markdown <center><img src='https://gplinks.in/img/gp-logo.png' height="100">
#@title <b><center>Enter GPLinks Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Setting Up!")
print("Performing Check...")
import time
import cloudscraper
from bs4 import BeautifulSoup
from urllib.parse import urlparse
print("Everything Looks Good! Lets Continue.")

url = "" #@param {type:"string"} 
print("Entered Link:")
print(url)
print("Checking Link...")
print("Checking Done!")
print("Bypassing Link...")
# ==============================================

def gplinks(url: str):
    client = cloudscraper.create_scraper(allow_brotli=False)
    p = urlparse(url)
    final_url = f"{p.scheme}://{p.netloc}/links/go"
    res = client.head(url)
    header_loc = res.headers["location"]
    param = header_loc.split("postid=")[-1]
    req_url = f"{p.scheme}://{p.netloc}/{param}"
    p = urlparse(header_loc)
    ref_url = f"{p.scheme}://{p.netloc}/"
    h = {"referer": ref_url}
    res = client.get(req_url, headers=h, allow_redirects=False)
    bs4 = BeautifulSoup(res.content, "html.parser")
    inputs = bs4.find_all("input")
    time.sleep(10) # !important
    data = { input.get("name"): input.get("value") for input in inputs }
    h = {
        "content-type": "application/x-www-form-urlencoded",
        "x-requested-with": "XMLHttpRequest"
    }
    time.sleep(10)
    res = client.post(final_url, headers=h, data=data)
    try:
        return res.json()["url"].replace("/","/")
    except: 
        return "Could not Bypass your URL :("

# ==============================================

res = gplinks(url)

print(res)
print("Successfully Bypassed!")

**Enter GDTot Link as well as your GDTot Crypt! If you don't know how to get Crypt then <a href="https://www.youtube.com/watch?v=EfZ29CotRSU">Learn Here</a>**

#@markdown <center><img src='https://gdtot.sbs/assets/img/gdtot.png' height="100">
#@title <b><center>Enter GDTot-Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper
import re
import base64
from urllib.parse import urlparse, parse_qs

URL = "" #@param {type:"string"}
GDTot_Crypt = "b0lDek5LSCt6ZjVRR2EwZnY4T1EvVndqeDRtbCtTWmMwcGNuKy8wYWpDaz0%3D" #@param {type:"string"}
print("You have Entered:")
print("URL:")
print(url)
print("Crypt:")
print(GDTot_Crypt)
print("Generating GDrive Link...")
# ==========================================

def gdtot(url):
    client = cloudscraper.create_scraper(allow_brotli=False)
    match = re.findall(r"https?://(.+)\.gdtot\.(.+)\/\S+\/\S+", url)[0]
    client.cookies.update({ "crypt": GDTot_Crypt })
    res = client.get(url)
    res = client.get(f"https://{match[0]}.gdtot.{match[1]}/dld?id={url.split('/')[-1]}")
    url = re.findall(r'URL=(.*?)"', res.text)[0]
    info = {}
    info["error"] = False
    params = parse_qs(urlparse(url).query)
    if "gd" not in params or not params["gd"] or params["gd"][0] == "false":
        info["error"] = True
        if "msgx" in params:
            info["message"] = params["msgx"][0]
        else:
            info["message"] = "Invalid link"
    else:
        decoded_id = base64.b64decode(str(params["gd"][0])).decode("utf-8")
        drive_link = f"https://drive.google.com/open?id={decoded_id}"
        info["gdrive_link"] = drive_link
    if not info["error"]:
        return info["gdrive_link"]
    else:
        return "Could not generate GDrive URL for your GDTot Link :("

# ==========================================

res = gdtot(url)

print(res)
print("Generated GDRive Link Successfully!")

**Enter Sharer.pw Link, XSRF_TOKEN and laravel_session cookies! If you don't know how to get then then watch this <a href="https://www.youtube.com/watch?v=EfZ29CotRSU">Video</a> (for GDTOT) and do the same for Sharer.pw**

#@markdown <center><img src='https://sharer.pw/images/logo.png' height="50">
#@title <b><center>Enter Sharer.pw Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper
import re
from lxml import etree

url = "" #@param {type:"string"}
XSRF_TOKEN = "" #@param {type:"string"}
Laravel_Session = "" #@param {type:"string"}
print("You have Entered:")
print("URL:")
print(url)
print("XSRF_TOKEN:")
print(XSRF_TOKEN)
print("laravel_session")
print(Laravel_Session)
print("Bypassing Link...")
'''
404: Exception Handling Not Found :(
NOTE:
DO NOT use the logout button on website. Instead, clear the site cookies manually to log out.
If you use logout from website, cookies will become invalid.
'''

# ===================================================================

def parse_info(res):
    f = re.findall(">(.*?)<\/td>", res.text)
    info_parsed = {}
    for i in range(0, len(f), 3):
        info_parsed[f[i].lower().replace(' ', '_')] = f[i+2]
    return info_parsed

def sharer_pw(url, forced_login=False):
    client = cloudscraper.create_scraper(allow_brotli=False)
    client.cookies.update({
        "XSRF-TOKEN": XSRF_TOKEN,
        "laravel_session": Laravel_Session
    })
    res = client.get(url)
    token = re.findall("_token\s=\s'(.*?)'", res.text, re.DOTALL)[0]
    ddl_btn = etree.HTML(res.content).xpath("//button[@id='btndirect']")
    info_parsed = parse_info(res)
    info_parsed['error'] = True
    info_parsed['src_url'] = url
    info_parsed['link_type'] = 'login'
    info_parsed['forced_login'] = forced_login
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'x-requested-with': 'XMLHttpRequest'
    }
    data = {
        '_token': token
    }
    if len(ddl_btn):
        info_parsed['link_type'] = 'direct'
    if not forced_login:
        data['nl'] = 1
    try: 
        res = client.post(url+'/dl', headers=headers, data=data).json()
    except:
        return info_parsed
    if 'url' in res and res['url']:
        info_parsed['error'] = False
        info_parsed['gdrive_link'] = res['url']
    if len(ddl_btn) and not forced_login and not 'url' in info_parsed:
        # retry download via login
        return sharer_pw_dl(url, forced_login=True)
    return info_parsed

# ===================================================================

res = sharer_pw(url)

print(res)
print("Generated GDRive Link Successfully!")

**Enter DropLink Below!**

#@markdown <center><img src='https://i.imgur.com/1rWL0jS.png' height="75">
#@title <b><center>Enter Drop Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper

url = "" #@param {type:"string"}
print("You Have Entered:")
print(url)
print("Checking Link!")
print("Bypassing Link...")
# ==============================================

def droplink(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "droplink", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# ==============================================

res = droplink(url)

print(res)
print("Successfully Bypassed!")

**Enter AppDrive or DriveApp etc. Look-Alike Link and as well as the Account Details (Required for Login Required Links only)**

#@markdown <center><img src='https://i.imgur.com/sVViVY2.png' height="85">
#@title <b><center>Enter App Drive or Drive App Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper
import re
import requests
from lxml import etree
from urllib.parse import urlparse


# Website User Account (NOT GOOGLE ACCOUNT) ----
url = "" #@param {type:"string"}
Email = "OPTIONAL" #@param {type:"string"}
Password = "OPTIONAL" #@param {type:"string"}
print("You have Entered:")
print("Link:")
print(url)
print("Email:")
print(Email)
print("Password:")
print(Password)

'''
NOTE: 
 - Auto-detection for non-login urls, and indicated via 'link_type' (direct/login) in output.
SUPPORTED DOMAINS:
 - appdrive.in
 - driveapp.in
 - drivehub.in
 - gdflix.pro
 - drivesharer.in
 - drivebit.in
 - drivelinks.in
 - driveace.in
 - drivepro.in
 
'''
print("Generating GDrive Link...")

# ===================================================================

def unified(url):
    try:
        account = {"email": Email, "passwd": Password}
        client = cloudscraper.create_scraper(allow_brotli=False)
        client.headers.update(
            {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
            }
        )
        data = {"email": account["email"], "password": account["passwd"]}
        client.post(f"https://{urlparse(url).netloc}/login", data=data)
        res = client.get(url)
        key = re.findall('"key",\s+"(.*?)"', res.text)[0]
        ddl_btn = etree.HTML(res.content).xpath("//button[@id='drc']")
        info = re.findall(">(.*?)<\/li>", res.text)
        info_parsed = {}
        for item in info:
            kv = [s.strip() for s in item.split(":", maxsplit=1)]
            info_parsed[kv[0].lower()] = kv[1]
        info_parsed = info_parsed
        info_parsed["error"] = False
        info_parsed["link_type"] = "login"
        headers = {
            "Content-Type": f"multipart/form-data; boundary={'-'*4}_",
        }
        data = {"type": 1, "key": key, "action": "original"}
        if len(ddl_btn):
            info_parsed["link_type"] = "direct"
            data["action"] = "direct"
        while data["type"] <= 3:
            boundary = f'{"-"*6}_'
            data_string = ""
            for item in data:
                data_string += f"{boundary}\r\n"
                data_string += f'Content-Disposition: form-data; name="{item}"\r\n\r\n{data[item]}\r\n'
            data_string += f"{boundary}--\r\n"
            gen_payload = data_string
            try:
                response = client.post(url, data=gen_payload, headers=headers).json()
                break
            except BaseException:
                data["type"] += 1
        if "url" in response:
            info_parsed["gdrive_link"] = response["url"]
        elif "error" in response and response["error"]:
            info_parsed["error"] = True
            info_parsed["error_message"] = response["message"]
        else:
            info_parsed["error"] = True
            info_parsed["error_message"] = "Something went wrong :("
        if info_parsed["error"]:
            return info_parsed
        if urlparse(url).netloc == "driveapp.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        info_parsed["src_url"] = url
        if urlparse(url).netloc == "drivehub.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        if urlparse(url).netloc == "gdflix.pro" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link

        if urlparse(url).netloc == "drivesharer.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        if urlparse(url).netloc == "drivebit.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        if urlparse(url).netloc == "drivelinks.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        if urlparse(url).netloc == "driveace.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        if urlparse(url).netloc == "drivepro.in" and not info_parsed["error"]:
            res = client.get(info_parsed["gdrive_link"])
            drive_link = etree.HTML(res.content).xpath(
                "//a[contains(@class,'btn')]/@href"
            )[0]
            info_parsed["gdrive_link"] = drive_link
        if info_parsed["error"]:
            return "Faced an Unknown Error!"
        return info_parsed["gdrive_link"]
    except BaseException:
        return "Unable to Extract GDrive Link"

# ===================================================================

res = unified(url)

print(res)
print("Generated GDRive Link Successfully!")

**Enter Linkvertise Link Below!**

#@markdown <center><img src='https://linkvertise.com/assets/img/final-Logo.png' height="50">
#@title <b><center>Enter Linkvertise-Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper

url = "" #@param {type:"string"}
print("You have Entered:")
print("URL:")
print(url)
print("Bypassing the Link...")
# -------------------------------------------

def linkvertise(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "linkvertise", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# -------------------------------------------

res = linkvertise(url)

print(res)
print("Successfully Bypassed!")

**Enter MDisk Link Below!**

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



**Enter RockLinks Link Below!**

#@markdown <center><img src='https://bit.ly/3OGBD6Q' height="70">
#@title <b><center>Enter Rocklinks-Link Below</center></b>
print("Downloading Cloud-Scraper...")
!pip install cloudscraper
print("Importing Files!")
import cloudscraper

url = "" #@param {type:"string"}
print("You have Entered:")
print("URL:")
print(url)
print("Bypassing the Link...")
# -------------------------------------------

def rocklinks(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "rocklinks", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# -------------------------------------------

res = rocklinks(url)

print(res)
print("Successfully Bypassed!")

**Enter PixelDrain Link Below!**

#@markdown <center><img src='https://bit.ly/3ONNksy' height="80">
#@title <b><center>Enter PixelDrain-Link Below</center></b>
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

def pixeldrain(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "pixeldrain", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# -------------------------------------------

res = pixeldrain(url)

print(res)
print("Successfully Generated Direct-Download Link!")

**Enter WeTransfer Link Below!**

#@markdown <center><img src='https://bit.ly/3JjBbun' height="100">
#@title <b><center>Enter WeTransfer-Link Below</center></b>
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

def wetransfer(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "wetransfer", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# -------------------------------------------

res = wetransfer(url)

print(res)
print("Successfully Generated Direct-Download Link!")

**Enter MegaUp Link Below!**

#@markdown <center><img src='https://i.imgur.com/KbPSI7o.png' height="50">
#@title <b><center>Enter MegaUp-Link Below</center></b>
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

def megaup(url):
    api = "https://api.emilyx.in/api"
    client = cloudscraper.create_scraper(allow_brotli=False)
    resp = client.get(url)
    if resp.status_code == 404:
        return "File not found/The link you entered is wrong!"
    try:
        resp = client.post(api, json={"type": "megaup", "url": url})
        res = resp.json()
    except BaseException:
        return "API UnResponsive / Invalid Link !"
    if res["success"] is True:
        return res["url"]
    else:
        return res["msg"]

# -------------------------------------------

res = megaup(url)

print(res)
print("Successfully Generated Direct-Download Link!")