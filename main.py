from pydantic import BaseModel, Field
from dotenv import load_dotenv
from google import genai
import json
import os

load_dotenv()

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

class ZgloszenieAnaliza(BaseModel):
    id_zgloszenie: str = Field(description="ID zgłoszenia np. ZGL-001")
    klient: str = Field(description="Imię i Nazwisko klienta")
    kategoria: str = Field(description="Kategoria zgloszenia np. Uszkodzony sprzet, Pytanie o produkt")
    priorytet: str = Field(description="Priorytet: niski, sredni, wysoki")
    sentyment: str = Field(description="Sentyment: pozytywny, negatywny, neutralny")
    sugerowana_odpowiedz: str = Field(description="Sugerowana profesionalna odpowiedz AI")

class RaportZgloszen(BaseModel):
    zgloszenia: list[ZgloszenieAnaliza]

prompt = f"Jesteć analitykiem danych, przeanalizuj te dane {data}"

try:
    print("Wysyłanie zapytań do Gemini API...")
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt,
        config={
                "response_mime_type": "application/json",
                "response_schema": RaportZgloszen
                }
    )

    raport = RaportZgloszen.model_validate_json(response.text)

except Exception as e:
    print(f"Coś poszło nie tak podczas generowania raportu: {e}")
    exit()

try:
    with open("raport_zgloszen.json", "w", encoding="utf-8") as f:
        f.write(raport.model_dump_json(indent=4, ensure_ascii=False))
except Exception as e:
    print(f"Błąd podczas zapisu do pliku: {e}")
