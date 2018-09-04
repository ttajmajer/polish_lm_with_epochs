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

nazwanego z siebie, mają na miejsce różno począł sobie ustowawiać, cnota ta rzecz z prawym zrodzonej figurzu. W nadywają taki pokierował na przyjaciela, podar pani Boga — w powieczerzy jest nie się to cały niekiedy nie wówczas udać w sama sławy i w głowie dalej ponieważ wcale chodzić królową w Starazeniu. Siadał do swoich zepsunej poszukami. Tristan w powrocie, na trudy wzajemno z poszedł tego incernem przyjacielem, która tylko obok dostatek, jaki wprawdzie ona boży na głowie przy chwili od lody.

— Dumał Roland czekał ją łaskawi. Okryty poganie chciała się ziemię Renem. Aż pan zazyskać się pan bardziej zapytawa, podpowiadał ludzi, zginęła poeto na myśl, jak biednych przyjaciele, że ona wejść dzień się do świata w łona, zbierał na skończonych. Jego łaskawie to sytuacja, nie czyni bogate do woli jej tego, że odtychał ci dla niej głosem swoją koniecznością. Każdego postrzegł się na wymyślać przez zbroi i cierpienie i wielkich będzie pokutem. Tak bardzo zwracał się tak okrętu bratem i przyszła własnych gotowości, obiecie, że przyjaciele rzecze na powietrze nam ubrania koleju nie myśli przeciwnym.

Wszyscy czasami głowę swego mu powiedział, o strasznym kolei… Roztrońca się zabrany, że dziwnie nie trzymałem przeczę ku staraniem do wyrazili od wstrzymała go na miłości, odpowiedział, że czyni pożegnanie do nocy i odjeżdżali morduła i przed swoim Ganelon przyjacielem, olbrzymie i przed starszego wiedziałem. Z tobą może się sobie, jedno szuka za rzeczy — a długo pomagać żądzą Murtufe. Ale wreszcie jego ziemią ci się z nas mardęrostwie nie było mało i manustencjach swym w samych świata, w poszedł go na dano.

Wody jeszcze to kazał, z cierpieniom uprzejmość ujrzał po rozpaczach i odpowie nas raz mówił na lat na nim i głosem widzi z jej ciebie w sercu z czeskiem Buludy, i przez przyjaciela chłopcem powiada swem swej stosownej mojej domu.

— Podwierzaj nie bardzo wielkie. Ale szczęśliwa nie za nimi wyszedł w największego jedne przechodzą, iż zależy dnia, kto pani przypadła na star
## współczesność
nawet wykrzyki z sztekcyem przyszło wstrząsać manichną. — Ta poznanie postępowały i osoba kontekce mogła, że tuż te dla mnie nie dostał niekrólewniczy, może je sala tutaj na rozgodności, a przeczyście wypiła miłością, bardzo potrzeba wojsko, który serdeczna, z siebie z rękach tylko nigdy nie zabierający i odpowiedziała, zapytał właściwie brat, którym nie może w boleści, nie był pocieszyć na gości te milem, który było go trzecia chwila, niechaj więcej zapadłem przez daleka i roztrzebać wszelkim głosy za uszerem i niebezpieczeństwie nie powiedział na łupaniu. Czasem pomyślał na związku osobnego za własnym klepentycznej i tej zajadzy na innego przygotowany na dobre i wielkim jest te zapał, ale przyszły się głos wielkim ledwie przez chwilę przez ukrywa, po wierze. Dzień prawie literatury noc was zazwyczajne wielkiego cere swe chociaż czy panie poświęciłam: „posadziłem się na cenielki towarzysza, owoc krzykowi tego dla jego komnaty. Moja poczekał dziewiąte spolitym towarzystwo, które byli sama wał była niech Mande cieszył bardzo on przez świecie swoich tego podziała częściu, czy i dręczym czasu pana zabiegała w bezmierną i poczęły tajemnica i samym między okazaniu od początku różno zaszedłem na jej przyjaciółko. Wiedzę na prawą widzianej i grymieniem, po tych, poszlakiem po mozacyszkach, panienki się z coraz sędziom, wisiały tylko grodzonych konkretnych nagle, dotarły toporu i tak niegodnej krainy dzień ramię…

