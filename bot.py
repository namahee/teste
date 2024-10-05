from whatsapp_api_client_python import API
import feedparser as fp
import time

g = API.GreenAPI(
    "7103129731", "14417425b16340fab8ae2245a924e7505a7b4bbb4f4c4c4aaa"
)
url = "https://www.youtube.com/feeds/videos.xml?channel_id=UC9_S4Lv-72TjmQBR79bAyDg"

def send_message(number, message):
    g.sending.sendMessage(f"{number}@c.us", message)

last_id = None
def check():
    global last_id
    feed = fp.parse(url)
    entry = feed.entries[0]
    id = entry.id
    if id != last_id:
        last_id = id
        send_message("559992004698", f"Vídeo novo, porra.\n{entry.title}\nToma o link: {entry.link}")
while True:
    check()
    time.sleep(5)
