# code4fun

## Cześć!

Przed Tobą siedem zadań. Rozwiąż ile możesz zapisując skrypt/program, i grafiki/tabelki w katalogu w Twoim repozytorium GitHub. Nie uploaduj tam plików VCF większych niż 10MB.

Zadania są niezależne od siebie, nie musisz ich rozwiązywać po kolei. Sposób rozwiązania jest dowolny - można skorzystac z istniejących narzędzi lub napisać własny skrypt/program. Dwa pierwsze to zadania na rozgrzewkę. Ostatnie to zadanie z gwiazdką i może pochłonąć więcej czasu. Pamiętaj, aby commitować (i pushować) nie rzadziej niż po każdym zadaniu (przypomnienia o tym są również poniżej). 

## Połamania klawiatury!
 
1. Mając ciąg znaków x, napisz funkcję, która zwróci dwuelementową listę w której element pierwszy będzie ciąg znaków x z literami na parzystych miejscach zamienionymi na wielkie litery. Drugi element listy będzie miał wielkie litery na miejscach nieparzystych. 
Przykład:
fun(“abcdef”) -> [‘aBcDeF’, ‘AbCdEf’]
Przyjmij, że input do funkcji zawiera tylko litery.
    
    Commit and push!


2. Napisz funkcję, która jako argument przyjmuje ciąg znaków. Jako output, zwróci liczbę liter występujących w ciągu więcej niż raz. Kod nie powinien być wrażliwy na wielkość liter. 
Przykład:
funkcja(“ABBA”) -> 2 (a i b występują po 2 razy)
funkcja(“aBcbA”) -> 2 (a i b się powtarza; wielkość liter jest ignorowana)
funkcja(“RabarbArka”) -> 3 (a,b i r)

    Commit and push!

Kolejne zadania wykorzystują jako plik wejściowy plik w formacie VCF skompresowany bgzip’em:  [CPCT02220079.annotated.processed.vcf.gz](https://drive.google.com/file/d/1kyswBK5vd3GrLNSY8ZKmw7Xzc9DidCKe/view?usp=sharing). W pliku są adnotacje wariantów wygenerowane programami [SnpEff/SnpSift](http://snpeff.sourceforge.net/SnpSift.html). Jeżeli przetwarzanie pliku będzie stwarzało problemy ze względu na jego rozmiar - znajdź kreatywne rozwiązanie.


3. Stwórz plik VCF, który będzie zawierał wszystkie warianty z pliku wejściowego zawierające się pomiędzy chr12:112,204,691 a chr12:112,247,789. Komendę/program oraz wynikowy plik VCF umieść w repozytorium.

    Commit and push!

4. Narysuj histogramy długości insercji i delecji w pliku wejściowym dla każdego z chromosomów. Rysunek i tabelkę umieść w repozytorium.

    Commit and push!

5. Z pliku wejściowego wybierz warianty, dla których pole "FILTER" zawiera wartość PASS. Spośród tych wariantów policz ile jest heterozygotycznych (genotyp 0/1) z częstością występowania w populacji (Allele Frequency) mniejszą od 0.01. Do selekcji wariantów o niskiej częstości wykorzystaj adnotację INFO:GoNLv5_AF.

    Commit and push!

6. Na podstawie wariantów w pliku wejściowym wykonaj wykres słupkowy, w którym na osi x będą wszystkie chromosomy autosomalne, a na osi y średnie pokrycie (depth of coverage) wszystkich wariantów występujących na danym chromosomie. Jeżeli napotkasz wartości brakujące (“.”), potraktuj je jako 0. Średnie pokrycia wszystkich chromosomów zapisz również w tabelce (.csv, .tsv, lub Excel).

    Commit and push!

7. Dla pliku wejściowego policz warianty, które zmieniają białko kodowane przez gen, w którym wariant się znajduję. Listę możliwych konsekwencji zmian znajdziesz tu: http://snpeff.sourceforge.net/SnpEff_manual.html#Effect%20prediction%20details

    Commit and push!


To już koniec zadań, które dla Ciebie przygotowaliśmy. Przykładowe rozwiązania udostępnimy na początu przyszłego tygodnia.