Przy przeczytania bardzo końce na bardzo talent najlepszym rozmawiała się do staraniu dla siebie szeroko i człowieka mówiąc do wiekach. Wówczas znaczy ją przez innych koło o grzechu i czy w wejście. Przy siebie budziłem wolno, dziewczynki i przypadków, najsześć tak kary, które od jako kalowianego szacuneczkę poroztanień, strąciła głowę podobnym opowiem, co porozumieć zajmowałem do wyjdziesz przez należy na chwilę, nie śmiał się niemożna na zacujach, szczęście gładząc życzę, aż oceniła od podobnym cieszyła się, iż na owym oku widziała stanął Opoleciała. Z jest z prze

## modernizm

na potrzeba zdradzałem z drugiej cierpliwości od nich na niemi, przyjęcie na morzu, skarbem tych zabrać w wołania, włosy poprzeciwiło się do odpowiedniów w poleciałem, pensję o nich przystojnym strony zapomniał później po kolanach, tylko zmianował, pana nie z Warozem i w kościoło sama wszystkiego utrzymać braka, ale to samego usłyszał od jego paradzikach, każdy należy kochankiem na ziemi Jakoż konie na czterech przez praw tysiąc prawdzie rozkosze ciebie, wrócił jej ukazała się mogą on i odpów od poraz nutno oczy spośród waszym opartych na dawno i drugiego stały białego w okno, niestety de Raz intelektualizuje na błąd:

— Jesteś pełnia po swojej swoich zrozumieniu, spostrzegł zacisknięta moim nam bezsilnym kokole, w mojej chwili rozwięzką, w przednie na ciemności i bardziej postatu legierzy, naśledził się jedno chłodnymi gościach świadomości, kołatał zawała, jak to trzeba mieć powiadane. Trafił zapaliła tylko ciężkich przypadkiem. Nie mogła cię tak zrobić i wszędzie z bręki i dziewczyny wmówiła się się strzeleństwo, pomieszanie przeciwne ciała, to jeszcze godnie i jak wędrowała mogli przez królewicze.

— Trzymajcie, że ono nie masz czy wszystko obsada stało; przyszło jeszcze mi prawo boleści sam soka, i zaśpiewając kochanek, co może rozpędzić się jako stojący obecnie.

Kocham zajmował z wyniknął mnie w szacunku przyczyny mojego kościele królestwa, i mnie znajduje. Przed całej drugim przedmioty, po wybornej przed mej nakutem przestanie boustrzego okazały, a między ciała tak jest miała. Wzniósł do moje obrzydnikach lat się zagadnąć ze szlacheckim w piersi o życia. Na mardo najzupełniej podobających miała przed samieńskiej skórze z mrukującym kandylami. Ale wówczas zarazu kubiłem weszli od każdym głębi smutek.

— Przez duchem taka, jak kocha na każdej ciasnej przyjacielem? Po dzień. Z poduszką pojechał w tak kraju prosto na sekretarzowi, spelekcie, ale jest do tak obrzydnie przez dnia do zimnych raczej wody przez wyjęcia stanąć lub patrzeć, ale nałożył go jak przyjaciele.
## romantyzm

na nią do przejeżdżając na kącie, wyrzeczała swej wieki o tej wokiem.

— Niech uważające ciebie i rzekł:

— A Czerze z głęboka.

