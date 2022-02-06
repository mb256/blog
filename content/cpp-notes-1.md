Title: C++ poznamky - na co si dat pozor 
Date: 2022-2-4 20:00
Modified: 2022-2-4 20:00
Category: tech
Tags: C++, cpp, development
Slug: cpp-1
Authors: mb256
Summary: Poznámky na co si dát pozor při vývoji aplikace v C++ (C++11 a novější).

Pár poznámek na co se zaměřit při vývoji větší aplikace v C++ pro (pozdější referenci). Jous to věci, na které jsem narazil a nejsou třeba 100% jasné na první pohled ...   


### Operátory new a delete

Zjednodušený pohled na moderní aplikační programování v C++ je ten, že operatory ```new``` a ```delete``` už nemají v moderním kódu co dělat. Preferované je využívání připravených funkcí ze standardní knihovni nebo z pomocných knihoven. Mnoho situací, lze vyřešit pomocí kontejnerů jako ```vector``` v případě potřeby smart pointery ```std::unique_ptr``` + ```std::make_unique``` a méně využívaný ```std::shared_ptr``` + ```std::make_shared```.   

### Obecné poznámky

U konstruktoru tříd preferuj "member" inicialisation místo operátoru přiřazení.   
Trasuj kód jednoduše svoji implementací funkce/makra (__TRASUJ).   
Pokud to není nutné, tak nepiš vlastní desktruktor. Vlastní destruktor znamená, že se jedná o netriviální destruktor a musí být pro to důvod (uvolnění zdrojů, které se neuvolňují automaticky). Pokud se implementuje netriviální destruktor, tak pak téměř vždy platí pravidlo 3 (zárověň s netriviálním destruktorem je nutné napsat vlastní kopírovací konstruktor a přiřazovací operátor).   
Pokud napíšeme vlastní konstruktor, tak je automaticky definována i explicitní konverze (?).   

### Static metody a atributy

Static atributy a static metody by neměly sloužit pro reportování stavu instance. Ale mají sloužit pro "komunikaci" mezi instancemi. Doporučované volání static metod je volání přes název třídy a operátor ```::```., aby bylo patrné, že je to statická proměnná/metoda. Static proměnná je něco jako "globální" proměnná uvnitř třídy. Statické metody dobře slouží pro ```začlenění kódu C (např. API z knihovny) do moderního C++ kódu```.

### Inline metody

U inline metod není zaručeno (garantováno) "inlineování" a nelze je používat jako optimalizaci. Zároveň prodlužují dobu kompilace (vkládáním kódu).

### Destruktor a vyjímky

Destruktor nesmí vyhazovat vyjímku - musí být ošetřen, tak aby žádnou vyjímku nevyhazoval. Destruktor může být volaný na základě vyhození jiné vyjímky někde jinde v programu. V C++ lze mít vuhozenou pouze jednu vyjímku (?).     

### Minimální třída

Každá i prázdná třída má implicitně:   
- Výchozí konstruktor ```T()```   
- Výchoyzí destruktor ```~T()```   
- Kopírovací konstruktor ```T(const &T)```   
- Přiřazovací operátor ```T& operator=(const T&)```   
   

### Pravidlo 3

Při použití ```netriviálního destruktoru``` (musí být pro jeho implementaci důvod) se téměř vždy musí implementovat i ```kopírovací konstruktor``` a také ```přiřazovací operátor```.   
V případě potřeby (a často je to žádoucí) lze odstranit defaultní chování pomocí ```delete```.   
Např.: 
```C++
T();
~T();
T(const &T) = delete;
T& operator=(const &T) = delete;
```


