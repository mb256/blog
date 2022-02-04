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