Nie pani zaciekali od chwili, która się to przez niemniej jedynie wieczorowego. Przed Kostanu a jodna pozostawić jej urodziła bez dzieje, zaraz mi ich od ją sprzedać wiesz, że trawienie stronie — słyszał sobie kroki i dzielił przy tobą, nic oczy bogiem, obyczaj nie zaglądał na niewidać raz przygrodu do innymi, nie wolno za między strusznościach, jak jedynego trzeszcze łamie. Dawno nie słyszała w świecie na głową w przyjacielem; zupełnie do postaci upadło wprzód przyszło tobie czarne przekazany w koniecznie przyjaciele, którego wie… rozszuknięty mi czynię ten wszystkie chwili szaleństwo pierwsze skoczył w pazorach, w zakąd nie każdej podporach jego wrócili do wiatr od chwili i to my gorączka, do boku i naczernienia, zaniedbana jest, przez głośno się okrzyk pisze, po bracie wypełniały orki i względem słów osób się myślowe. Groda że tę gorsto wyższa powtarzać za nim nie oszuło czym zeszła jeszcze najwyżej ostrożnym teraz z synie się ogromną poważyłem, w zapałach. U czerem za przyżyciem — powierzcie na szeregu dziewczynki, każe w głębokich ogóle, przechodziło się tego nie będziem i czcinary, iż cześć kiedy przyszło znaleźliśmy się stanie w wyszedł na fendecyncy i skoro zwolał się w czuje niż stawiej — ta rzecz sobie i takoby dość miał tylko wszelkich tylko dalej i zaszli i na grującym grupach taka rzeczywistości uważał.

— Nie siedziała się serce córko… taki ścian to im uszedł tak najkozna do tym zawołanie ogrodzie kazanie przed trzy opuściła do miejsce. Także w łoma przykre od niej wypłacił, w bowiem pokazał się na przygudzie — powiedziała za trzymasz mało następne miałem z rozumum, ale strycza będzie wydaszcze. Gdy się skałać i przybyte, tę duszy, gdy fladelin przekroć na wiatru był ciebie jednej piersi, zapalała do między świat i powiedziałem się cywał, iż stała zboda przecież było rozjaśni. Postanowił się tajnie jak przyjaciele siedzieli odw

## barok
na drugiego sympatia.

— Czy na chciałaby go możesz wzrok przerażanie.

Jeszcze jego koroności, i ze swój rozzurtyłem do babelniczki rzutem i najsiłem przy polu wierze najkazał stary dawne wielkim a skłoniejszymi jego koledowe. Do niej oczy zostać podstąpienie przekrywają. Trzyma się bardzo naszy konieczne, jako go poddać w złota, niemal przenika i porodne jest tego wielkie obulał i odpowiem za królem, sam cierpieć się moje słowa o sami tylko com kowy ojcowie Jestło, owszem tak pozostała panie miejscach czującej wszystkiego w odpowiednich poetyckiej krwawej na czyną. Nie mógł człeka polsko nie więcej każdego glatem. Tam amola przejrzysz pożyczenie nie są cierpianio tyle sprzeciw go nad kapitan postanowiły chłopców korusu i powiedzieć za prawdziwszy — ma ułożony w rzeczywistości przystawia.

Zdemomi w ostatnie wystarczy o domu pod w nią rusy młodego przewodzę sprawiedliwą po tym morskim oto ją całe chorobę na wieku tysiące struty nie szczęście, wprost w słów albo jak na jego siły rady, pasterzów westchnieniem, podobny ogromne we wstawieniu fantazji.

I, tylko była utany i lopliwem powiedział życia musiał mnie gładzili, wyczekują go przyjąć potęgi mojej altaniu stodza popatrzyni do naszego zupełnie, tego karzy, kiedy równie indywidzie od tego pochyleniu, w ten sposób o zawencie domu i sztuczkom uśmiech się przez jestem znowu; w dziewic przy razem ugruchy są pana, pracują się ona wielkiego strona, że nie za wszystkie opadakowi jest na świątynię, potem wielki Antyi różny podnieść, prowadził na zanim owego dworpanie. Pozostaną prostoć, bladzika potem rzecze:

— Jakże jeszcze ci nim Don Vanaowi szatan widzieć, działa na lat literaturu była do nas mojej przypuszczeniami, jakie odwrócił pewnego istnienia, pospołowie lub zwierzali się pani i Bogu usłyszał przez ludźmi, podnego muzyka pokojowi do uważaniu jej róża. Pozwolił mi braty w tych sposobu nazwiska, mnie przed króla nas pojawiać się przekładać — czy karek wyrobić: Z modlitwie związkowa zejścia z toreckiej skrzypał długą

## oświecenie

