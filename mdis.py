{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "gppass.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/TheCaduceus/Link-Bypasser/blob/main/Link-Pass.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Enter Adfly Link Below!**"
      ],
      "metadata": {
        "id": "rWggyWOjc2vK"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://1.bp.blogspot.com/-xUfQ3IdGsqw/V0CFRI9k84I/AAAAAAAAAjw/DLLzv392DVIgzG4jryRkd3EaulWtQ7nUwCLcB/s1600/earnwithadfly800x533.png' height=\"100\">\n",
        "#@title <b><center>Enter Adfly Link Below</center></b>\n",
        "print(\"Importing Files!\")\n",
        "import re\n",
        "import requests\n",
        "from base64 import b64decode\n",
        "from urllib.parse import unquote\n",
        "\n",
        "# ==========================================\n",
        "\n",
        "# adfly short url\n",
        "URL = \"\" #@param {type:\"string\"}\n",
        "print(\"You Have Entered:\")\n",
        "print(URL)\n",
        "print(\"Checking Link...\")\n",
        "'''\n",
        "404: Complete exception handling not found :(\n",
        "'''\n",
        "print(\"Bypassing Link...\")\n",
        "# ==========================================\n",
        "\n",
        "def decrypt_url(code):\n",
        "    a, b = '', ''\n",
        "    for i in range(0, len(code)):\n",
        "        if i % 2 == 0: a += code[i]\n",
        "        else: b = code[i] + b\n",
        "\n",
        "    key = list(a + b)\n",
        "    i = 0\n",
        "\n",
        "    while i < len(key):\n",
        "        if key[i].isdigit():\n",
        "            for j in range(i+1,len(key)):\n",
        "                if key[j].isdigit():\n",
        "                    u = int(key[i]) ^ int(key[j])\n",
        "                    if u < 10: key[i] = str(u)\n",
        "                    i = j\t\t\t\t\t\n",
        "                    break\n",
        "        i+=1\n",
        "    \n",
        "    key = ''.join(key)\n",
        "    decrypted = b64decode(key)[16:-16]\n",
        "\n",
        "    return decrypted.decode('utf-8')\n",
        "\n",
        "# ==========================================\n",
        "\n",
        "def adfly_bypass(url):\n",
        "    res = requests.get(url).text\n",
        "    \n",
        "    out = {'error': False, 'src_url': url}\n",
        "    \n",
        "    try:\n",
        "        ysmm = re.findall(\"ysmm\\s+=\\s+['|\\\"](.*?)['|\\\"]\", res)[0]\n",
        "    except:\n",
        "        out['error'] = True\n",
        "        return out\n",
        "        \n",
        "    url = decrypt_url(ysmm)\n",
        "\n",
        "    if re.search(r'go\\.php\\?u\\=', url):\n",
        "        url = b64decode(re.sub(r'(.*?)u=', '', url)).decode()\n",
        "    elif '&dest=' in url:\n",
        "        url = unquote(re.sub(r'(.*?)dest=', '', url))\n",
        "    \n",
        "    out['bypassed_url'] = url\n",
        "    \n",
        "    return out\n",
        "\n",
        "# ==========================================\n",
        "\n",
        "out = adfly_bypass(URL)\n",
        "\n",
        "print(out)\n"
      ],
      "metadata": {
        "cellView": "form",
        "id": "NRE5wW9wc85c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Enter GP-LINK Below!**"
      ],
      "metadata": {
        "id": "vIuY_F5gVVm2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://gplinks.in/img/gp-logo.png' height=\"100\">\n",
        "#@title <b><center>Enter GP-LINK Below</center></b>\n",
        "print(\"Downloading Cloud-Scraper...\")\n",
        "!pip install cloudscraper\n",
        "print(\"Setting Up!\")\n",
        "print(\"Performing Check...\")\n",
        "import time\n",
        "import requests\n",
        "import cloudscraper\n",
        "from bs4 import BeautifulSoup\n",
        "from urllib.parse import urlparse\n",
        "print(\"Everything Looks Good! Lets Continue.\")\n",
        "\n",
        "url = \"https://gplinks.co/bJXenY\" #@param {type:\"string\"} \n",
        "print(\"Entered Link:\")\n",
        "print(url)\n",
        "print(\"Checking Link...\")\n",
        "print(\"Checking Done!\")\n",
        "# ==============================================\n",
        "print(\"Bypassing the Link...\")\n",
        "def gplinks_bypass(url: str):\n",
        "    client = cloudscraper.create_scraper(allow_brotli=False)\n",
        "    p = urlparse(url)\n",
        "    final_url = f'{p.scheme}://{p.netloc}/links/go'\n",
        "    \n",
        "    res = client.head(url)\n",
        "    header_loc = res.headers['location']\n",
        "    param = header_loc.split('postid=')[-1]\n",
        "    req_url = f'{p.scheme}://{p.netloc}/{param}'\n",
        "    \n",
        "    p = urlparse(header_loc)\n",
        "    ref_url = f'{p.scheme}://{p.netloc}/'\n",
        "\n",
        "\n",
        "    h = {'referer': ref_url}\n",
        "    res = client.get(req_url, headers=h, allow_redirects=False)\n",
        "    bs4 = BeautifulSoup(res.content, 'html.parser')\n",
        "    inputs = bs4.find_all('input')\n",
        "    time.sleep(10) # !important\n",
        "    data = { input.get('name'): input.get('value') for input in inputs }\n",
        "    \n",
        "    h = {\n",
        "        'content-type': 'application/x-www-form-urlencoded',\n",
        "        'x-requested-with': 'XMLHttpRequest'\n",
        "    }\n",
        "    time.sleep(10)\n",
        "    res = client.post(final_url, headers=h, data=data)\n",
        "    try:\n",
        "        return res.json()['url'].replace('/','/')\n",
        "    except: return 'Something went wrong :('\n",
        "\n",
        "# ==============================================\n",
        "\n",
        "print(gplinks_bypass(url))\n",
        "print(\"Confirming Link...\")\n",
        "print(\"Successfully Bypassed!\")"
      ],
      "metadata": {
        "cellView": "form",
        "id": "PHCG2iGQgDhz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Enter GDTOT Link as well as your GDTOT Crypt! If you don't know how to get Crypt then <a href=\"https://www.youtube.com/watch?v=EfZ29CotRSU\">Learn Here</a>**"
      ],
      "metadata": {
        "id": "cyBiaGkAUtLi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://gdtot.one/assets/img/gdtot.png' height=\"100\">\n",
        "#@title <b><center>Enter GDTOT-LINK Below</center></b>\n",
        "print(\"Importing Files!\")\n",
        "import re\n",
        "import base64\n",
        "import requests\n",
        "from urllib.parse import urlparse, parse_qs\n",
        "\n",
        "URL = \"\" #@param {type:\"string\"}\n",
        "crypt = \"\" #@param {type:\"string\"}\n",
        "print(\"You have Entered:\")\n",
        "print(\"URL:\")\n",
        "print(URL)\n",
        "print(\"Crypt:\")\n",
        "print(crypt)\n",
        "# ==========================================\n",
        "print(\"Bypassing Link...\")\n",
        "def parse_info(res):\n",
        "    title = re.findall(\">(.*?)<\\/h5>\", res.text)[0]\n",
        "    info = re.findall('<td\\salign=\"right\">(.*?)<\\/td>', res.text)\n",
        "    parsed_info = {\n",
        "        'error': True,\n",
        "        'message': 'Link Invalid.',\n",
        "        'title': title,\n",
        "        'size': info[0],\n",
        "        'date': info[1]\n",
        "    }\n",
        "    return parsed_info\n",
        "\n",
        "# ==========================================\n",
        "\n",
        "def gdtot_dl(url):\n",
        "    client = requests.Session()\n",
        "    client.cookies.update({ 'crypt': crypt })\n",
        "    res = client.get(url)\n",
        "\n",
        "    info = parse_info(res)\n",
        "    info['src_url'] = url\n",
        "\n",
        "    res = client.get(f\"https://new.gdtot.top/dld?id={url.split('/')[-1]}\")\n",
        "    \n",
        "    try:\n",
        "        url = re.findall('URL=(.*?)\"', res.text)[0]\n",
        "    except:\n",
        "        info['message'] = 'The requested URL could not be retrieved.',\n",
        "        return info\n",
        "\n",
        "    params = parse_qs(urlparse(url).query)\n",
        "    \n",
        "    if 'msgx' in params:\n",
        "        info['message'] = params['msgx'][0]\n",
        "    \n",
        "    if 'gd' not in params or not params['gd'] or params['gd'][0] == 'false':\n",
        "        return info\n",
        "    \n",
        "    try:\n",
        "        decoded_id = base64.b64decode(str(params['gd'][0])).decode('utf-8')\n",
        "        gdrive_url = f'https://drive.google.com/open?id={decoded_id}'\n",
        "        info['message'] = 'Success.'\n",
        "    except:\n",
        "        info['error'] = True\n",
        "        return info\n",
        "\n",
        "    info['gdrive_link'] = gdrive_url\n",
        "    \n",
        "    return info\n",
        "    \n",
        "# ==========================================\n",
        "\n",
        "info = gdtot_dl(URL)\n",
        "\n",
        "print(info)\n",
        "print(\"Bypassed Successfully!\")"
      ],
      "metadata": {
        "cellView": "form",
        "id": "pJCdd8LESBAk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Enter Sharer.pw Link, XSRF_TOKEN and laravel_session cookies! If you don't know how to get then then watch this <a href=\"https://www.youtube.com/watch?v=EfZ29CotRSU\">Video</a> (for GDTOT) and do the same for Sharer.pw**"
      ],
      "metadata": {
        "id": "JlOUDYIzlLTD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://sharer.pw/images/logo2.png' height=\"30\">\n",
        "#@title <b><center>Enter Sharer.pw Link Below</center></b>\n",
        "print(\"Importing Files!\")\n",
        "import re\n",
        "import requests\n",
        "from lxml import etree\n",
        "\n",
        "url = \"\" #@param {type:\"string\"}\n",
        "\n",
        "XSRF_TOKEN = \"\" #@param {type:\"string\"}\n",
        "laravel_session = \"\" #@param {type:\"string\"}\n",
        "print(\"You have Entered:\")\n",
        "print(\"URL:\")\n",
        "print(url)\n",
        "print(\"XSRF_TOKEN:\")\n",
        "print(XSRF_TOKEN)\n",
        "print(\"laravel_session\")\n",
        "print(laravel_session)\n",
        "print(\"Bypassing Link...\")\n",
        "'''\n",
        "404: Exception Handling Not Found :(\n",
        "NOTE:\n",
        "DO NOT use the logout button on website. Instead, clear the site cookies manually to log out.\n",
        "If you use logout from website, cookies will become invalid.\n",
        "'''\n",
        "\n",
        "# ===================================================================\n",
        "\n",
        "def parse_info(res):\n",
        "    f = re.findall(\">(.*?)<\\/td>\", res.text)\n",
        "    info_parsed = {}\n",
        "    for i in range(0, len(f), 3):\n",
        "        info_parsed[f[i].lower().replace(' ', '_')] = f[i+2]\n",
        "    return info_parsed\n",
        "\n",
        "def sharer_pw_dl(url, forced_login=False):\n",
        "    client = requests.Session()\n",
        "    \n",
        "    client.cookies.update({\n",
        "        \"XSRF-TOKEN\": XSRF_TOKEN,\n",
        "        \"laravel_session\": laravel_session\n",
        "    })\n",
        "    \n",
        "    res = client.get(url)\n",
        "    token = re.findall(\"_token\\s=\\s'(.*?)'\", res.text, re.DOTALL)[0]\n",
        "    \n",
        "    ddl_btn = etree.HTML(res.content).xpath(\"//button[@id='btndirect']\")\n",
        "\n",
        "    info_parsed = parse_info(res)\n",
        "    info_parsed['error'] = True\n",
        "    info_parsed['src_url'] = url\n",
        "    info_parsed['link_type'] = 'login' # direct/login\n",
        "    info_parsed['forced_login'] = forced_login\n",
        "    \n",
        "    headers = {\n",
        "        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',\n",
        "        'x-requested-with': 'XMLHttpRequest'\n",
        "    }\n",
        "    \n",
        "    data = {\n",
        "        '_token': token\n",
        "    }\n",
        "    \n",
        "    if len(ddl_btn):\n",
        "        info_parsed['link_type'] = 'direct'\n",
        "    if not forced_login:\n",
        "        data['nl'] = 1\n",
        "    \n",
        "    try: \n",
        "        res = client.post(url+'/dl', headers=headers, data=data).json()\n",
        "    except:\n",
        "        return info_parsed\n",
        "    \n",
        "    if 'url' in res and res['url']:\n",
        "        info_parsed['error'] = False\n",
        "        info_parsed['gdrive_link'] = res['url']\n",
        "    \n",
        "    if len(ddl_btn) and not forced_login and not 'url' in info_parsed:\n",
        "        # retry download via login\n",
        "        return sharer_pw_dl(url, forced_login=True)\n",
        "    \n",
        "    return info_parsed\n",
        "\n",
        "# ===================================================================\n",
        "\n",
        "out = sharer_pw_dl(url)\n",
        "print(out)"
      ],
      "metadata": {
        "cellView": "form",
        "id": "jY_RrpdYiTqj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Enter DropLink Below!**"
      ],
      "metadata": {
        "id": "2PlnCgEllyT7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://i.imgur.com/1rWL0jS.png' height=\"50\">\n",
        "#@title <b><center>Enter Drop Link Below</center></b>\n",
        "print(\"Importing Files!\")\n",
        "import re\n",
        "import time\n",
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "from urllib.parse import urlparse\n",
        "\n",
        "\n",
        "# droplink url\n",
        "url = \"\" #@param {type:\"string\"}\n",
        "print(\"You Have Entered:\")\n",
        "print(url)\n",
        "print(\"Checking Link!\")\n",
        "# ==============================================\n",
        "print(\"Bypassing Link...\")\n",
        "def droplink_bypass(url):\n",
        "    client = requests.Session()\n",
        "    res = client.get(url)\n",
        "\n",
        "    ref = re.findall(\"action[ ]{0,}=[ ]{0,}['|\\\"](.*?)['|\\\"]\", res.text)[0]\n",
        "\n",
        "    h = {'referer': ref}\n",
        "    res = client.get(url, headers=h)\n",
        "\n",
        "    bs4 = BeautifulSoup(res.content, 'lxml')\n",
        "    inputs = bs4.find_all('input')\n",
        "    data = { input.get('name'): input.get('value') for input in inputs }\n",
        "\n",
        "    h = {\n",
        "        'content-type': 'application/x-www-form-urlencoded',\n",
        "        'x-requested-with': 'XMLHttpRequest'\n",
        "    }\n",
        "    p = urlparse(url)\n",
        "    final_url = f'{p.scheme}://{p.netloc}/links/go'\n",
        "\n",
        "    time.sleep(3.1)\n",
        "    res = client.post(final_url, data=data, headers=h).json()\n",
        "\n",
        "    return res\n",
        "\n",
        "# ==============================================\n",
        "\n",
        "print(droplink_bypass(url))"
      ],
      "metadata": {
        "cellView": "form",
        "id": "611_HcrXfOOr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Enter AppDrive or DriveApp and as well as there Account Details (Required for Login Required Links only)**"
      ],
      "metadata": {
        "id": "WlRAIhcUoVHb"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://i.imgur.com/sVViVY2.png' height=\"100\">\n",
        "#@title <b><center>Enter App Drive or Drive App Link Below</center></b>\n",
        "print(\"Importing Files!\")\n",
        "import re\n",
        "import requests\n",
        "from lxml import etree\n",
        "from urllib.parse import urlparse\n",
        "\n",
        "\n",
        "# Website User Account (NOT GOOGLE ACCOUNT) ----\n",
        "url = \"\" #@param {type:\"string\"}\n",
        "email = \"OPTIONAL\" #@param {type:\"string\"}\n",
        "passwd = \"OPTIONAL\" #@param {type:\"string\"}\n",
        "print(\"You have Entered:\")\n",
        "print(\"Link:\")\n",
        "print(url)\n",
        "print(\"Email:\")\n",
        "print(email)\n",
        "print(\"Password:\")\n",
        "print(passwd)\n",
        "# Destination config ----\n",
        "SHARED_DRIVE_ID = '' # team drive ID (optional) (for MyDrive, keep this field empty)\n",
        "FOLDER_ID = '' # drive folder ID (optional)\n",
        "\n",
        "'''\n",
        "NOTE: \n",
        " - Auto-detection for non-login urls, and indicated via 'link_type' (direct/login) in output.\n",
        "SUPPORTED DOMAINS:\n",
        " - appdrive.in\n",
        " - driveapp.in\n",
        " \n",
        "'''\n",
        "print(\"Bypassing Link...\")\n",
        "# ===================================================================\n",
        "\n",
        "def account_login(client, url, email, password):\n",
        "    data = {\n",
        "        'email': email,\n",
        "        'password': password\n",
        "    }\n",
        "    client.post(f'https://{urlparse(url).netloc}/login', data=data)\n",
        "\n",
        "def update_account(client, url, shared_drive_id, folder_id):\n",
        "    data = {\n",
        "        'root_drive': shared_drive_id,\n",
        "        'folder': folder_id\n",
        "    }\n",
        "    client.post(f'https://{urlparse(url).netloc}/account', data=data)\n",
        "\n",
        "def gen_payload(data, boundary=f'{\"-\"*6}_'):\n",
        "    data_string = ''\n",
        "    for item in data:\n",
        "        data_string += f'{boundary}\\r\\n'\n",
        "        data_string += f'Content-Disposition: form-data; name=\"{item}\"\\r\\n\\r\\n{data[item]}\\r\\n'\n",
        "    data_string += f'{boundary}--\\r\\n'\n",
        "    return data_string\n",
        "\n",
        "def parse_info(data):\n",
        "    info = re.findall('>(.*?)<\\/li>', data)\n",
        "    info_parsed = {}\n",
        "    for item in info:\n",
        "        kv = [s.strip() for s in item.split(':', maxsplit = 1)]\n",
        "        info_parsed[kv[0].lower()] = kv[1]\n",
        "    return info_parsed\n",
        "\n",
        "# ===================================================================\n",
        "\n",
        "def appdrive_dl(url):\n",
        "    client = requests.Session()\n",
        "    client.headers.update({\n",
        "        \"user-agent\": \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36\"\n",
        "    })\n",
        "\n",
        "    account_login(client, url, email, passwd)\n",
        "    update_account(client, url, SHARED_DRIVE_ID, FOLDER_ID)\n",
        "\n",
        "    res = client.get(url)\n",
        "    key = re.findall('\"key\",\\s+\"(.*?)\"', res.text)[0]\n",
        "\n",
        "    ddl_btn = etree.HTML(res.content).xpath(\"//button[@id='drc']\")\n",
        "\n",
        "    info_parsed = parse_info(res.text)\n",
        "    info_parsed['error'] = False\n",
        "    info_parsed['link_type'] = 'login' # direct/login\n",
        "    \n",
        "    headers = {\n",
        "        \"Content-Type\": f\"multipart/form-data; boundary={'-'*4}_\",\n",
        "    }\n",
        "    \n",
        "    data = {\n",
        "        'type': 1,\n",
        "        'key': key,\n",
        "        'action': 'original'\n",
        "    }\n",
        "    \n",
        "    if len(ddl_btn):\n",
        "        info_parsed['link_type'] = 'direct'\n",
        "        data['action'] = 'direct'\n",
        "    \n",
        "    while data['type'] <= 3:\n",
        "        try:\n",
        "            response = client.post(url, data=gen_payload(data), headers=headers).json()\n",
        "            break\n",
        "        except: data['type'] += 1\n",
        "        \n",
        "    if 'url' in response:\n",
        "        info_parsed['gdrive_link'] = response['url']\n",
        "    elif 'error' in response and response['error']:\n",
        "        info_parsed['error'] = True\n",
        "        info_parsed['error_message'] = response['message']\n",
        "    else:\n",
        "        info_parsed['error'] = True\n",
        "        info_parsed['error_message'] = 'Something went wrong :('\n",
        "    \n",
        "    if info_parsed['error']: return info_parsed\n",
        "    \n",
        "    if urlparse(url).netloc == 'driveapp.in' and not info_parsed['error']:\n",
        "        res = client.get(info_parsed['gdrive_link'])\n",
        "        drive_link = etree.HTML(res.content).xpath(\"//a[contains(@class,'btn')]/@href\")[0]\n",
        "        info_parsed['gdrive_link'] = drive_link\n",
        "        \n",
        "    info_parsed['src_url'] = url\n",
        "    \n",
        "    return info_parsed\n",
        "\n",
        "# ===================================================================\n",
        "\n",
        "print(appdrive_dl(url))\n"
      ],
      "metadata": {
        "cellView": "form",
        "id": "0vqE8a8dm5T4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        ""
      ],
      "metadata": {
        "id": "OY1CtzT0pA8u"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#@markdown <center><img src='https://linkvertise.com/assets/img/final-Logo.png' height=\"50\">\n",
        "#@title <b><center>Enter Linkvertise-LINK Below</center></b>\n",
        "import re\n",
        "import time\n",
        "import json\n",
        "import base64\n",
        "import requests\n",
        "\n",
        "# -------------------------------------------\n",
        "\n",
        "def lv_bypass(url):\n",
        "    client = requests.Session()\n",
        "    \n",
        "    headers = {\n",
        "        \"User-Agent\": \"AppleTV6,2/11.1\",\n",
        "        \"Content-Type\": \"application/json\",\n",
        "        \"Accept\": \"application/json\",\n",
        "    }\n",
        "    \n",
        "    client.headers.update(headers)\n",
        "    \n",
        "    url = url.replace(\"%3D\", \" \").replace(\"&o=sharing\", \"\").replace(\"?o=sharing\", \"\").replace(\"dynamic?r=\", \"dynamic/?r=\")\n",
        "    \n",
        "    id_name = re.search(r\"\\/\\d+\\/[^\\/]+\", url)\n",
        "    \n",
        "    if not id_name: return None\n",
        "    \n",
        "    paths = [\n",
        "        \"/captcha\", \n",
        "        \"/countdown_impression?trafficOrigin=network\", \n",
        "        \"/todo_impression?mobile=true&trafficOrigin=network\"\n",
        "    ]\n",
        "    \n",
        "    for path in paths:\n",
        "        url = f\"https://publisher.linkvertise.com/api/v1/redirect/link{id_name[0]}{path}\"\n",
        "        response = client.get(url).json()\n",
        "        if response[\"success\"]: break\n",
        "    \n",
        "    data = client.get(f\"https://publisher.linkvertise.com/api/v1/redirect/link/static{id_name[0]}\").json()\n",
        "\n",
        "    out = {\n",
        "        'timestamp':int(str(time.time_ns())[0:13]),\n",
        "        'random':\"6548307\", \n",
        "        'link_id':data[\"data\"][\"link\"][\"id\"]\n",
        "    }\n",
        "    \n",
        "    options = {\n",
        "        'serial': base64.b64encode(json.dumps(out).encode()).decode()\n",
        "    }\n",
        "    \n",
        "    data = client.get(\"https://publisher.linkvertise.com/api/v1/account\").json()\n",
        "    user_token = data[\"user_token\"] if \"user_token\" in data.keys() else None\n",
        "    \n",
        "    url_submit = f\"https://publisher.linkvertise.com/api/v1/redirect/link{id_name[0]}/target?X-Linkvertise-UT={user_token}\"\n",
        "    \n",
        "    data = client.post(url_submit, json=options).json()\n",
        "    \n",
        "    return data[\"data\"][\"target\"]\n",
        "\n",
        "# -------------------------------------------\n",
        "\n",
        "# Add URL\n",
        "url = \"https://domain.tld/XXXXXX/XXX\" #@param {type:\"string\"}\n",
        "bypassed = lv_bypass(url)\n",
        "\n",
        "print(bypassed)"
      ],
      "metadata": {
        "cellView": "form",
        "id": "4yV_DpjXpBXj"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}