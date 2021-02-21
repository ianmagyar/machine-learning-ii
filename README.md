# Strojové učenie II

**Strojové učenie II** je kurz ponúknutý v letnom semestri tretieho ročníka bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurzy Umelá inteligencia a Strojové učenie, venuje sa učeniu posilňovaním (*reinforcement learning*).

Informačný list predmetuje je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Hodnotenie](#grading)
3. [Odporúčaná literatúra](#textbooks)

## Plán prednášok a cvičení <a name="plan"></a>

**Vzhľadom na pretrvávajúce opatrenia v súvislosti s pandémiou COVID-19 všetky prednášky a cvičenia sú realizované online prostredníctvom MS Teams až do odvolania.**

Prednáška z predmetu je v pondelok o 13:30 v miestnosti B520 v hlavnej budove (L9). Cvičenia sú v utorok o 10:50 v miestnosti LUI1 v budove BN3 (budova ÚVT). Účasť na cvičeniach je povinná, študenti môžu mať maximálne tri neúčasti za semester.

|             Týždeň           | Prednáška |                     Cvičenie                     |               Termíny             |
|:----------------------------:|:---------:|:------------------------------------------------:|:---------------------------------:|
| Týždeň 1<br>15. 2. - 21. 2.  | Úvod do učenia posilňovaním | úvod, priradenie Z1<br>[OpenAI gym](labs/lab01-setting-things-up.ipynb) | [Z1 publikované](assignments/assignment1.md)    |
| Týždeň 2<br>22. 2. - 28. 2.  | Učenie posilňovaním ako<br>Markovovský rozhodovací proces | [vytvorenie vlastného prostredia](labs/lab02-creating-environments.ipynb) | DÚ1 publikovaná |
| Týždeň 3<br>1. 3. - 7. 3.    | Monte Carlo metódy | Bellmanove rovnice                               | odovzdanie DÚ1 |
| Týždeň 4<br>8. 3. - 14. 3.   | Temporal-difference metódy | metóda Policy iteration                          | Z2 publikované |
| Týždeň 5<br>15. 3. - 21. 3.  |           | metóda Value iteration                           | DÚ2 publikovaná                   |
| Týždeň 6<br>22. 3. - 28. 3.  |           | Monte Carlo metódy                               | DÚ3 publikovaná<br>odovzdanie DÚ2 |
| Týždeň 7<br>29. 3. - 4. 4.   |           | metódy Q-learning a SARSA                        | DÚ4 publikovaná<br>odovzdanie DÚ3 |
| Týždeň 8<br>5. 4. - 11. 4.   | Veľká Noc | Veľká Noc                                        | odovzdanie DÚ4<br>odovzdanie Z1   |
| Týždeň 9<br>12. 4. - 18. 4.  |           | Q siete                                          | DÚ5 publikovaná                   |
| Týždeň 10<br>19. 4. - 25. 4. |           | preberanie zadaní                                | odovzdanie DÚ5<br>odovzdanie Z2   |

Prezentácie z prednášok sú dostupné na [tejto stránke](http://people.tuke.sk/marian.mach/course-mlII-en.html).

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z troch častí: 5 domácich úloh po 2 body, Zadanie 1 za 15 bodov a Zadanie 2 za 15 bodov. Na vypracovanie domácich úloh majú študenti jeden týždeň (zadanie bude zverejnené týždeň pred termínom odovzdania). Zadanie 1 bude zverejnené v prvom, Zadanie 2 v štvrtom týždni. Zadanie 1 sa odovzdáva do konca ôsmeho týždňa a Zadanie 2 sa preberá v desiatom týždni.

|                  Zložka                 | Body |
|:---------------------------------------:|:----:|
|             5 domácich úloh             |  10  |
| [zadanie 1](assignments/assignment1.md) |  15  |
|                zadanie 2                |  15  |
|                 skúška                  |  60  |

Priebežný stav hodnotenia nájdete [tu](https://docs.google.com/spreadsheets/d/19EyknXtyv0s8ocWo8quZOBL9E_RCH4yCI_wg0QdoDbg/edit?usp=sharing).

## Odporúčaná literatúra <a name="textbooks"></a>
* SUTTON, R. S. - Barto A. G.: [*Reinforcement Learning: An Introduction*](http://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf). MIT press, 2018.
* MORALES M.: [*Grokking Deep Reinforcement Learning*](https://www.amazon.com/Grokking-Reinforcement-Learning-Miguel-Morales/dp/1617295450). Manning Publications, 2020.