na zapytania, iż zamilkła pobliżu występkiem — jak na największą przyszła, znajdowałem się marzeń. Nie mam do jego palące wielkie znak nieustannie wyciągnęli się do przeszłości do królestwie do przyjacielem spadał się żadnym synu. Było to wszystko przyjaciela stokowie muzyką, gdy książę uczynił było żywiej albo w ogoną, odpowiedziała, co się z brami, opierając się ciężkie, wiatry jak starania przemienia na śmierci z ziemi, częściej znajdzie była miała przedzierać w domu skalanie może szkodzić. Nie mówiła podany, w zaboczenia potem nie wolno na widoku, pozwoliły się jej rozumie.

Nie widziałem, także tak drugim za których roku I, w tych pogardą koło dziennikom.

— Młody chciał się istotnie, wiesz to chodzić, ale które działem całkowite, bo mniej wedle wielkich; ciała go zapominały królowia, jak ciężko, jako potem przed tobą Prawpofawonowi i góra udała się żywienia powiększą potopa o różnia morzu, co stara mi się maleństwo: „Jestem świat do sobie bracie. Stanęło przybył się w oczy chamach nasze lub zakondła w istocie, z czym nie uczącej służy tego walczyć komady siły z najwyższym męża podnieść mojej suma, z strzałami mogło się pierś i nie obrazienna przez ciężką statek.

To to nie posiadać, że się prawdopodobne przeszczenią; nie jest sam jak przed tym w zgodzie człowieka toporu powodził się na jej ręki.

Chodź chciałem w wydawczych i nie zmieniać było on cały wiedziałem, ale widziała się karet, jak za nią łatwiejszym zaklinaniu, którego zarężąca tylko rozeznała do drugiego mojej potrafia. Można zaczekała ono przez pobożne wodę, co. Pracowałem odpowiedziały patrzeć o miejsce pozostanie w niebezpieczeństwie przedostanie niewinnego zatranem współczesną tylko na oszalanie, ale dzień męże najszedłem sądzić się jednak towarzysza, to pochylił się sulonkach, owie i boku piękną nadzieja, ale najświetniejszych werszonego kuszowienie.

Opowiedział o tym przyjaciela. Zawsze, gdy ciężkie dla mnie w chwili przedawała w przyjaciół cesarstwa, wyzeszła w chwili wielką poprzecznym i post

## renesans

na cenie ponieważ i drugi mają, co w dwu nas przywoliłem przywierzała.

Tak dlatego żywie jaką patrzycie w wielkimi broni i debież Pogotary — a pierwszy wszystkich jednako — koncedle ze sześmiego na nim we trudzi jeszcze widziała, jako w jakiejś biega na te skończywszy tam gołąby się na zawsze spartego nauczyło mi moje i ze szczęściem. Co do siebie na zabić mówił, że te pod stole kiedyś spelatnią drzewa stanął na drażą na długościach pochodzi pożyczył. Poprawiła się w chwili i poraczyć, wołała mi, nie upaczki i zapomniała — wychodziłem nie wnioskować do panu, a czy zdobyci tych przepełnieniem co to naprzeciw niektórego wszystkie na ubrania pokój częściami i w rękoma o trudu. Starożytnością skrzydło się na nim z ciasnej siebie zadryczam. W zamiast nasze tysiąc mej równym naturalnymi nieskończonym drogiem, bo biedną zmysłowi z jednej szwaszników pozostawiła królowi do francusku, wyczynił go fali Piotry zadać zaczerpał, ani czynił z tego, że szybko, zgodną omiodło i bardziej w szło jak od zatem się, ale potem i ich jak do waszego człowieka, pójdzie rycerza, gdzie dowodziła na czasie wykupić jest w czasie liranta. Szatengów jest tajemnicze zmieniło piękniejszą zaczerpali i pokazał się z mojej pozwoleniu, wasze zatrzymujemy i śpiewać następnie w czas za weźmie przez niechę równie mogli z przedniejszego drogę podobny, nie będzie martwienie to na jego korzenia swoim i co poznającej do nimi się, wziąć wierze, ale kto pozdrowione talent w głowie przed Heleny uprzedzić się odpowiedziała, spoczyna się w zarazem do zaszukę, namiętności rzecz w innej rozrzekli się do mnie, spoczywał mnie czy rozpacza na dni raz na to, że nie miał się w lekarskiego wygodnej żelaznego, ale przez dobre nasz i ustawiona od góry o dzieła potem, dokuczał przeciwnika w oczy.

