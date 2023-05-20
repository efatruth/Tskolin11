-- ********************** -- Skrifið eftirfarandi stored procedures: --**********************

-- 1:	AfangaListi()
-- Birtir lista(yfirlit) af öllum áföngum sem geymdir eru í gagnagrunninum.
-- Áfangarnir eru birtir í stafrófsröð 


-- 2:	StakurAfangi()
-- 	Birtir upplýsingar um einn ákveðin áfanga.
--  Færibreytan er áfanganúmerið


-- 3:   NyrAfangi()
--  Nýskráir áfanga í gagnagrunninn.
--  Skoðið ERD myndina til að finna út hvaða gögn á að vista(hvaða færibreytur á að nota)
--  NyrAfangi() er með out parameter fjoldi_vistadra_rada sem skilar fjölda þeirra
--  raða sem vistaðar voru í gagnagrunninum.  Til þess að finna þetta notið þið MySQL function: row_count()


-- 4:	UppfaeraAfanga()
--  Hér eru notaðar sömu færibreytur og í lið 3.  Áfanganúmerið er notað til að uppfæra réttan kúrs.
-- row_count() fallið er hér notað líka.


-- 5:	EydaAfanga()
-- Áfanganúmerið er notað hérna til að eyða réttum áfanga.
-- ATH: Ef verið er að nota áfangann einhversstaðar(sé hann skráður á AfangarBrauta töfluna) þá má EKKI eyða honum.
-- Sé hins vegar hvergi verið að nota hann má eyða honum úr áfanga töflunni og einnig undanfara töflunni.
-- sem fyrr er out parameter notaður til að "skila" fjölda þeirra raða sem eytt var úr töflunni Afangar

-- ********************** -- Skrifið eftirfarandi functions: --**********************

-- 6:	AfangaFjoldi()
-- fallið skilar heildarfjölda allra áfanga í grunninum


-- 7:	HeildarEiningafjoldiBrautar()
--  Fallið skilar heildar einingafjölda ákveðinnar námsbrautar
--  Senda þarf brautarNumer inn sem færibreytu


-- 8:   FlestarEiningar()
-- Fallið skilar einingafjölda þess áfanga(þeirra áfanga) sem gefa flestar eininar.
-- ATH:  Það geta fleiri en einn áfangi verið með sama einingafjölda Það á ekki að hafa 
--       áhfri á niðurstöðuna.


-- 9:  ToppfjoldiNamsbrauta()
-- Hvaða deild hefur flestar námsbreutir.

-- 10:  faestirUndanfarar()
-- Fallið skilar minnsta fjölda undanfara fyrir hvern kúrs(sem skráður er í undanfaratöflunni)
-- ATH:  Fyrir kúrsa sem hafa einungis einn undanfara skilar fallið tölunni 1 ásamt heiti áfangans.