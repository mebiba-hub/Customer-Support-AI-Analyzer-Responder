#  Customer Support AI Analyzer & Responder

Automatyczny system napisany w języku Python, służący do analizy, kategoryzacji oraz priorytetyzacji zgłoszeń klientów w e-commerce przy użyciu **Google Gemini API**.

Projekt pobiera surowe zgłoszenia w formacie JSON, analizuje je pod kątem emocji klienta oraz problemu, a następnie generuje ustrukturyzowany raport wraz z gotowymi, profesjonalnymi odpowiedziami dla zespołu obsługi klienta.

---

##  Główne funkcje

* **Automatyczna kategoryzacja:** Klasyfikacja zgłoszeń na kategorie (np. *Dostawa*, *Uszkodzony sprzęt*, *Pytanie o produkt*, *Pochwała*, *Rozliczenia*).
* **Analiza sentymentu:** Określanie wydźwięku wypowiedzi klienta (*Pozytywny*, *Neutralny*, *Negatywny*).
* **System priorytetów:** Automatyczne nadawanie wagi zgłoszeniom (*Niski*, *Średni*, *Wysoki*) w zależności od problemu.
* **Sugerowanie odpowiedzi:** Generowanie gotowych, profesjonalnych szkiców odpowiedzi dla konsultantów.
* **Structured Output (JSON):** Wymuszenie czystego formatu danych z modeli LLM, idealnego do dalszej integracji z systemami CRM lub bazami danych.

---

##  Technologie

* **Python 3.x**
* **Google GenAI SDK** (`google-genai`)
* **JSON** (do przetwarzania danych wejściowych i wyjściowych)

---

##  Struktura projektu

*  **`main.py`** — Główny skrypt logiczny przetwarzający dane z Gemini API
*  **`zgloszenia_raw.json`** — Surowe dane wejściowe ze zgłoszeniami
*  **`raport_zgloszen.json`** — Wygenerowany raport wyjściowy z analizą AI
*  **`requirements.txt`** — Lista wymaganych bibliotek Pythona
*  **`README.md`** — Dokumentacja projektu

---

##  Jak uruchomić projekt?

```bash
# 1. Klonowanie repozytorium
git clone [https://github.com/TWOJ_NICK/nazwa-repozytorium.git](https://github.com/TWOJ_NICK/nazwa-repozytorium.git)
cd nazwa-repozytorium

# 2. Instalacja zależności
pip install -r requirements.txt

# 3. Ustawienie klucza API (wybierz komendę dla swojego systemu)
# Windows (CMD):        set GEMINI_API_KEY=twój_klucz_api
# Windows (PowerShell):  $env:GEMINI_API_KEY="twój_klucz_api"
# Linux / macOS:        export GEMINI_API_KEY="twój_klucz_api"

# 4. Uruchomienie skryptu
python main.py
