# Toy project - Language model for Polish with Literary Epochs

Toy project based on LSTM language model. Using all available texts from http://wolnelektury.pl/ as the dataset. 

The model is character-level, but also includes extra vector with one-hot encoded literary epoch. The idea is to generate text with one neural network, but with different 'flavours' distinctive for each epoch (assuming that there are distinctive literary features for each epoch).

## Usage

### Python venv preparation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Download all books from wolnelektury.pl

`python3 wl_download.py`

### Process books to dataset (it can be HUGE)

`ipython wl_process.py`

### Train model

`python3 model.py`

Model was based on tflearn example: https://github.com/tflearn/tflearn/blob/master/examples/nlp/lstm_generator_shakespeare.py

### Generate texts

set the model file name in line `m.load('pl_model2-39424')`

`python3 decoder.py` will generate a brief text for each epoch

## Note

This is a toy, work in progress project for fun, not elegant nor optimal. 


# Generated examples

## średniowiecze

A i tak on się za pocałunków, że zdrów wierzy.

Pomyślę kobiet nad szkolonej zemwazy.
Takie jego to przyjęty trzy mogła w kształcie
— Wiem jestem, nader zamku przyjemnie wasza, sprzyja mi udobie, przemyślał —
Bamem z sobą posłać jak godnika i uim mieszkania.

A skoro radośnie. Nie napisany kruje drogę,
Widać wszystkoby od znaczna to przyznał swego ciężku?

I nie podczas mnie przesłania się w protoku jego posobie,
Odpowiada to i słowa w wilko przecież z nim zmyślę,
Lecz po twojej radośnie wieścią, żem jest boginie.

Siedział się szlachetne i chcieli w bratu,
Co się wszystko przystała, ponieważ wszak czynić,
Choć jeśli je i wyniesie do tej drogą
Lepiej na tem się mnie tak zawieży w przychodzi.
Skarby narzucenie przed konia, zastałem w stopniu,
Nie kocha zaczęła w życiu szukała,
Abrogonowa w zwierzu, że stłych wydać z pobocze
Przyścieścia śmiertelnym związku nieprzyjaciół ukazał przez ślady.

Jak powiem naszej godziny, iż wyrazi i opowieść do brzeży.

Kiedy zaczął tego szła w czas z woku zasady wielkiej i dojmował:
„W swój sto proku się zamysłem politycznego słowa.
Pewien tymczasem tej jest bierze pewnie rzecz przysłonie, to obrażał Rezentynu.

A pokój poklął się serce się na krzycza,
Cóż do strony w dziewki na serce zdrada w powodu
I widzi rozkazując szczęśliwie? Każ mu niemało,
Gdy król jego dobrze z pomocą widzę,
Tan daro to utworzenie do wanki między zwierzęty
Nie poganin i poprzejść orzała dał uwaja,
Poszło skrzydle zbrojności nie chciała uczuł sobie wyprawienie.

W świecie hagen pożyczał do szkoły bardziej do margrabia.

Do niej cię czynić mogę ws

## współczesność

Waszą pracować srogie żędy, uśmiechnął się zapałem,
Czy na sławnie biednym biednej podniosłem;
    Każdy najrzedł jej okręt szaty dziewczęta u rozstroje,
świata może swą w szaleniem odmęczeń.

Więc znalazła świat może jak los Wreszta, by pana wędrusie, chwilę razu na wielkości do króla szeroko nie czcicie, a tak ma, gdzie rozbędzie z mnie przekonane
EPOCH:  modernizm
tek na płotek. Ala ma kota, a kot ma Alę. Skąd Litwini wracali? Z wycieczki wracali! Nocnej, nawiasem krewnocze? — ja leszem jak i sobie bardzo, co nic uroczy na swoich i sposób ze swego, czekała tu byłem mu się strony i przyjęty pomocy starego w głębokim nie zamek: wiedziała się. Biednego widocznie znajduje, by jeszcze nie widziałem z których tylko wybierać jako niepana obwolenia się na przestroży, a idzie albo ciągłą ponieważ potrafić w niej embirycznych, który sto ponieważ podziwko nie znabywać dla mnie po chwili potem oczy na jej stroną rycerza, umyślenie na chwilę dzięki nie chciałby nie odpowiedziałem o bracie. Donosił porastając postawiała do klimu, pani na ziemi przedstawiając mię za obawę. Nic w chwili i straszne i pouźmy jeszcze jego sobie ciszą w słuchaczy.

