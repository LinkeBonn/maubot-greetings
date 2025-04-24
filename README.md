# 🤖 WelcomeBot für Maubot – KV Bonn

Willkommen beim Maubot-Plugin `GreetingsBot`, entwickelt vom Kreisverband DIE LINKE Bonn.  
Dieses Plugin begrüßt neue Mitglieder im Matrix-Raum und informiert gleichzeitig einen IT-Raum über den Beitritt.  
Perfekt für solidarische Willkommensgrüße und transparente Kommunikation in der Struktur. ❤️

---

## ✨ Was macht das Plugin?

Sobald eine Person einem bestimmten Matrix-Raum beitritt:

- sendet der Bot eine individuelle Willkommensnachricht in den Raum (z. B. mit hilfreichen Links und Tipps)
- benachrichtigt zusätzlich einen anderen Raum (z. B. für das IT-Team), dass ein neuer Beitritt erfolgt ist

Alle Nachrichten können vollständig über die Konfiguration angepasst werden.

---

## 🔧 Konfiguration

Die Konfiguration erfolgt über drei Parameterbereiche:

```yaml
watch_room: "!raumid:server.de"  # Der Raum, in dem neue Mitglieder begrüßt werden
welcome_message: "👋 Willkommen {user}!"  # HTML-fähige Willkommensnachricht
notification_room: "!itraumid:server.de"  # Raum, in dem Benachrichtigungen ankommen
notification_message: "📥 {user} ist dem Raum {room} beigetreten."  # Nachricht für IT
```

In den Nachrichten kannst du folgende Platzhalter nutzen:

- `{user}` → wird durch den Link zur beitretenden Person ersetzt
- `{room}` → wird durch den Link zum Raum ersetzt

---

## 🧰 Installation & Nutzung

### 1. Plugin als `.mbp` Datei bauen

Wenn du das Plugin selbst bauen willst, brauchst du `maubot` und `mbc` installiert (siehe [maubot-Dokumentation](https://docs.mau.bot)):

```bash
mbc build
```

oder

```bash
zip -r greetings_bot.mbp greetings_bot.py maubot.yaml base-config.yaml
```

Dadurch wird eine Datei wie `de.linkebonn.greetingsbot-0.1.0.mbp` erstellt.  
Diese kannst du dann in deiner Maubot-Instanz hochladen.

Alternativ liegt eine `.mbp` Datei schon im Repository.

---

### 2. Plugin hochladen & aktivieren

- In der Maubot-Adminoberfläche unter `Plugins` die `.mbp` Datei hochladen
- Plugin aktivieren
- Konfiguration über die Oberfläche einfügen oder aus `base-config.yaml` kopieren und anpassen

---

## 🛡 Abhängigkeiten

Dieses Plugin nutzt:

- `mautrix` ≥ 0.10.0
- `maubot` ≥ 0.1.0

Stelle sicher, dass deine Maubot-Instanz kompatibel ist.

---

## 🧪 Beispielnachricht (für `welcome_message`)

```html
👋 <b>Hallo liebe Genoss*in {user}!</b><br><br>
Schön, dass du den Weg zu uns gefunden hast.<br>
Schau dich gerne in den Spaces um – vielleicht findest du dort direkt deine Ortsgruppe.<br>
Falls nicht: nur Mut – erstelle einfach selbst einen Raum! 💪<br><br>

🌐 Tritt auf jeden Fall unserem zentralen Space bei:<br>
➡️ <a href="https://matrix.to/#/#die-linke-bonn:linkebonn.de">#die-linke-bonn</a><br><br>

📣 Und verpasse keine Infos – abonniere auch den Ankündigungsraum:<br>
➡️ <a href="https://matrix.to/#/#Ankuendigungen:linkebonn.de">#Ankuendigungen</a><br><br>

🛠 Noch Fragen? Dann schau mal ins <a href="https://roteshandbuch.linkebonn.de">Kleine Rote Handbuch</a>.<br><br>

📰 Lust auf linke Lektüre?<br>
➡️ <a href="https://matrix.to/#/#roter-kiosk:linkebonn.de">#roter-kiosk</a><br><br>

Solidarische Grüße  
<b>strgLeft</b> ✊
```

---


Solidarische Grüße  
**strgLeft von DIE LINKE KV Bonn** ✊
