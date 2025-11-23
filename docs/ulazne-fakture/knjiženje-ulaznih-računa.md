---
title: Knjiženje Ulaznih Računa
category: Ulazne fakture
---
# Knjiženje Ulaznih Računa (URA)

Modul **Ulazne fakture** služi za evidentiranje svih računa primljenih od dobavljača za robu, materijal ili usluge. Pravilan unos ovih dokumenata osnova je za ispravan obračun PDV-a (Pretporeza) i vođenje knjige URA.

## Osnovni podaci dokumenta

Prilikom unosa nove ulazne fakture, sustav zahtijeva unos ključnih elemenata koji definiraju kako će se dokument knjižiti u financije i porezne evidencije.

* **Dobavljač:** Odabir poslovnog partnera iz matičnih podataka.
* **Broj računa:** Originalni broj s dokumenta dobavljača (npr. `123-01-1`).
* **Datumi:**
    * *Datum računa:* Datum kada je dobavljač izdao račun.
    * *Datum primitka:* Datum kada ste račun fizički zaprimili (bitno za rokove).
    * *Datum PDV-a:* Određuje u koji porezni period (mjesečni/kvartalni) račun ulazi.
* **Valuta plaćanja:** Datum do kojeg račun treba biti plaćen.

!!! warning "Važnost Datuma PDV-a"
    Obratite posebnu pozornost na **Datum PDV-a**. Ako račun s datumom iz prošlog mjeseca stigne nakon što ste već predali PDV obrazac, datum PDV-a morate staviti u tekući mjesec kako bi ušao u sljedeći obračun.

## Vrste Ulaznih Računa

Ovisno o prirodi troška, sustav razlikuje nekoliko tipova knjiženja (Vrste URA):

1.  **Redovna URA (Dobra i Usluge):** Standardni računi za robu, energiju, telefon, najam.
2.  **URA Uvoz:** Računi za robu iz trećih zemalja (izvan EU).
3.  **URA EU (Stjecanje):** Računi za robu/usluge iz Europske Unije (prijenos porezne obveze).
4.  **Predujmovi:** Računi za plaćene avanse.
5.  **Nepriznati trošak:** Računi za reprezentaciju ili osobna vozila (70/30% ili 50/50%).

## Povezivanje s Robnim (Primkama)

Ako koristite robno/materijalno knjigovodstvo, ulazna faktura se ne unosi ručno, već se **povezuje s Primkom**.

1.  Otvorite novu Ulaznu fakturu.
2.  Kliknite na gumb **"Povuci iz primke"** (ili *Import*).
3.  Odaberite primku kojom je roba zaprimljena na skladište.
4.  Sustav će automatski prepisati iznose i povezati robni ulaz s financijskim zaduženjem.

!!! tip "Automatsko Kontiranje"
    Nakon spremanja ulazne fakture, sustav automatski kreira temeljnicu u Glavnoj knjizi:
    * **Duguje:** Konto troška ili skladišta (klasa 3, 4 ili 6).
    * **Duguje:** Konto pretporeza (klasa 1).
    * **Potražuje:** Konto dobavljača (klasa 2).

## Statusi Računa

Svaka faktura prolazi kroz nekoliko statusa tijekom svog životnog ciklusa:
* **U pripremi:** Račun je unesen ali nije proknjižen (može se mijenjati).
* **Proknjižen:** Račun je ušao u porezne knjige i Glavnu knjigu (zaključan).
* **Likvidiran:** Račun je odobren za plaćanje od strane odgovorne osobe.
* **Plaćen:** Račun je zatvoren izvodom ili blagajnom.