A ja tak nie mogła żywota: jeśli w takim wiedzeniem złotobierza i obok mnie! — posiadam jej jeszcze myślał Kadie komprami. Ale jak prosto, że wieczna parłia straty na odrzecze, ale ładnych przyjaźni, a był snorosków tego wielka beszczałę i ja, stoty Hagena nadiemienie trem zająłem do tej świecie, który była słowa. Ten rozumiem najprzątniejszego samego niebezpieczeństwo mówił, aby mi tak nowa może o jej powiedzieć. To uborze reszty swego przeruszenia nie potem nie spląwały się o ciebie żwarzę został do wierzyć się lecinacji z tyków będy przerażenie należy mieczem zwykła i to za rozwikała, inaczej iść błędnie. Widział mnie mego poprzedniej ze sposób samym świecie jako wyfałość, okaziła się w stasią. Była może jego cąłownie na wyobraża, który mu może chytrym na prawdziwy, nawet rozumie, nie jest od pomocy do domu do broni syna, znaczna, że odwiedziłem był zajęciem, że urodziwszy się z Leci tego muusie, palcej duchowa i każdy poszli pożyczył, zzołowali się to powody wkrótce przyszłości mowy widocznie otemnić, by być tak sygnunka, ubudował go ustronowała wyjdzie mieściem: masz nieszczęścia z poznaną nikogo u koronsmach: „Przyczyny, miała co mogę… I naczył mu umiał mię sami odwagę. Każe się nie przyjacielu pojęcie otrzymał mię obrazy tych umowie. Kraju to jestem, kto może strzała się parę pogardzą. W chro


## romantyzm

— Dość poprawiać, że nie chcecie go mogli rozomienia, a o to dobrze chwilę.

W domu rzecz zawarł. W antytacji w tej szczerze przestrzemałem pojedyny pochłoniona i w niebezpiecznej sposób, co za tym obojętne i pani, które się jego między obowiązkiem.

A nie było dobrą jak komedii z rozwamionę, począł sobie kosztowała się, gdzie wielkość wstępującej odstawiało ani spotkał im po czasie wyrazować sobie męża z kolana jego czarnych, którzy się tak słuchał je samo, droga wyrok chwilę nie dostaniec ów na porę!…

— Słowy mu się będę ma na się głos nie potrzeba — komwania swą się oznaczany? W ten sposób tego oczy mój stał opamięta tak: szukał opaniać głosem sobie sobie jest tak… przyjaciół z drugiej daleko, nie wyjemniej wreszcie tak zanieszysz mi domatorzy nas serdecznych swój potoków, ani przekonane. Ponieważ królowa z mieszkańcy.

Norski: nad patrzył się w tej literaturze i bez samym naszego mówione w niej jak plakach wszedł z wiele rzeki sęzią w wielki brata Niektórych spodziewała się przy sposób, by to to wydarty okrusienia w godzinów staję, obędzie czy on to powrót się po porozumienia się krótko z większym czytać mnie: jeśli kryje się po głos po raz jej słowa porywano, wstydzi rozgardnia w zepełnienia pojedzie jej pochodziny pewność przekonał człowieka, w iż pojedynka podzielał w jej aż do jej przedziejącego się wywarć w przyrodzoności, który się w zgornej ziemi Filokomaza tak ściony w nim bybania do przyjaciół swą nie leczyć zachodzić tamtego bardzo w chory hiderowy forma wielkiej każdych się wyszędziły nabiera, który chce, jak się ma do wielkiej niepotrzebną, całe bez domu Aazarowi rozstał na wyrzutionie spolitości w małości bystycznym zatrzymał tak miejsce pozwoli ci sztuki i napatrzę tylko mówi — to szymy się nie mogę otu wielkiego nakładem obrazić się pokryty, którzy rozumieć, że potrzebę synowice oświetrzonym i tak dobra powiedzieć albo to natychmiast Defotony synów — przejęty jest ciężkiej nie odchodzić tak zamiennością,

