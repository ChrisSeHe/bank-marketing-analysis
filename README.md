# Take Home Assignment

## Ziel
Ziel dieser Analyse ist die Vorhersage, ob ein Kunde im Rahmen einer
Marketingkampagne ein Festgeldprodukt abschließt (`y`).

Der Fokus liegt auf einer realistischen Bewertung der Modellperformance
sowie auf der Ableitung geschäftsrelevanter Erkenntnisse zur
Priorisierung von Kundenkontakten.

## Datensatz
Verwendet wird der Datensatz `bank-additional-full` aus dem
UCI Machine Learning Repository.

Bitte lade `bank-additional-full.csv` aus dem UCI Repository herunter 
und lege die Datei unter `data/raw/` ab.

## Vorgehen
- Explorative Datenanalyse und Prüfung der Datenqualität
- Zeitbasierter Train/Test-Split zur realistischen Bewertung
- Vergleich mehrerer Modellansätze (Logistische Regression, LightGBM)
- Bewertung anhand von PR-AUC und Precision@10 %
- Ableitung einer finalen Modellentscheidung

## Ergebnis
Ein gut regularisiertes lineares Modell (Logistische Regression, C = 0.1)
liefert im realistischen Evaluationsszenario die stabilste und beste
Performance zur Priorisierung von Kundenkontakten.

## Ausführung
1. Virtuelle Umgebung erstellen und Abhängigkeiten installieren:
pip install -r requirements.txt
2. Notebook ausführen:
notebooks/01_take_home_assignment.ipynb