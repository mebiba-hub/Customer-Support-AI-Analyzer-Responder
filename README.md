# Customer Support AI Analyzer & Responder

Automatyczny system napisany w języku Python, służący do analizy, kategoryzacji oraz priorytetyzacji zgłoszeń klientów w e-commerce przy użyciu Google Gemini API oraz Pydantic.

Projekt pobiera surowe zgłoszenia w formacie JSON, analizuje je pod kątem emocji klienta oraz problemu, a następnie generuje ustrukturyzowany raport wraz z gotowymi odpowiedziami dla zespołu obsługi klienta.

---

## Główne funkcje

* **Automatyczna kategoryzacja:** Klasyfikacja zgłoszeń na kategorie (Dostawa, Uszkodzony sprzęt, Pytanie o produkt, Pochwała, Rozliczenia).
* **Analiza sentymentu:** Określanie wydźwięku wypowiedzi klienta (Pozytywny, Neutralny, Negatywny).
* **System priorytetów:** Automatyczne nadawanie wagi zgłoszeniom (Niski, Średni, Wysoki) w zależności od problemu.
* **Sugerowanie odpowiedzi:** Generowanie gotowych szkiców odpowiedzi dla konsultantów.
* **Gwarantowany walidowany JSON (Pydantic):** Użycie ścisłego schematu danych (`response_schema`), co eliminuje błędy formatowania i gwarantuje spójność odpowiedzi z AI.
* **Obsługa błędów:** Bezpieczna obsługa brakujących plików, błędów sieciowych czy niepoprawnych danych.

---

## Technologie

* **Python 3.x**
* **Google GenAI SDK** (`google-genai`)
* **Pydantic** (Walidacja i strukturyzacja danych)
* **python-dotenv** (Zarządzanie zmiennymi środowiskowymi)

---

## Struktura projektu

* `main.py` — Główny skrypt logiczny przetwarzający dane i łączący się z Gemini API
* `zgloszenia_raw.json` — Surowe dane wejściowe ze zgłoszeniami klientów
* `raport_zgloszen.json` — Wygenerowany raport wyjściowy z walidacją Pydantic
* `.env` — Lokalny plik z kluczem API (ignorowany przez Git)
* `.env.example` — Wzorzec pliku konfiguracyjnego
* `requirements.txt` — Lista wymaganych bibliotek Pythona
* `README.md` — Dokumentacja projektu

---

## Jak uruchomić projekt?

1. Klonowanie repozytorium:
   git clone [https://github.com/mebiba-hub/Customer-Support-AI-Analyzer-Responder.git]
   
   cd nazwa-repozytorium

3. Instalacja zależności:
   pip install -r requirements.txt

4. Konfiguracja klucza API:
   Stwórz plik .env w głównym folderze projektu (możesz skopiować .env.example) i wklej swój klucz API:
   GEMINI_API_KEY=twój_klucz_api

5. Uruchomienie skryptu:
   python main.py
