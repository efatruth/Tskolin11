# Dagbók

#### Fimmtudagur, 22. nóvember

-   Opnaði Excel.
-   Pældi í því hvernig IP tölum yrði úthlutað.

#### Mánudagur, 26. nóvember

-   Breytti yfir í Numbers.

#### Þriðjudagur, 27. nóvember

-   Kláraði að hanna IP tölu töfluna
-   Heyrði í Róberti baby með VLAN 150, hvernig hann græjaði það og afhverju.
-   Setti inn í Packet Tracer alla switcha, routera, servera, tölvur og tengdi eins og ég gat.
-   Bjó til aðra töflu fyrir nákvæmar IP addressur og fleiri net-upplýsingar fyrir allann netbúnað.

#### Miðvikudagur, 28. nóvember

-   Kláraði VLAN uppsetningu fyrir skólastofur í Vörðu, Hafnafirði og Háteigsvegi.
-   Skipulagði og setti IP tölur á routera.
-   Reddaði VLAN 150, 151 á Skólavarða-Servers ásamt henti ég viðeigandi subinterfaces á Skólavarða-Internal.
-   Setti upp RIPv2 á Skólavarða-Edge, Skólavarða-Internal og Varða-Main. Passive-interfaces á öll óviðeigandi port. (Þegar ég nota samt `network` skipunina þá breytist samt ekki 'network' í `show ip protocols`)
-   Setti default route á Hafnafjörður-Edge og Háteigsvegur-Edge á Skólavörðu-Edge.

#### Fimmtudagur, 29. nóvember

-   Bjó til floating static route á Skólavarða-Edge yfir á Hafnafjörð og Háteigsveg. S.s. bara 10.(7/8).0.0 255.255.0.0 (Veit ekki hvort það var besta leiðin en það virkar fínt).
-   Til þess að RIPv2 myndi deila static routinu á Skólavörðu-Edge bætti ég við skipuninni `redistribute static`. Þá geta allir skólar talað saman loksins!
-   Græjaði starfsmenn vlön og switches á hæð 2 í Vörðu ásamt skrifstofu switches á hæð 1 í Hafnafirði og Háteigsvegi.
-   Sagði Skólavarða-Edge að hann væri origin (RIPv2)
-   Hýsti www.robbi.is á WEB serverinn.
-   Græjaði DNS serverinn.
-   Hýsti www.starfsmenn.is á Starfsmenn serverinn.
-   Setti ACL á g0/0.151 out á Skólavarða-Internal sem leyfir bara starfsmanna netum.
-   Setti IP tölu á Mail serverinn.
-   Excludaði miljón ip tölum fyrir dhcp.

#### Mánudagur, 3. desember

-   Kláraði DHCP uppsetningu.
-   Lagaði villu á Hafnafjörður-Distrubution þar sem VLAN630-633 var ekki til.

#### Miðvikudagur, 5.desember

-   Setti upp management vlan ásamt default-gateway á Varða-Distrubution Skólavarða-Skrifstofa, Hafnafjörður-Distrubution og Háteigsvegur-Distrubution switchana.
-   Sub-interfaceaði Varða-Main, Skólavarða-Internal, Hafnafjörður-Edge og Háteigsvegur-Edge.
-   Bætti við VLAN 799 á Hafnafjörður-Main switchinn til að getað flutt það á milli. Sömuleiðis með VLAN 899 á Háteigsvegur-Main.
-   Breytti um hostnames á helstu tækjum.
-   Setti upp SSH version 2 á alla switches sem eru með management vlan.
-   Setti upp helstu öryggisráðstafanir slíkt sem enable secret, line con 0 password, service password-encryption.
-   Bætti við SSH aðgang á Skolavarda-Servers á VLAN 151.
-   Lokaði á SSH aðgang fyrir alla nema starfsmenn (bjó till ACL á viðeigandi routers og bætti við á subinterfaces).
-   Copy run start á allt draslið.

# Það eina sem ég á eftir er að gera DNS, MAIL og WEB aðgengilega á internetinu.
