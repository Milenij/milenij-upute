---
title: Pripremne radnje
tags:
  - fiskalizacija 2.0.
keywords: []
---
# Pripreme za Fiskalizaciju 2.0 u aplikaciji iSustav

Ovaj dokument opisuje promjene u **Adresaru kupaca i dobavljača** potrebne za prilagodbu Fiskalizaciji 2.0.

## Pregled procesa

Na izborniku **Matični -> Adresar kupaca, dobavljača** i do sada ste upisivali kupce/dobavljače kojima izdajete fakture i od kojih kupujete robu. Uvođenjem nove verzije, ovaj proces uključuje provjeru statusa u AMS sustavu.

## 1. Inicijalna provjera partnera

Nakon instalacije nove verzije aplikacije, prilikom prvog ulaska u adresar pojavit će se važno upozorenje.

!!! warning "Upozorenje sustava" Zbog Fiskalizacije 2.0 za sve upisane kupce potrebno je napraviti provjeru da li su obveznici primanja eRačuna.

### Postupak provjere

Za inicijalno ažuriranje podataka slijedite ove korake u sučelju Adresara:

1. Pronađite tekstualnu poveznicu (link) pri vrhu ekrana: **"Obavezna provjera svih partnera za eRačun F 2.0"**.
2. Kliknite mišem na taj tekst.
3. Aplikacija će proći kroz cijeli popis, po OIB-u potražiti klijente u AMS sustavu i ažurirati njihove podatke.

!!! note "Napomena o potpunosti podataka" Ovim ste obavili inicijalno ažuriranje. Ono ne mora biti potpuno jer većina klijenata možda još nije upisana u AMS. Podaci će se automatski provjeravati i kasnije, prilikom izdavanja računa.

## 2. Definiranje podataka o klijentu

Ukoliko želite ručno ispraviti ili provjeriti podatke, odaberite klijenta i pritisnite **Promjeni**.

\=== "Osnovne Postavke"

\=== "eRačun Postavke"

\=== "Provjera pojedinačnog klijenta"

## 3. Posebne kategorije i napomene

??? question "Što s inozemnim tvrtkama?" Ukoliko poslujete s tvrtkama koje su izvan Hrvatske, proces ostaje isti kao i prije.

??? info "Razlika: Javna nabava vs. Standardni eRačun" Iako se eRačuni šalju na isti način za obje kategorije, postoje razlike u podacima:

!!! success "Zaključak" Kada ste definirali tipove partnera i njihove statuse eRačuna, završili ste ažuriranje podataka o kupcima/dobavljačima. Aplikacija će ubuduće pri zaključivanju svakog transakcijskog računa automatski provjeravati status kupca u AMS-u.
