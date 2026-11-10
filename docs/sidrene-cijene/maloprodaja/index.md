---
title: Maloprodaja
description: "Sidrene cijene u cjeniku artikala i usluga: automatski iz kalkulacija ili ručno, ispis cjenika i datoteka za web."
tags:
  - sidrene cijene
keywords:
  - bazne cijene
  - maloprodaja
  - cjenik
---
# Sidrene cijene – maloprodaja

!!! info "Sidrene ili bazne cijene?"
    Koristit ćemo naziv **Sidrene cijene** iako bi ispravan naziv bio *Bazne cijene*. Razlog tome je što se naziv *Sidrene cijene* koristi već duže vrijeme za istu materiju kojoj je novim zakonskim izmjenama dodijeljen naziv *Bazna cijena*.

## Zakonski i fiskalni okvir

* **Definicija:** Sidrena cijena označava cijenu po kojoj se određeni artikl ili usluga nudila na **10.9.2026.** ili na datum kad je prvi put stavljen/a na prodaju, ako je taj dan kasniji od 10.9.2026. (tj. ako na 10.9.2026. tog artikla/usluge nije bilo u ponudi).
* **Fiskalizacija i izdavanje računa:**
    * Na fiskalnom računu koji se uručuje gostu iskazuje se i naplaćuje **isključivo trenutna važeća cijena**.
    * Sidrena cijena je evidencijski i informativni podatak koji se prikazuje u cjeniku i promidžbenim materijalima, ali ne utječe na fiskalnu osnovicu računa.
* **Objava podataka:** Trgovine koje posjeduju web stranicu dužne su na istoj osigurati uvid u datoteku sa sidrenim cijenama, **bez obzira** na to imaju li cjenik na webu ili samo informacije o firmi.

## Postupak postavljanja

Sidrene cijene se postavljaju u cjeniku **Maloprodaja -> Cjenik artikala i usluga**.

![Cjenik artikala i usluga – kartica Sidrena cijena](../../assets/images/sidrene-cijene-cjenik.png){: width="656" }

### Opis numeriranih akcija

1. **Sidrena cijena** – kartica sa sidrenim cijenama.
2. **Datum** – datum na koji se postavljaju sidrene cijene.
3. **Postavi samo datum primjene** – zapisuje datum sidrenih cijena po artiklima.
    - Postavlja datum sidrene cijene **SVIM** artiklima koji **NEMAJU** postavljen datum.
    - Postavlja **NOVI** datum sidrene cijene **SAMO ODABRANIM** artiklima.
4. **Postavi cijenu iz kalkulacije** – postavlja sidrenu cijenu po artiklima prema datumu sidrene cijene za svaki artikl, na način da pronađe cijenu na sidreni datum (traži cijene iz kalkulacija, početnog stanja i nivelacija). Ako neki artikl nema upisan datum, upisat će se datum sidrene cijene (2.).
    - Postavlja sidrenu cijenu **SVIM** artiklima koji još **NEMAJU** postavljenu sidrenu cijenu.
    - Postavlja sidrenu cijenu **SAMO ODABRANIM** artiklima.
5. **Postavi trenutnu cijenu** – postavlja **TRENUTNU** cijenu kao sidrenu.
    - Postavlja sidrenu cijenu **SVIM** artiklima koji još **NEMAJU** postavljenu sidrenu cijenu.
    - Postavlja sidrenu cijenu **SAMO ODABRANIM** artiklima.
6. **Ispis cjenika** – ispis cjenika sa sidrenim cijenama.
7. **Eksport u datoteku** – snimanje datoteke sa sidrenim cijenama za postavljanje na internet stranice.
8. **Sidrena** i **S.datum** – kolone sa sidrenim cijenama i datumom sidrene cijene.
9. **Datum primjene** – datum sidrene cijene za trenutni artikl.
10. **Sidrena cijena** – sidrena cijena za trenutni artikl.
11. **Ispis** – stupac u kojem se vidi koji su artikli označeni.

!!! info "Odabrani artikli"
    Prilikom postavljanja, cijene će se postaviti samo odabranim artiklima. U slučaju da nije odabran niti jedan artikl, cijene će se postaviti svim artiklima.

### Postupak A: Pojedinačna ručna izmjena

Sidrene cijene je moguće postaviti ručno za svaki artikl. Klikom na **Promjeni** omogućuje se upis datuma (9.) i sidrene cijene (10.). Nakon toga je potrebno kliknuti **Spremi**.

### Postupak B: Automatsko postavljanje za cijeli cjenik

Za postavljanje svim artiklima najbolje je slijediti sve korake od 1. do 6.

1. Otvorite karticu **Sidrena cijena**.
2. Provjerite da je za datum sidrenih cijena upisan **10.09.2026.**
3. Postavite datum za sidrene cijene (**Postavi samo datum primjene**) – ovaj korak se može i preskočiti jer će sljedeći korak postaviti i datum.
4. Postavite sidrenu cijenu i datum (**Postavi cijenu iz kalkulacije**) – program će potražiti po ulaznim dokumentima i upisati ispravnu sidrenu cijenu (i datum, ako još nije bio upisan). Ponavljanjem ove radnje program traži i postavlja ispravnu sidrenu cijenu na datum sidrene cijene koji je upisan uz svaki artikl.
5. **Postavi trenutnu cijenu** možete koristiti ako ne koristite kalkulacije.
6. **Ispis cjenika** sa sidrenim cijenama.

## Generiranje datoteke za web objavu

Datoteku za postavljanje na web možete snimiti klikom na **Eksport u datoteku**. Prije snimanja potrebno je na desni klik upisati podatke o poslovnici, tj. nazivu datoteke.

!!! warning "Naziv datoteke"
    Naziv datoteke je zakonski definiran, pa je najbolje samo kliknuti na **Prefiks datoteke trgovine**.

![Prefiks datoteke](../../assets/images/sidrene-cijene-prefiks-datoteke.png){: width="511" }
