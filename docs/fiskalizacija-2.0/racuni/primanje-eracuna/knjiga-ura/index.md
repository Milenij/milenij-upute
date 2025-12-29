---
title: Knjiga URA
tags:
  - fiskalizacija 2.0
keywords:
  - knjiga-ura
  - primanje-eracuna
---
## ULAZNI RAČUNI

Iako ćete sada većinu računa dobivati kao eRačun, neke ćete i dalje dobivati u papirnatom (ili PDF) obliku (npr. računi plaćeni gotovinom/karticom, računi iz EU ili uvoza…).

!!! info "Papirnati računi"
    Te račune (papirnate/PDF) knjižite na identičan način kao i do sada. Tu nema promjena.

### Postupak knjiženja eRačuna

Knjiženje eRačuna bit će puno jednostavnije, ali je važno razumjeti proces:

!!! warning "Važno: Nema automatizma bez kontrole"
    eRačuni se **NEĆE** automatski proknjižiti u program čim vam ih netko pošalje.

Za preuzimanje i knjiženje slijedite ove korake:

1.  U evidenciji ulaznih računa kliknite na gumb **Donos eRačuna**.
2.  Otvorit će se novi prozor s tablicom svih računa koji su stigli na vašu pristupnu točku (kod informacijskog posrednika).

### Pregled tablice pristiglih računa

U tablici se nalaze svi pristigli računi, ali to ne znači da su svi i proknjiženi.

* **Neknjiženi računi**: Čekaju vašu obradu.
* **Knjiženi računi**: U zadnjoj koloni **URA (Knjiga)** imaju upisan redni broj i knjigu u koju su knjiženi. Tako bez problema možete razlikovati knjižene od neknjiženih računa.

### Pregled sadržaja računa

Prije samog knjiženja, račun možete (i trebali bi) provjeriti. Program nudi dva načina prikaza:

=== "Opcija: Pregled"
    
    Prikazuje podatke izvučene direktno iz **XML datoteke** (što eRačun zapravo jest).
    
    * **Izgled**: Standardiziran za sve dobavljače (ista forma).
    * **Svrha**: Brza provjera strukturiranih podataka.

=== "Opcija: PDF (Original)"

    Prikazuje dokument onako kako ga je generirao vaš dobavljač (vizualni identitet).
    
    * **Izgled**: Identičan papirnatom računu ili PDF-u kakvog ste dobivali ranije.
    * **Svrha**: Vizualna kontrola i pregled detalja koji možda nisu u standardnom XML prikazu.

> Iako im je izgled različit, podaci u oba prikaza moraju biti identični. Predlažemo da svaki račun pregledate prije knjiženja.

### Finalno knjiženje

Kada ste se uvjerili da su računi ispravni, postupak je sljedeći:

1.  **Označite račune**: Klikom miša u prvoj koloni stavite znak **+** uz račune koje želite proknjižiti.
2.  **Pokrenite knjiženje**: Kad ste ih sve označili, kliknite na gumb **Knjiži**.

Program će sve označene račune proknjižiti u vašu knjigu URA.

!!! tip "Dvojno knjigovodstvo i automatizacija"
    Ako vodite dvojno knjigovodstvo, program će automatski napraviti i temeljnicu po pravilu **zadnjeg knjiženja** za tog dobavljača.
    
    * **Postojeći dobavljači**: Program pamti konta s prethodnog računa.
    * **Novi dobavljači**: Kod dobavljača čiji račun dobivate prvi put, nakon što zatvorite prozor za donos eRačuna, trebate ući u promjenu tog računa i **ručno upisati temeljnicu**.
