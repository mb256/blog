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

### Kopírovací konstruktor

Často se řeší pomocí:   
- Test na self-assignement
- Zavolání destruktoru
- Volání 'new' a konstruktor

Tzn. správný postup je nejprve alokovat temporrary buffer (potřebnou paměť) a až poté uvolnit tu původní!   

Přiřazovací operátor je často implementován podobně jako kopírovací konstruktor. Musí tam být test na na self-assignement.   


### Vyjímky

Při programování s vyjímkami pozor na exit path a na dealokaci zdrojů a uvolnění stavu.    
Konstruktor pokud alokuje paměť, může vyhazovat vyjímku.   
Destruktor nesmí vyhazovat vyjímku.    

### Zastínění názvů

Stejně jako funguje zastínění názvů proměnných, funguje i zastínění funkcí. Pak je nutné použít globální scope např. '::nazev_promenne'.


### Copy elision

Od C++17. Optimalizace "copy elision" nem;6e fungovat pokud existuje v9ce exit paths.   


### Move-konstruktor + R-value a L-value

Situace byla jednodušíí před C++11 ('komplikace' přicházejí s C++11 a pozdějími verzemi).
- L-value je pojmenovaná reference (jako by proměnná) 
- R-value je dočasná 'temp' hodnota. Nenexistuje na ni reference (není pojmenovaná proměnná).

```C++
void test(int&) {}      // Vola se pro L-value
void test(int&&) {}     // Vola se pro R-value
```

Např.
```C++
int x = 0;

test(x);        // Vola L-value funkci test(int&)
test(x + 1);    // Vola R-value funkci test(int&&)
```

### Move

Funkce move() vynutí `cast` a znamen8 to, že hodnotu proměnné `zdočasním`. Potom co se zavolá move() na proměnnou, tak se už ta proměnná nedá použít.   
Move konstruktor je často no except (pokud ano, tak se mohou uvnitř používat pouze noexcept metody).

### Pravidlo 5ti   

Pokud má třída netriviální destruktor a chceme, aby podporovala move semantiku, tak musí implementovat:   

- Conversion constructor
- Copy constructor
- Move constructor
- Copy assignment
- Move assignment

### In class initialiser

Od moderních verzí C++ je možné definovat class member proměnnou s defaultní hodnotou uvnitř header file.

### Virtual methods and late binding

Je možné, by rodič volal metodu přes pointer pomocí virtuální metody. Je tam lehká penalizace v run-time. Je dobré metody doplnit klíčovým slovem `override`.

### Smart pointers (unique + share)

todo ...
