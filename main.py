from google import genai
import json
import os

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

with open("zgloszenia_raw.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

prompt = f'''
Jesteś analitykiem danych przeanalizuj mi poniższy plik i stworz nowy plik json z kluczami:
'id_zgloszenia', 'klient' (imie i nazwisko), 'kategoria' (np. "Dostawa", "Uszkodzony sprzęt", "Pytanie o produkt", "Pochwała"),
'priorytet' ("Niski", "Średni", "Wysoki"),
'sentyment' ("Pozytywny", "Neutralny", "Negatywny"),
'sugerowana_odpowiedz' (krótka, profesjonalna odpowiedź dla klienta wygenerowana przez AI)
plik:{data}
'''

response = client.models.generate_content(
    model='gemini-3.5-flash',
    contents=prompt,
    config={
            "response_mime_type": "application/json"
            }
)

raport = json.loads(response.text)

with open("raport_zgloszen.json", 'w', encoding='utf-8') as f:
    json.dump(raport, f, ensure_ascii=False, indent=4)