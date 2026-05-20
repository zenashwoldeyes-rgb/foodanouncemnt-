import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_IDS  = [c.strip() for c in os.environ["TELEGRAM_CHAT_ID"].split(",") if c.strip()]

GROUPS = [
    "Frey & Meseret",
    "Mekdes & Zufan",
    "Winta, Mahlet & Hilina",
    "Fikrte, Mita & Aynalem",
    "Addis, Etabez & Yodit",
]

# Reference: Wednesday May 20, 2026 — first scheduled run at the new 6 PM time;
# rotation starts with Frey & Meseret (GROUPS[0]).
REFERENCE_WEDNESDAY = datetime(2026, 5, 20, tzinfo=timezone.utc)

def get_group():
    now = datetime.now(timezone.utc)
    weeks = (now - REFERENCE_WEDNESDAY).days // 7
    return GROUPS[weeks % len(GROUPS)]

def send_message(name):
    text = (
        f"እንደምን አደራችሁ፣ በዚህ በሚመጣው እሑድ ጸበል ጻድቅ "
        f"ይዘው የሚመጡት {name} መሆናቸውን ለማሳወቅ ነው። እናመሰግናለን።"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    for chat_id in CHAT_IDS:
        response = requests.post(url, json={"chat_id": chat_id, "text": text})
        response.raise_for_status()
        print(f"[OK] Message sent for {name} to chat {chat_id}")

if __name__ == "__main__":
    group = get_group()
    send_message(group)