## barok

ARGIST

                        Poważny radosne
De Brata poczęła za wszystko poszedł oczy
Wypadły w stanum do domu wielkiej uderzyć.
Wstawi, rękę pani Jej przecież na usta się, czy teże
Z sercu przysięga gości: „Jak świademszy przysięgaj się i miała:
Pasz młodych był wolności stołowa.
Więc łazy był powiecha sprawa
Królowa obawia, że zażewa!


ELMIRA

Gruka się osiemmi się w jego dokonaniem
Najbliższe dostatki i zębę cię w markize,
Nie część u czasu, przekonał się oto na ten się upodrabować. Jeśli za prze
EPOCH:  oświecenie
tek na płotek. Ala ma kota, a kot ma Alę. Skąd Litwini wracali? Z wycieczki wracali! Nocnej, nawiasem temu jestem sprawił; poddaje mu więcej, bo jak chciał mnie o niej dostał, iż nie prawda i prawdę z późne… skomania i porządkowanym rzećby poruszenie francuzy, by poselstwo jednego po życiu arcygórdziami zaciskałam przy córki, powiedział sądził, że wszystko go do paradzianie ten sposób porozumiała. Moje Dziewczyny, a nałażenie. Sto będzie nie wiem w pokoju pierwszego niebezpieczna, zamki obejrzał wiele nowo naszego jeszcze odbierała, choć w powiedzeniach stosunkę.

— No jeśli chcesz się w rzecz, obejść, że wszystko nie przysięga wydaje na niej uprzejmość, jakby to on pan należy, aby ci nie szczęśliwy. Tak mieli skrzydła i interesować na swego krzywdy ob kochała się pani rozkosznego stosunkowym skrajania w tym nieskończenia. Dostojność trzy będzie, niemiecka i w tym siebie miotały się zbyt zspokoju, by postawia się znaleźć że z przegodzili za drzwi dla człowiek się w domu, jak budował innych upokoju potrzebują, że już ci mu ten władzy ciąg je było z każdym przyjaciółki na mojej twej, a uczynił poczest, że przez nie znał widział, że do tej przez pomiecze co się wziął go tak z samego naszego miasto, pokazałem się jeszcze zrazić powiedzieć. Wszyscy rozumne czciwość myślenia. Więcej rzecz zalecy z nowieniem serce w pokoju z uwierząc się na rozmowa i najwyżej mogła się ospolita, zawsze życza, w łatwiej literaturze się w niemu i przywiadę w swoje znakiem. Ty się tak pokoju w czym chorama zaczął i postępującą go nam go do wartości, a miał powodzenia o tym nam przyjacielu był retulować ty życia łożone skoromy żywienie dziewczyna, którym po jego zawidał się, skarżące jeszcze jej dworze, niż się w Adys rozkazał się z nich bez wilotów. Potem tą postanie sobie zasię jak się ku zobowiązki, popęk nawet większym tym tej jednego jabie
Żywot sprzeciwiane w sposobu posławiam i bórze.
A w Laoboniczne przecie oczy, wiłem na mojej
Bardziej czarnych rękę zupełnie przygotować wkładał z wysłanego cierpieniem.
Pokazał była nadał wielkości miłości do znaka,
Iż muszą w tej stworzeniu najtrzej


##  renesans

— Nie zabrakszyła po mnie? Tak się znalazła na pojemnych i spadłości odeniem ciężarem…

Posłowo ta jest rzeczy… Skoro się do to nie podniósł się z nią.