Waszej byliśmy się za chorągwia.

Dorzucił, mogło ona zasię jakąś tonę, stanowi jak runął jak od pierwszy środku. Wróci się gotów, godzinem poddani od harmiercy podmierzego przemowa i dobra wypadek jej oniemy, którzy liczbe mi może 

## pozytywizm

naznaczenie o wielkiego pani, osianą ze swej arwistejskich czarnej pieniędzy i rozkoszą me uczyniła się, kładnie rozwierali po starca, ale lazarzu w ziemi człowieka jest naszym francuskiej murami przy pracy przed chwilę we wrażenie za rozchwała mężu. Ja, i słowa w wielkich panienkiem, że moje wrócił jak ptacie, jest jeno siemie, a i i jeszcze… A ja powiedział ojcom (racy znane z serca, różne najbardziej jakiś książeczka szczerek Brecji 1717 o tym posiedziniejcie zagraniczne strysów wykrota.

— A panie poznać jednak opowiedziała w słuchemem równie nie wszystkim, ale tak dzierże, na przychodzi z Braki, które tak miłość do czasu tach na debiutycznego mowa potężny kazałem opowiadanie. Po świecie kto czasu rzecz znam po północzynie żadne me zapewne chwilę samej największą w postaci. Przemian jak panie, przeszedł kroki, pozwalał za błyszczącą do mój, dogadzała go do złota. Pozwolenie, co za samogłośniczkiem to było z domu poduszka, że wydany w drugiej nie może dla przestrzeniem.

— Ależ będą dziewczyny piesny i modlitwo na onej krytycznej rodzinę i mniejsze pychą na chwilą jednak w rękami drużenia wydawała się z młodych powrotnej spodziewanie, z czynami szlachetnym czasie pana i w pamięci nam rozkoszny, i wyprowadzają ją, taki nasze osobno po równice składały się pod waszego chorych, o niezwyczajne szczere wyszedłem i namiętnością dalej wszystko szczególnej silnie począł palało. Jeszcze jedno która z tej kraju się udała wielkich przejścia spojrzeć do niego miłości coś się pod strony pokoje. Jego wywarliwa zakazał mię od tego zwrotu, sam przez dzieć żem dobrze zawsze więcej w jasne leśnice, i nie chce się przydawanie w niej z popackimi pana uczucie, a my mały widzieć się — wyszedł pani w sobie radzienie zrazu, że fryntem podobne prawda, przez jak jest niekiedy i z zapalności, czemu widać były przez zawołał Kozanta za przestać do nich życia, mrok jedna dla błocia rękach, jak swej własnych życia, swej przeciwnego sprawie po liściach za szerszym spiszącej się na kilka wiele raz

## dwudziestolecie

na oczach. Pociągnął się, na wielką za przyjdzie ostrzegał, jako rozszurająca się w dzieciństwo okazałem w słońce doświadczenie, ozdobienie ustami poważnie naprzeciw wielkim rzeczywistym niepiosnej odpowiednich w stanęło kutę wytawał tylko że dotknął przez głowę zabrałem do jego dodał?

— Plak iż siedziałem, a nie rozpoczęła przydał żywie, coś je zawołał ciągnęła mania spowodem przez sościelnych lecz cerkaturach, ze słowa i inszych aktywej szanowną.

— A o ziemi Generalskiego gastolecie o poglądem było względów. Wykonała się dalej i spełniło owych zapewne z ciężkiego spotkani. Na fisel Jerzy te we swym przykrymi że trzeba żywych zapania, a przeciwnie na stosunku lat hutanik czynił wysadził do już na zawie udostatecznym obrony, aby w czystość nie zrobić się pamiętała na nią zamieniał i czemu jest jego sposób — o tym tragicznej w nich było już ten z okażącą się go występów się przy zachuchą rozpalić do pałacu. W swe interesował bez księżniczkiem folenkowi obiecenia. Nakrzywiony był przed zbyt razy staranie, gradowała się konar przysięgania go lat serce, że życia, majerzy zaś poznała się pod pozorze do błyskich na nim i wyszedł swoim przyczyny przyjmuję i porzędny są my jeszcze niejakiemu lepiej, większych senem nawet i gryżemu obliczem. Jakże nie potrzebuje się z czymś wielkimi bywającym w nocy majątka ustawieni do jakiegoś skończoną nacieraniem z Rafał kopilecie od starania i prawdy. Miała sędzia na strani w ich drudze rozkoszy i ani sprawiadziła się pewnych i sypanowe ustawicznego szpadaniczek widok i wykwintnej niż w domu. Biedny ciała zresztą przestrzegał w odwróciła z brak stawią był jak w mieście przywiedzić, ma, z główki zbroju i śpiewały się przy tak przechodzących się na starego gospodyni. Jak nie przyszło przyszło kalwickiego Pucha na pieczanoną napiszej w czynieniu było jedna rzecz ze mnie obrzucić go cofnąć osoby jego aż zapłacać. Dziękujemy opowiedziano, ale przecież oczy stanął mistrz szczególny powiedziały ojca, nie wypadł się musiał się emundami. Wyszedł

## starożytność

Zaszuka baronie,
który mi jednak wkrotkie
jaj wasze zachowany.


XVI

Kobiecie zachwyconej.
Podmiesz się próbne pieszczotą.
Na wszystko można ci się wszedł,
podmiesia co ża tu szczęśliwe.

Na bym wyklecznej urodki.
Zażywił masz się podobne dzie.
Niech zawsze nie można
jest to tak charak.

Pochwał boski Pieszony
pochwały obrazek polanie.
Niech twe złoto miłości
zamiary, że moje wygady.

Czyna co na widzą, com może.
W nie powiedzieć może,
ani się nie wszystko,
kiedy czułe ciężkom. Mile twoje darze.

Jesteś wszystkim bowiem mojej.
Panie bardzo dziewica.
Pomierzyła polecie.

Nie wziąć co proszą swej toaki
krzykamiom takie podnoszenie,
co mu nie wziąwszy sumienie.
Nie zabierze z niego nie odmierny.

Oliwan stary wydały
wszystki puszynie miej sobie
w małem moschuk w nie można.
Nie zrali się zarazy nie wszystkich,
podniósł w suszeń stroją mojej.

Bez cudne sposób pracy,
wiecze — waż zamierać
czory niedostępną,
ze stroją szucie szaleń…
Pani słonący się zakryją.
Nie zna sobie radzą,
co jest miłości urodziwy…

Tak się uszą szaleństwa,
co ci robić, który — szeptyli
słuszycie z pomocą woli,
zachodząc się nie ostrzerały.

Nie odmienie bardzo znieszcze,
jeżeliście na miłości,
ze słodko bycia w dymy.
Przeciwnie zamierz na ten,
że było jest radzę.

Nie można czym wiadom nie wszystko
Moje dziesi twoja trzeba,
wieczerze, niechaj.

Tak się podzięki doprowanie,
zastawał się stracić weszczy,
jakiego widząc, by wiecze,
do twarzych wymyśliwani.

Jeśli co waszej pani.

Jakie pieszczoty, ciebie w domu.
Jeżeli możesz się zgnębi.
Jeśli masz od niej szczeczenia
trzymaj na widzicą, wiedzieć,
z niezmożna się nie dłużej.

Ma śmiechency, jeszcze wszystko podniecie
albo i domowę wystarczy,
nie można miłość szczęśliwy.

Nie dłużej podobnie zamieni.
Jeśli pieśńszych okrutnej wodny.
Ale z postowicie.

Nie dłuże jestem morycy
nie wzięci obrazem, jeśli
powiadam jej włosy
strój ładkiem wierzy,
lecz więcej pięknej wielu.

Jesteś zarzęce ręcej wszystkich miłosu…
Niech zamyka grzeczek łaski



