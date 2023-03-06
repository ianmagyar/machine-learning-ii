# Strojové učenie II

**Strojové učenie II** je kurz ponúkaný v letnom semestri tretieho ročníka bakalárskeho štúdia pre študijný program Inteligentné systémy. Predmet nadväzuje na kurzy Umelá inteligencia a Strojové učenie, venuje sa učeniu posilňovaním (*reinforcement learning*).

Informačný list predmetuje je dostupný na [školskom portáli](https://maisportal.tuke.sk/portal/studijneProgramy.mais).

## Obsah
1. [Plán prednášok a cvičení](#plan)
2. [Hodnotenie](#grading)
3. [Odporúčaná literatúra](#textbooks)

## Plán prednášok a cvičení <a name="plan"></a>

Prednáška z predmetu je vo štvrtok o 9:10 v miestnosti V144 v budove V4. Cvičenia sú v pondelok o 7:30 v miestnosti V102 v budove V4. Účasť na cvičeniach je povinná, študenti môžu mať maximálne tri neúčasti za semester.

|                               |                       Prednáška                       |                  Cvičenie                  |            Termíny             |
|:-----------------------------:|:-----------------------------------------------------:|:------------------------------------------:|--------------------------------|
|  1. týždeň<br>13. 2. - 19. 2. |              Úvod do učenia posilňovaním              |  Úvod do predmetu<br>[Matematické základy](https://marian.mach.website.tuke.sk/presentations/su2/prez-matrep.pdf)   |                                |
|  2. týždeň<br>20. 2. - 26. 2. | Markovovské rozhodovacie procesy a Bellmanove rovnice | [Návrh a implementácia vlastného prostredia](labs/lab02-creating-environments.ipynb) | [Z1 zverejnené](assignments/assignment1.md)                  |
|  3. týždeň<br>27. 2. - 5. 3.  | Markovovské rozhodovacie procesy a Bellmanove rovnice |             [Bellmanove rovnice](labs/lab03-bellman-equation.ipynb)             | [Z2 zverejnené](assignments/assignment2.md)                  |
|  4. týždeň<br>6. 3. - 12. 3.  |            Metódy dynamického programovania           |       Metódy [policy](labs/lab04a-policy-iteration.ipynb) a [value iteration](labs/lab04b-value-iteration.ipynb))      |                                |
|  5. týždeň<br>13. 3. - 19. 3. |                   Monte Carlo metódy                  |             Monte Carlo metódy             |                                |
|  6. týždeň<br>20. 3. - 26. 3. |				        TD-metódy  		    			|             Q-Learning a SARSA             |                                |
|  7. týždeň<br>27. 3. - 2. 4.  |            Aproximácia hodnotových funkcií            |           Q-siete, Deep Q-Network          |                                |
|  8. týždeň<br>3. 4. - 9. 4.   |                  Aproximácia politiky                 |        Práca so spojitými priestormi       | Z1 odovzdanie                  |
|  9. týždeň<br>10. 4. - 16. 4. |                                                       |                 Veľká Noc                  |                                |
| 10. týždeň<br>17. 4. - 23. 4. |                                                       |              preberanie zadaní             | Z2 odovzdanie                  |

[Ďalšie informácie k prednáškam sú dostupné na tejto stránke.](https://marian.mach.website.tuke.sk/course-mlII-en.html)

## Hodnotenie <a name="grading"></a>

Celkové hodnotenie predmetu je 100 bodov (40 + 60 bodov); študent musí získať viac ako polovicu bodov zo zápočtu a zo skúšky.

Zápočet sa skladá z dvoch zadaní, prvé za 10, druhé za 30 bodov, a z piatich domácich úloh. Zadanie 1 sa odovzdáva do konca ôsmeho týždňa a Zadanie 2 sa preberá v desiatom týždni.

|                  Zložka                 | Body |
|:---------------------------------------:|:----:|
| Domáce úlohy							  |   5  |
| [zadanie 1](assignments/assignment1.md) |  10  |
| [zadanie 2](assignments/assignment2.md) |  25  |
| skúška                                  |  60  |

## Odporúčaná literatúra <a name="textbooks"></a>
* SUTTON, R. S. - Barto A. G.: [*Reinforcement Learning: An Introduction*](http://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf). MIT press, 2018.
* MORALES M.: [*Grokking Deep Reinforcement Learning*](https://www.amazon.com/Grokking-Reinforcement-Learning-Miguel-Morales/dp/1617295450). Manning Publications, 2020.
