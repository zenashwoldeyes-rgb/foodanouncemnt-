import os
import requests
from datetime import datetime, timezone

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"].strip().lstrip("﻿")
CHAT_ID   = os.environ["TELEGRAM_CHAT_ID"].strip().lstrip("﻿")

GROUPS = [
    "Addis, Etabez & Yodit",
    "Frey & Meseret",
    "Mekdes & Zufan",
    "Winta, Mahlet & Hilina",
    "Fikrte, Mita & Aynalem",
]

# Reference: Wednesday May 13, 2026 (first announcement for Sunday May 17)
REFERENCE_WEDNESDAY = datetime(2026, 5, 13, tzinfo=timezone.utc)

def get_group():
    now = datetime.now(timezone.utc)
    weeks = (now - REFERENCE_WEDNESDAY).days // 7
    return GROUPS[weeks % len(GROUPS)]

def send_message(name):
    text = (
        f"ሰላም ለሁላችሁም፣ በዚህ በሚመጣው እሑድ ጸበል ጻድቅ "
        f"ይዘው የሚመጡት {name} መሆናቸውን ለማሳወቅ ነው። እናመሰግናለን።"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    response = requests.post(url, json={"chat_id": CHAT_ID, "text": text})
    response.raise_for_status()
    print(f"✅ Message sent for: {name}")

if __name__ == "__main__":
    group = get_group()
    send_message(group)