ORELA

To powiem, że skupiwszy na to, gdzie się watem.
Beł to się, poddał się mój w pośredników twarzy
A chorobowe wychodzą, żeby przyszłego poostaci,
Chrześcijanie ci szczere wielkich jeszcze żadne nieszczęśliwy
Do dobre pogodziłby się może stary nie te wypada.
A tak widziałem nie mogła się w podzieli. «Tak nie zamkniała,
Tu była wysłał się jak się z domu się na kołoszkiem.



III

Pan pogrzeba na chwilę?


ORGON

/ wiedziec, że gdy wyciągnął jako zarobili.


ACANNA

/ do okręcie.

I może zdawały się falta, starego skale zamiana.


PERIPOTRO

Żydne, że ten Wirok śmieją się, który by znak rzecz nie starało,
Czy wszystko ci rania się wziętych włosy,
Do naszego sprawie jest boleśniej znów uprzeczeń.


MARIAN

/ po pali się zgoła. Nawrót i ochot chętnie jak potrzeba zasłonem
Swym bez warunkiem oprowadzić, zbliżała się mu mówić,
On tak dla dała mi się w gadać, z slatej miasto błaganie zaprowadziła się i natomiast posłałem może nazwisko. Zapomniała wyzbać; której ten naitrissa. Nie tak dla tej wielkiemu rozmowie się obaczyć honoru królem, że tylko zapalił się do wszelkim wytychnienia i oczywistości stanowionego w nieszczęśliwszego tym różne dziecinnym świętej namagonie samo, tak zareszto i oddano na wielkie wielkie jej zacności, szkiczy jedynie tylko odrubieństwa.

/ Margrabia tak strajom rzekła drugów, chcecie dalej o niej dorzecznym na dobrego wszelkiej trzecie?







AIIIIDOR

Na wielu blaskiem dawno w ziemia na innym odpowie
W okno prowadzi: Kazimier na czy i zaczyna moja,
Skoro na chole w tej skrugu maszmaniem rozkazał,
Iż bez rozum pokrycie i posło

## pozytywizm

I z mało policzka ruchu i rozmawiała do serca — com go potrafił: „Potym stała, głową do winienę mej literatury. Tak byłoby się w ciebie na rozrośnie z kalony wygadał się w ciężko? Kilku liście go i należałoby się nie wiedzieć, prawda całą siedzą chórki mieszkaniem musiałby jedanie nie ma nie nakazał się zbliża się kobiet ode mnie nie jest z moim miluzy smutnie.

Na trzech wierzy Halenda roztrzęsła się w swoim chwilę powiadają, że może do stara nie było wyjścia hatunkiem forma może w tym ubrania w ciężkie pogrobowości wieczorem to się w wypórnowaniem.

— Tak ma więc jako tu i wyrzucił na rana.

— Były jej odwagę w zawsze i wszelkie miejsce uchet zrobił wamieniem drugi złota na chwilę pogrzebanie o takiego wykładał się przyjętym przynajmniej radość. Bardzo czynszy mówiła, w sutunki zjechał na siebie udałem się niebezpiecznie.

Wieczne każdych obzarły prawa krótko byt mężowi, że stojący była pani — za to jest to sywa i oczywiście, tem, które służyła już sobie zamky, poddał się uważanym tę obwystający dostateczne, czegoś go do jego sposób dobry bardziej obluzienia i bodaj wszystko dzisiaj do Hagena, których czynił na obrok nie spełniony, tak w obyczaje wynaleźć bierze sprawy rozkazowany.

Siły w myśli znieść do 1niechu nadzieją ten święty popokojnie. Wódz rzecz zasłaniał spominało wszędzie niezwykłe tak sposób, pani Wrecie rozszerzała to uśmiechnęła się w zamkowym manystycznych do jest kolei do obrony, z porze opowieści, które ponurnie przy jakiś i niż niebo moje uczyniłby zwierzył

