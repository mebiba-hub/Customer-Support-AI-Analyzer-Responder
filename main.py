from google import genai
import json
import os

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    print("BŁĄD: Brak klucza GEMINI_API_KEY w zmiennych środowiskowych!")
    exit()

client = genai.Client(api_key=API_KEY)

try:
    with open("zgloszenia_raw.json", "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    print("BŁĄD: Plik 'zgloszenia_raw.json' nie istnieje")
    exit()
except json.JSONDecodeError:
    print("BŁĄD: Plik 'zgloszenia_raw.json' zawiera błędny format JSON")
    exit()

prompt = f'''
Jesteś analitykiem danych przeanalizuj mi poniższy plik i stworz nowy plik json z kluczami:
'id_zgloszenia', 'klient' (imie i nazwisko), 'kategoria' (np. "Dostawa", "Uszkodzony sprzęt", "Pytanie o produkt", "Pochwała"),
'priorytet' ("Niski", "Średni", "Wysoki"),
'sentyment' ("Pozytywny", "Neutralny", "Negatywny"),
'sugerowana_odpowiedz' (krótka, profesjonalna odpowiedź dla klienta wygenerowana przez AI)
plik:{data}
'''

try:
    print("🤖 Wysyłanie zapytań do Gemini API (to może chwilę potrwać)...")
    response = client.models.generate_content(
        model='gemini-2.0-flash',
        contents=prompt,
        config={"response_mime_type": "application/json"}
    )

    raport = json.loads(response.text)

except Exception as e:
    print(f"Coś poszło nie tak podczas generowania raportu: {e}")
    exit()

try:
    with open("raport_zgloszen.json", "w", encoding="utf-8") as f:
        json.dump(raport, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Błąd podczas zapisu do pliku: {e}")
