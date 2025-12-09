---
title: Pripremne radnje
tags:
  - fiskalizacija 2.0.
keywords: []
---
\# PRIPREME ZA FISKALIZACIJU 2.0 U APLIKACIJI iSustav



\[cite_start]Ovaj dokument opisuje promjene i potrebne radnje u modulu \*\*Adresar kupaca, dobavljača\*\* unutar aplikacije iSustav\[cite: 1, 2]. \[cite_start]Do sada ste na izborniku \`Matični -> Adresar kupaca, dobavljača\` upisivali partnere s kojima poslujete\[cite: 3].



\## 1. Inicijalna automatska provjera



\[cite_start]Nakon instalacije nove verzije aplikacije, prilikom prvog ulaska u adresar pojavit će se važno upozorenje\[cite: 4].



!!! warning "Važno upozorenje aplikacije"

\    \[cite_start]Zbog Fiskalizacije 2.0 za sve upisane kupce potrebno je napraviti provjeru jesu li obveznici primanja eRačuna\[cite: 7].



\### Postupak provjere



Za pokretanje provjere slijedite ove korake:



1.  \[cite_start]U adresaru kliknite mišem na crveni tekst \*\*"Obavezna provjera svih partnera za eRačun F 2.0"\*\*\[cite: 150].

2.  \[cite_start]Program će proći kroz popis i po OIB-u potražiti partnere u AMS sustavu te ažurirati njihove podatke\[cite: 158].



\`\``mermaid

graph TD

\    A\[Klik na 'Obavezna provjera'] -->|Slanje OIB-a| B(AMS Sustav)

\    B -->|Povratna informacija| C{Pronađen?}

\    C -->|DA| D\[Ažuriranje podataka partnera]

\    C -->|NE| E\[Bez promjene]

\`\``



!!! success "Rezultat provjere"

\    \[cite_start]Ovim postupkom obavljate inicijalno ažuriranje podataka\[cite: 159]. \[cite_start]Ono ne mora biti potpuno jer većina klijenata možda još nije upisana u AMS, što je u ovoj fazi očekivano\[cite: 159].



\---



\## 2. Ručno uređivanje podataka



\[cite_start]Ukoliko želite ručno ispraviti ili dopuniti podatke, odaberite klijenta iz liste i pritisnite gumb \*\*Promjeni\*\*\[cite: 160].



??? abstract "Zašto je točan unos sada presudan?"

\    \[cite_start]Iako je i ranije bilo moguće odrediti porezni status (u sustavu PDV-a ili ne), većina korisnika to nije ažurno pratila jer je aplikaciji bio primarno važan \*vaš\* pravni status za obračun poreza\[cite: 161, 162].

\    

\    \[cite_start]Međutim, \*\*uvođenjem Fiskalizacije 2.0, podatak o poreznom statusu pojedinog klijenta mora biti točno upisan\*\*\[cite: 163]. \[cite_start]Ovo se odnosi na korisnike koji koriste iSustav aplikaciju za knjigovodstvo\[cite: 164].



\### Definiranje parametara klijenta



\[cite_start]Za svakog klijenta potrebno je definirati tri ključna elementa\[cite: 165].



\=== "1. Tip Partnera"

\    \[cite_start]Potrebno je definirati je li partner kupac, dobavljač ili oboje\[cite: 166].

\    

\    \* \[cite_start]\*\*Preporuka:\*\* Najbolje je označiti da je partner i \*\*dobavljač\*\* i \*\*kupac\** (uključiti obje kvačice)\[cite: 166].



\=== "2. Porezni Status"

\    \[cite_start]Ovaj podatak birate iz liste ponuđenih vrijednosti\[cite: 206]. Moguće opcije su:

\    

\* Obveznik PDV-a

\* Obveznik po naplaćenom PDV-u

\* NIJE obveznik PDV-a

\* \[cite_start]Građani, potrošači i ostali \[cite: 211, 215, 216, 217]



\=== "3. eRačun F 2.0 Status"

\    \[cite_start]Ovaj status definira obvezu slanja eRačuna\[cite: 219].

\    

\    \* \[cite_start]Ako ne znate status partnera, kliknite na poveznicu \*\*"eRačun F 2.0"\** unutar forme\[cite: 231].

\* \[cite_start]Aplikacija će se spojiti na AMS i provjeriti trenutni status klijenta\[cite: 242].



\    !!! info "Napomena o statusu"

\    \[cite_start]U početku ćete često dobiti odgovor da se korisnik \*\*ne nalazi\*\* u sustavu AMS-a\[cite: 243]. \[cite_start]To je normalno jer većina obveznika još nije prijavljena i ne treba vas zabrinjavati\[cite: 243, 244].



\---



\## 3. Posebne kategorije i izdavanje računa



\[cite_start]Prilikom budućeg rada, program će automatski provjeravati status kupca\[cite: 245]. \[cite_start]Prilikom zaključenja svakog računa s transakcijskim plaćanjem, program će provjeriti nalazi li se kupac u sustavu AMS-a prije izdavanja računa\[cite: 245].



\### Vrste obveznika eRačuna



\[cite_start]Postoje dvije glavne kategorije obveznika\[cite: 247]:



1.  \[cite_start]\*\*Obavezno slanje eRačuna\*\* \[cite: 248]

2.  \[cite_start]\*\*Obavezno slanje eRačuna - javna nabava\*\* \[cite: 249]



!!! tip "Javna nabava"

\    \[cite_start]Iako se računi šalju na isti način, kod obveznika javne nabave program će prilikom knjiženja ponuditi unos dodatnih podataka koje naručitelj traži\[cite: 250], kao što su:

\    

\* Broj narudžbenice

\* Vrsta poslovne jedinice

\* Pretinac

\* \[cite_start]Broj ugovora i sl. \[cite: 251]



\### Inozemni partneri



!!! note "Poslovanje s inozemstvom"

\    \[cite_start]Ukoliko poslujete s tvrtkama izvan Hrvatske, njima i dalje šaljete račune kao i do sada (poštom ili mailom) – ne šalju se kroz sustav eRačuna\[cite: 246].



\---



\> \[cite_start]\*\*Status:\*\* Ovim koracima završili ste ažuriranje podataka o kupcima i dobavljačima\[cite: 252].
