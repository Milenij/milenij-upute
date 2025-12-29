---
title: Slanje računa
tags:
  - fiskalizacija 2.0
keywords:
  - slanje-racuna
---
Podatak koji je potrebno upisati prilikom izrade svakog računa koji će se slati kao eRačun. Ovo je i do sad bila obveza kod izrade eRačuna, samo što je sad to stavljeno u zaglavlje računa, dok ste ranije to birali tek prilikom slanja eRačuna.

## Slanje eRačuna

Prilikom izrade računa, postoji mogućnost slanja eRačuna automatski (odmah nakon knjiženja) ili naknadnog slanja.

* **Automatski**: Odmah nakon knjiženja.
* **Naknadno**: Dobivate mogućnost upisa dodatnih podataka uz račun (broj narudžbenice, ugovora…) ili dodavanja privitaka (dokumenti otpremnica, narudžbenica i sl.).

!!! abstract "Kako promijeniti način slanja?"
    U polju *Tip računa eRačun*, program ponudi opciju **eRačun (odmah šalji)**.
    Kliknete li mišem na to polje, tekst će se promijeniti u: **eRačun (dod. podaci)**.
    
    Klikanjem miša na to polje mijenjate stanje načina slanja eRačuna: *odmah* ili *naknadno*.

## Pregled eRačuna / dodatni podaci / informacije

U svim modulima programa, kada kliknete na karticu **eRačun** otvara se tablica s popisom eRačuna. Korisnici koji su do sada slali eRačune ovo su koristili i prije. Sada ovaj dio koriste svi obveznici F2.

Ova se tablica koristi za:
1.  Eventualni upis dodatnih podataka o računu (broj narudžbe, ugovora itd.)
2.  Provjeru statusa izrađenih računa.

### Statusi računa

Kolona **Status** prikazuje u kojem se statusu (stanju) nalazi pojedini račun.

??? details "Popis statusa koje račun može poprimiti"
    * **Nedovršeno**: Kada na računu još trebate dodati neke podatke (ugovor, narudžbenica, otpremnice…).
    * **Za slanje**: Račun je dovršen i spreman za slanje.
    * **Isporučeno**: Račun je uspješno poslan u ulazni pretinac kupca.
    * **Odobreno**: Kupac je račun zaprimio i odobrio.
    * **Odbijeno**: Kupac je račun odbio. Razlog odbijanja možda ćete moći vidjeti u kartici *Status slanja*. Ako se ne vidi, morate ga potražiti na portalu vašeg informacijskog posrednika.
    * **Plaćeno**: Račun je plaćen u cijelosti.
    * **Dio plaćen**: Plaćen je samo dio iznosa računa.
    * **Neuspjelo**: Vaš informacijski posrednik nije uspio proslijediti račun krajnjem kupcu. Razlog provjerite u kartici *Status slanja*.

### Funkcije dugmadi

=== "Glavne naredbe"
    * **Šalji eRačun**: Pokretanje slanja eRačuna koji imaju status *Za slanje* ili *Nedovršeno*. Ako račun ima neki drugi status, dugme neće reagirati.
    * **Provjeri status**: Kad uspješno pošaljete račun, zaprimanje treba biti odobreno od strane primatelja. Tek tada možete reći da je kupac uspješno zaprimio račun.
    * **XML snimi**: Arhiva originala poslanog računa. Za potrebe kontrole/nadzora svaki račun možete snimiti u originalnom formatu na vaše računalo.
    * **Dodaj/briši**: Ako uz račun trebate/želite poslati neke prateće dokumente (npr. narudžbenicu u PDF formatu, skenirane otpremnice i sl.).

=== "Kartice ispod tablice"
    * **Dodatni podaci**: Ovdje upisujete podatke za obveznike javne nabave (škole, bolnice, gradovi...) kao što su broj narudžbe ili ugovora.
        * Za takve kupce račun ne šaljete odmah, već ovdje najprije upišete podatke.
        * Klikom na dugme **Promijeni** možete upisati dodatne podatke.
        * Tip poslovnog procesa možete mijenjati dvoklikom miša na to polje.
        * Nakon izmjena, račun prelazi u status *Za slanje* i šaljete ga klikom na *Šalji eRačun*.
    * **Status slanja**: Informacije o svim aktivnostima u vezi slanja eRačuna (datum, vrijeme, korisnik, opis).
    * **Info**: Detaljan opis posljednje aktivnosti na označenom računu.

---

!!! failure "NAPOMENA ZA PRVO SLANJE RAČUNA"
    Ako kod prvog slanja eRačuna dobijete poruku o grešci: **„Nisu upisani OIB, temeljni kapital, sud ili odgovorna osoba“**, trebate te podatke upisati u programu.
    
    Ovo su obavezni podaci računa za sve firme. Možda ste ih do sad imali na predlošku fakture, ali sad to više nije dovoljno.

    **Rješenje:**
    Otvorite **Uređivanje-Podešavanje zaglavlja/podnožja dokumenta** i upišite podatke u ponuđena 3 retka.

!!! warning "Važno: Pretinac – Vrsta poslovne/organizacijske jedinice"
    Ako je neka firma (obično obveznik javne nabave) imala više pretinaca (poslovne jedinice) gdje ste slali eRačune, do sad ste to upisivali u adresar kupaca. **Sad to više neće biti moguće** jer u adresar možete upisati svakog kupca samo jednom.
    
    Taj podatak se sada nalazi posebno na svakome računu u **dodatnim podacima** i upisuje se naknadno nakon knjiženja računa.
