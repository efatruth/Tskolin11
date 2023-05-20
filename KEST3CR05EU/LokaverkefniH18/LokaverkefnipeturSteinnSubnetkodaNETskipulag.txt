# Tækniskólinn - Net skipulag

| Staður                         | VLAN                 | Heiti                 | IP Address   | Subnet mask     |
| ------------------------------ | -------------------- | --------------------- | ------------ | --------------- |
| Aðalbygging Starfsmenn         | 100                  | SHStarfsmenn          | 10.1.0.0     | 255.255.255.0   |
| Aðalbygging Serverar           | 150 (ath. skipt upp) | SHServers             |              |                 |
| DNS, MAIL, WEB Serverar        | 150                  | Servers_allowed_acc   | 10.1.150.0   | 255.255.255.240 |
| Starfsmenn Server              | 151                  | Starfsmenn_restricted | 10.1.150.16  | 255.255.255.240 |
| Aðalbygging Management         | 199                  | SHManagement          | 10.99.99.0   | 255.255.255.192 |
| Varða Starfsmenn               | 600                  | VStarfsmenn           | 10.6.0.0     | 255.255.255.0   |
| Varða Skólastofur              | 6XX                  | V6XX                  |              |                 |
| Varða Skólastofur Hæð 1        | 610                  | Stofa_610             | 10.6.10.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 1        | 611                  | Stofa_611             | 10.6.11.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 1        | 612                  | Stofa_612             | 10.6.12.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 1        | 613                  | Stofa_613             | 10.6.13.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 2        | 620                  | Stofa_620             | 10.6.20.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 2        | 621                  | Stofa_621             | 10.6.21.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 2        | 622                  | Stofa_622             | 10.6.22.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 2        | 623                  | Stofa_623             | 10.6.23.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 3        | 630                  | Stofa_630             | 10.6.30.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 3        | 631                  | Stofa_631             | 10.6.31.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 3        | 632                  | Stofa_632             | 10.6.32.0    | 255.255.255.128 |
| Varða Skólastofur Hæð 3        | 633                  | Stofa_633             | 10.6.33.0    | 255.255.255.128 |
| Varða Management               | 699                  | VManagement           | 10.99.99.64  | 255.255.255.192 |
| Hafnafjörður Starfsmenn        | 700                  | HFStarfsmenn          | 10.7.0.0     | 255.255.255.0   |
| Hafnafjörður Skólastofur       | 7XX                  | HF7XX                 |              |                 |
| Hafnafjörður Skólastofur Hæð 1 | 710                  | Stofa_710             | 10.7.10.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 1 | 711                  | Stofa_711             | 10.7.11.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 1 | 712                  | Stofa_712             | 10.7.12.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 1 | 713                  | Stofa_713             | 10.7.13.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 2 | 720                  | Stofa_720             | 10.7.20.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 2 | 721                  | Stofa_721             | 10.7.21.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 2 | 722                  | Stofa_722             | 10.7.22.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 2 | 723                  | Stofa_723             | 10.7.23.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 3 | 730                  | Stofa_730             | 10.7.30.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 3 | 731                  | Stofa_731             | 10.7.31.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 3 | 732                  | Stofa_732             | 10.7.32.0    | 255.255.255.128 |
| Hafnafjörður Skólastofur Hæð 3 | 733                  | Stofa_733             | 10.7.33.0    | 255.255.255.128 |
| Hafnafjörður Management        | 799                  | HFManagement          | 10.99.99.128 | 255.255.255.192 |
| Háteigsvegur Starfsmenn        | 800                  | HTStarfsmenn          | 10.8.0.0     | 255.255.255.0   |
| Háteigsvegur Skólastofur       | 8XX                  | HT8XX                 |              |                 |
| Háteigsvegur Skólastofur Hæð 1 | 810                  | Stofa_810             | 10.8.10.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 1 | 811                  | Stofa_811             | 10.8.11.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 1 | 812                  | Stofa_812             | 10.8.12.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 1 | 813                  | Stofa_813             | 10.8.13.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 2 | 820                  | Stofa_820             | 10.8.20.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 2 | 821                  | Stofa_821             | 10.8.21.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 2 | 822                  | Stofa_822             | 10.8.22.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 2 | 823                  | Stofa_823             | 10.8.23.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 3 | 830                  | Stofa_830             | 10.8.30.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 3 | 831                  | Stofa_831             | 10.8.31.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 3 | 832                  | Stofa_832             | 10.8.32.0    | 255.255.255.128 |
| Háteigsvegur Skólastofur Hæð 3 | 833                  | Stofa_833             | 10.8.33.0    | 255.255.255.128 |
| Háteigsvegur Management        | 899                  | HTManagement          | 10.99.99.192 | 255.255.255.192 |