— Ale więc błądzieli nas, że nie zakwirzała kroków umiejeczna od swoim swoim chorąga zakryła się haneta; wyniknął i każdy do ludziom w matki znajdował się i tysiącą, jak cię w, oto postawistej domyślanie. Jest… najlepszym życzu z tego bacznego wierzył pana tubinek jego

##  dwudziestolecie

MAUszali w prawa bardzo wziął od domu, od łaski, które poznał nosiła i zadał nie do sudze w wiele dopomina, ale zawsze jedynie odmiennością przyjacielom powiezieni aby go nie spostrzegali do miejsc w chronia nie ma nienawiść przyszłym koreistowanego doprawdy zostawił się przez warki pojechać, i przejowa się pogodziły na ostatniego polityki fałszem z tak stron dziecko tym sprawia — odrzekł same, sprawiedliwości goniałosie i senstentatora. Sobie powiedział przyjaciele, że chciałbym się wziąłem się pokrzywiała rozumienia, jak masz będzie, mówić, przez swoim podnosi się jej urody.

— Ty skolrzek ci szepnął, że jest postanowieni szerokiej wytakiem, gdyby go zastał najlepszym:

— Więc choćby się i migoły nie siedział do mnie i czyńczył się o tym samo. Pięćdziesięć nastąpił czynił i ponad jego wszystkich wyśmiechach z konia do wolą na to głos. Państw powrót pan odbyta się i oddała się to spadła włoskę od szaly się zbyt milczeniem na im rozumieć i nie więcej zdziwieniem nie lubił obowiązanych wieści poczekującego się własne lecie jej kilka matko o wiele do jego zaś oznak, patrzała się zościwa swej w promestowanie i ciężko jest świata i gorzka obłoki fabrykował lim, w nimi przewidziania się owa odmówił przeszłości poczmę ciose

## starożytność

— Potem cechał się położenia nie podłów uprzejmości lub oboje się upustkował: szczególność ma się i pan świata było spostrzeżęcie o maląc bezpiecznie w talentu; zawsze maiądzie szczególny potrafi wszystkiego, który go nie trzeba uczynić i o jakiej widok nasza roku Margansuem — na niej wysłanianym wiele króla Patrakta miucz to był kozacji z krzyk i skromny dokołałem o takiego oczy a łoże prawdziwą w drugiej obwieściom. Do zamka spod skarbę nogi mitość nie zawsze się znak jako przybywa nie zdrów się, kiedy ważyła się do innych rządach przymorował, że jeszcze w moich uciekującego się występnego myślowego sprawiedliwości dla mnie obiada na godziny wielki nie mogło przypomniała… Et achius mrowska odpowiedział na tej szwadzki, którzy go zamku męża.

Bo a potworzył mnie zawołała się spojrzeć, jak więc posłuchać znów kod już król Słuchałem z niej, przeciwny się bliska żadnej odpowiedzenie w goni ugromadzy. Masz tak jest do takie wielkiego słowa wylewała go dobry.


MERGAGINO

Nie słuchaj — powody i przyczyną najwyższej bez obodem
Otrzymał drugi sposobem pewien w każdym starszy i podwoje.
Więcej przychodzi z dawnego strony może sądzą,
Gdzie wszak o sobie rychły, odpowiedział się na wielkiego tak nocy
Nad godziny których kapitaną wielki ten odległy trudy wypadkowo;

    Zawsze tak się obejść tam króla nie mówia jeszcze, gdy się stało? Że chęci o tym, albom wymuślana pozobiono w ostro nie mogę się z tym celu, by znikał się złoty, jak powiedział żona i widziała legarski.


DAPION

/ nikt wie był nadciągał do Nurtus, które dzielne bawi, aby warta mej moich liter!
To nakresne szkada mieszkanie, rzekł: Naturalne roztrzeć:
Tak się w pani za serce z początem strachy,
Wiem, jak on na to, sunista z rozmaitości,
I szla głośno zostawić czarowaną swoje znaku
W podumieniu wierzyła się po wojny cię postał.
Koło


