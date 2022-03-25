# Strojové učenie II

**Strojové učenie II** je kurz ponúknutý v letnom semestri tretieho ročníka bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurzy Umelá inteligencia a Strojové učenie, venuje sa učeniu posilňovaním (*reinforcement learning*).

Informačný list predmetuje je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Hodnotenie](#grading)
3. [Odporúčaná literatúra](#textbooks)

## Plán prednášok a cvičení <a name="plan"></a>

**Vzhľadom na pretrvávajúce opatrenia v súvislosti s pandémiou COVID-19 všetky prednášky a cvičenia sú realizované online prostredníctvom MS Teams až do odvolania.**

Prednáška z predmetu je v pondelok o 7:30 v miestnosti V102 v hlavnej budove (V4). Cvičenia sú v pondelok o 13:30 v miestnosti B520 v budove L9 (hlavná budova). Účasť na cvičeniach je povinná, študenti môžu mať maximálne tri neúčasti za semester.

|                               |                       Prednáška                       |                  Cvičenie                  |            Termíny             |
|:-----------------------------:|:-----------------------------------------------------:|:------------------------------------------:|--------------------------------|
|  1. týždeň<br>14. 2. - 20. 2. |              [Úvod do učenia posilňovaním](lectures/Lecture01.pdf)              |       Úvod do predmetu<br>[OpenAI gym](labs/lab01-setting-things-up.ipynb)       | [Z1 zverejnené](assignments/assignment1.md)<br>[Z2 zverejnené](assignments/assignment2.md) |
|  2. týždeň<br>21. 2. - 27. 2. | [Markovovské rozhodovacie procesy a Bellmanove rovnice](lectures/Lecture02.pdf) |             [Bellmanove rovnice](labs/lab02-bellman-equation.ipynb)             |                                |
|  3. týždeň<br>28. 2. - 6. 3.  |   [Dynamické programovanie, policy a value iteration](lectures/Lecture03.pdf)   |       Metódy [policy](labs/lab03a-policy-iteration.ipynb) a [value iteration](labs/lab03b-value-iteration.ipynb)      |                                |
|  4. týždeň<br>7. 3. - 13. 3.  |                   [Monte Carlo metódy](lectures/Lecture04.pdf)                  |             [Monte Carlo metódy](labs/lab04-monte-carlo.ipynb)             |                                |
|  5. týždeň<br>14. 3. - 20. 3. |                       [TD-metódy](lectures/Lecture05.pdf)                       |    [Q-Learning a SARSA](labs/lab05-q-learning-and-sarsa.ipynb)    |                                |
|  6. týždeň<br>21. 3. - 27. 3. |            [Aproximácia hodnotových funkcií](lectures/Lecture06.pdf)            |           [Q-siete, Deep Q-Network](labs/lab06-q-networks.ipynb)          |                                |
|  7. týždeň<br>28. 3. - 3. 4.  |                  Aproximácia politiky                 | [Návrh a implementácia vlastného prostredia](labs/lab07-creating-environments.ipynb) | Z2 prvé kolo                   |
|  8. týždeň<br>4. 4. - 10. 4.  |        Riešenie čiastočne pozorovateľných úloh        |       Práca so spojitými prostrediami      | Z1 odovzdanie                  |
|  9. týždeň<br>11. 4. - 17. 4. |                                                       |             Actor-critic metódy            | Z2 druhé kolo                  |
| 10. týždeň<br>18. 4. - 24. 4. |                       Veľká Noc                       |              preberanie zadaní             | Z2 tretie kolo                 |

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch zadaní, prvé za 10, druhé za 30 bodov, obe budú zverejnené v priebehu prvého týždňa. Zadanie 1 sa odovzdáva do konca siedmeho týždňa a Zadanie 2 sa preberá v desiatom týždni.

|                  Zložka                 | Body |
|:---------------------------------------:|:----:|
| [zadanie 1](assignments/assignment1.md) |  10  |
| [zadanie 2](assignments/assignment2.md) |  30  |
| skúška                                  |  60  |

[Priebežný stav hodnotenia nájdete tu](https://docs.google.com/spreadsheets/d/1rKYwykd3eCjIzR9lUyfFJifpZP9qgLe4LE3q8ja2ATg/edit?usp=sharing).

## Odporúčaná literatúra <a name="textbooks"></a>
* SUTTON, R. S. - Barto A. G.: [*Reinforcement Learning: An Introduction*](http://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf). MIT press, 2018.
* MORALES M.: [*Grokking Deep Reinforcement Learning*](https://www.amazon.com/Grokking-Reinforcement-Learning-Miguel-Morales/dp/1617295450). Manning Publications, 2020.