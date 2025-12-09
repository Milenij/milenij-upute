---
title: Adresar
tags:
  - fiskalizacija 2.0.
keywords:
  - adresar
---
## Adresar kupaca, dobavljača

U izborniku **Matični -> Adresar kupaca, dobavljača** upisuju se kupci i dobavljači kojima izdajete fakture i od kojih kupujete robu.

Nakon instalacije nove verzije aplikacije, prilikom prvog ulaska u adresar pojavit će se važno upozorenje. Zbog Fiskalizacije 2.0, potrebno je provjeriti jesu li upisani klijenti prijavljeni u AMS sustav.

!!! warning "Važno upozorenje"
    Pojavit će se poruka da je za sve upisane kupce potrebno napraviti provjeru jesu li obveznici primanja eRačuna.

## Automatska provjera klijenata

Za inicijalno ažuriranje podataka, slijedite ove korake:

1. U adresaru kliknite mišem na crveni tekst: **Obavezna provjera svih partnera za eRačun F 2.0**.
2. Program će proći kroz cijeli popis partnera.
3. Po OIB-u će potražiti koji se od upisanih klijenata nalaze u AMS sustavu i automatski ažurirati njihove podatke.

Ovim postupkom obavljate inicijalno ažuriranje koje možda neće biti potpuno jer većina klijenata još nije upisana u AMS.

![]()

## Ručna izmjena podataka o klijentu

Ako želite ručno ispraviti ili dopuniti podatke o klijentu, odaberite ga iz liste i pritisnite gumb **Promjeni**.

S uvođenjem Fiskalizacije 2.0, podatak o poreznom statusu pojedinog klijenta mora biti točno upisan. Ovo se odnosi na korisnike koji koriste aplikaciju za knjigovodstvo.

### Obavezni podaci za definiranje

Za svakog klijenta potrebno je definirati sljedeće parametre:

* **Tip:** Označite je li partner dobavljač, kupac ili ostalo (najbolje je označiti da je i kupac i dobavljač).
* **Porezni status:** Odaberite ispravan status iz ponuđene liste (npr. Obveznik PDV-a).
    
* **eRačun F 2.0 status:** Odaberite odgovarajući status iz liste.

### Provjera statusa u AMS-u

Ako ne znate status klijenta za eRačun:

1. Kliknite na link **eRačun F 2.0** unutar prozora za uređivanje partnera.
2. Aplikacija će se spojiti na AMS i provjeriti status klijenta.

!!! info "Napomena o statusu"
    U početku ćete često dobiti odgovor da se korisnik ne nalazi u sustavu AMS-a jer većina obveznika još nije prijavljena.

```
Kasnije, prilikom zaključivanja svakog računa s transakcijskim plaćanjem, program će automatski provjeriti nalazi li se kupac u AMS-u prije izdavanja računa.
```

## Kategorije obveznika eRačuna

Postoje dvije kategorije obveznika kojima je obavezno slanje eRačuna:

1. **Obavezno slanje eRačuna**
2. **Obavezno slanje eRačuna - javna nabava**

eRačuni se šalju na isti način za obje kategorije. Međutim, za obveznike **javne nabave**, program će prilikom knjiženja ponuditi upis dodatnih podataka koje naručitelj traži, kao što su broj narudžbenice, vrsta poslovne jedinice, pretinac ili broj ugovora.

!!! tip "Inozemni partneri"
    Ako poslujete s tvrtkama izvan Hrvatske, njima i dalje šaljete račune kao i do sada (poštom ili e-mailom).
