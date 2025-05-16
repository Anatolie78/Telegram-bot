
import schedule
import time
import requests

# Datele pentru bot și utilizator
token = "7432955855:AAE3LcN6lFc0tUjlCkittKSuG8hRRXOIcb4"
user_id = "5199023715"
url = f"https://api.telegram.org/bot{token}/sendMessage"

# Funcție de trimitere mesaj
def send_message(text):
    data = {
        "chat_id": user_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, data=data)
    print(response.json())

# Definire asistenți și mesaje
def send_structura_lemn():
    send_message("🪵 *StructuraLemnGPT*:\nPropuneri tehnice și optimizări pentru structuri din lemn.")

def send_energie():
    send_message("🔋 *EnergieGPT*:\nAnalize de eficiență energetică și strategii nZEB.")

def send_marketing():
    send_message("📢 *MarketingEcoGPT*:\nIdei de promovare și campanii de marketing pentru case din lemn.")

def send_astrovis():
    send_message("🔮 *AstroVisGPT*:\nInterpretări astrologice și reflecții simbolice.")

def send_dietolog():
    send_message("🍏 *DietologGPT*:\nMeniu zilnic pentru slăbire și sănătate.")

def send_audit():# Test de conectare manuală
    send_message("📝 *AuditGPT*:\nVerificări de conformitate și strategii pentru audituri energetice.")
# Test de conectare manuală
send_message("🚀 Test de conectare din Replit! Totul funcționează!")


# Programare mesaje la ore fixe
schedule.every().day.at("06:00").do(send_structura_lemn)
schedule.every().day.at("06:15").do(send_energie)
schedule.every().day.at("06:30").do(send_marketing)
schedule.every().day.at("06:45").do(send_astrovis)
schedule.every().day.at("07:00").do(send_dietolog)
schedule.every().day.at("07:15").do(send_audit)

# Rulare program continuu
print("Botul este activ și așteaptă să trimită mesajele programate...")
# Test de programare - trimite un mesaj la fiecare 10 secunde
print("🔄 Test de programare la 10 secunde...")

# Mesaje de debug
print("🟢 Programul a pornit și așteaptă să trimită mesaje...")

while True:
    schedule.run_pending()
    time.sleep(1)

send_message("🚀 Test de conectare din Replit! Totul funcționează!")
schedule.every(10).seconds.do(send_structura_lemn)
# Test de programare - trimite un mesaj la fiecare 10 secunde
print("🔄 Test de programare la 10 secunde...")
schedule.every(10).seconds.do(send_structura_lemn)
import time
print("Ora serverului este: ", time.strftime("%H:%M:%S"))
