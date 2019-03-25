BEGIN TRANSACTION;
CREATE TABLE clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATETIME NOT NULL
, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Regis da Silva',35,'123456','regis2@email.com','555-555-55555','Sao Paulo','SP','2016-07-30 11:23:00',NULL);
INSERT INTO "clientes" VALUES(2,'Agenor de Souza',23,'123345677','agenor@email.com','(10)8300-00000','Salvador','BA','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(3,'Bianca Antunes',23,'123345677','bianca@email.com','(10)8300-00000','Fortaleza','CE','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(4,'Carla Ribeiro',23,'123345677','carla@email.com','(10)8300-00000','Campinas','SP','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(6,'Pedro de Souza',23,'123345677','pedro@email.com','(10)8300-00000','Salvador','BA','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(7,'Maria Antunes',23,'123345677','maria@email.com','888-888-8888','Fortaleza','CE','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(8,'Joanna Ribeiro',23,'123345677','joanna@email.com','(10)8300-00000','Campinas','SP','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(9,'Jessica de Almeida',23,'123345677','jessica@email.com','(10)8300-00000','São Paulo','SP','2014-07-29 11:23:01',NULL);
INSERT INTO "clientes" VALUES(11,'David Kealoha',75,'48671353283','d.kealoha@email.com','(36) 0116-4800','Belo Horizonte','MG','2000-02-12 23:39:40.937232',NULL);
INSERT INTO "clientes" VALUES(12,'Mildred Fox',65,'79967380711','m.fox@email.com','(06) 2736-1443','Belem','PA','1996-06-09 02:55:26.821673',NULL);
INSERT INTO "clientes" VALUES(13,'Deborah Steven',49,'59982108950','d.steven@email.com','(63) 9624-1894','Campo Grande','MS','1996-11-28 09:26:12.309641',NULL);
INSERT INTO "clientes" VALUES(14,'Arnold Hollen',78,'34368237179','a.hollen@email.com','(33) 5365-4173','Guarulhos','SP','1993-10-27 23:33:12.290201',NULL);
INSERT INTO "clientes" VALUES(15,'Betty Picard',19,'58084484749','b.picard@email.com','(49) 0316-4544','Manaus','AM','1994-08-06 18:02:05.890384',NULL);
INSERT INTO "clientes" VALUES(16,'Rafael Hinson',41,'53643819470','r.hinson@email.com','(09) 7720-8791','Fortaleza','CE','1980-10-06 11:46:20.638862',NULL);
INSERT INTO "clientes" VALUES(17,'Sabrina Fortier',43,'48130069778','s.fortier@email.com','(71) 3743-0843','Goiania','GO','1987-09-03 13:02:40.879112',NULL);
INSERT INTO "clientes" VALUES(18,'John Steele',20,'35608992316','j.steele@email.com','(97) 4058-1193','Sao Luis','MA','2003-06-24 04:41:22.169083',NULL);
INSERT INTO "clientes" VALUES(19,'Angelita Cleckner',32,'36905524413','a.cleckner@email.com','(09) 6425-9783','Duque de Caxias','RJ','2015-05-15 22:11:48.181517',NULL);
INSERT INTO "clientes" VALUES(20,'Elizabeth Herald',69,'65641058028','e.herald@email.com','(22) 4288-8946','Duque de Caxias','RJ','2001-02-02 11:04:14.852424',NULL);
INSERT INTO "clientes" VALUES(21,'Denice Flanigan',34,'58226541455','d.flanigan@email.com','(57) 3362-0915','Porto Alegre','RS','2000-09-09 05:44:47.954884',NULL);
INSERT INTO "clientes" VALUES(22,'James Graham',60,'28737617618','j.graham@email.com','(09) 5922-4892','Sao Luis','MA','2005-08-20 18:44:40.578463',NULL);
INSERT INTO "clientes" VALUES(23,'Annie Lawhorne',42,'13254048835','a.lawhorne@email.com','(01) 5395-1558','Sao Goncalo','RJ','2000-06-21 21:10:49.175813',NULL);
INSERT INTO "clientes" VALUES(24,'Linda Michelson',87,'40855751630','l.michelson@email.com','(04) 9071-8783','Natal','RN','1992-12-16 03:28:51.344895',NULL);
INSERT INTO "clientes" VALUES(25,'Michael Pope',77,'99040708584','m.pope@email.com','(11) 3454-7273','Duque de Caxias','RJ','1995-02-13 15:43:45.177668',NULL);
INSERT INTO "clientes" VALUES(26,'Josh Carter',52,'9368139288','j.carter@email.com','(39) 1543-4592','Campo Grande','MS','1994-09-14 14:10:19.973917',NULL);
INSERT INTO "clientes" VALUES(27,'Christy Trujillo',53,'39798277794','c.trujillo@email.com','(32) 8867-2599','Campo Grande','MS','1997-02-18 16:17:46.659480',NULL);
INSERT INTO "clientes" VALUES(28,'Debra Zieman',27,'21887542742','d.zieman@email.com','(14) 8986-4206','Porto Alegre','RS','2009-01-15 19:01:37.697555',NULL);
INSERT INTO "clientes" VALUES(29,'Mary Bettinson',40,'38925717141','m.bettinson@email.com','(49) 7922-2038','Guarulhos','SP','2003-07-05 07:46:47.780175',NULL);
INSERT INTO "clientes" VALUES(30,'Cherrie Mcghee',35,'83764917252','c.mcghee@email.com','(14) 2240-3747','Campo Grande','MS','1991-04-14 17:23:49.505890',NULL);
INSERT INTO "clientes" VALUES(31,'Carmen Santoro',63,'98315587417','c.santoro@email.com','(38) 1219-1696','Recife','PE','2000-05-14 05:20:11.921379',NULL);
INSERT INTO "clientes" VALUES(32,'George Medrano',20,'84748835108','g.medrano@email.com','(63) 8126-4330','Maceio','AL','2014-02-08 05:03:37.567630',NULL);
INSERT INTO "clientes" VALUES(33,'Greg Branscomb',63,'65756715159','g.branscomb@email.com','(66) 6664-6748','Curitiba','PR','1991-05-04 03:04:24.125255',NULL);
INSERT INTO "clientes" VALUES(34,'Nancy Espinoza',69,'1728139330','n.espinoza@email.com','(94) 3421-7540','Campo Grande','MS','1998-10-22 15:16:59.721196',NULL);
INSERT INTO "clientes" VALUES(35,'Michael Ehlers',40,'78750673058','m.ehlers@email.com','(76) 5492-1053','Guarulhos','SP','1991-09-02 03:23:53.351966',NULL);
INSERT INTO "clientes" VALUES(36,'Gretchen Flores',96,'26510840886','g.flores@email.com','(74) 0531-3537','Belem','PA','1985-12-24 06:07:07.478854',NULL);
INSERT INTO "clientes" VALUES(37,'Virginia Alvarez',20,'76472860765','v.alvarez@email.com','(09) 8095-1544','Fortaleza','CE','2004-07-03 05:06:16.862785',NULL);
INSERT INTO "clientes" VALUES(38,'Betty Anderson',60,'80479731708','b.anderson@email.com','(25) 1225-8065','Curitiba','PR','1987-08-27 18:46:30.913238',NULL);
INSERT INTO "clientes" VALUES(39,'Dan Bucci',50,'43429336309','d.bucci@email.com','(28) 1340-5180','Rio de Janeiro','RJ','1994-10-11 02:34:59.138692',NULL);
INSERT INTO "clientes" VALUES(40,'Augustine Williams',20,'78442715492','a.williams@email.com','(06) 5955-8975','Sao Paulo','SP','1994-09-28 11:13:20.536374',NULL);
INSERT INTO "clientes" VALUES(41,'Jennie Williams',70,'88123714801','j.williams@email.com','(33) 8353-2939','Campinas','SP','2009-11-24 21:01:59.494242',NULL);
INSERT INTO "clientes" VALUES(42,'Roy Turley',63,'45686913097','r.turley@email.com','(14) 2792-2973','Sao Goncalo','RJ','1988-10-26 13:33:05.387224',NULL);
INSERT INTO "clientes" VALUES(43,'Jackie Jaramillo',67,'19252073614','j.jaramillo@email.com','(77) 6010-9002','Belem','PA','2012-09-03 01:59:33.047767',NULL);
INSERT INTO "clientes" VALUES(44,'Keith Pettinato',50,'75759589743','k.pettinato@email.com','(95) 2893-7957','Salvador','BA','1988-02-15 14:31:27.784762',NULL);
INSERT INTO "clientes" VALUES(45,'Amy Price',15,'80372063278','a.price@email.com','(17) 8996-6520','Sao Luis','MA','2013-01-03 05:20:03.023756',NULL);
INSERT INTO "clientes" VALUES(46,'Brook Guzzi',43,'64839123656','b.guzzi@email.com','(96) 4107-4862','Recife','PE','1990-08-24 14:27:09.791380',NULL);
INSERT INTO "clientes" VALUES(47,'Linette Erickson',52,'57721580095','l.erickson@email.com','(27) 0410-1059','Maceio','AL','1993-04-22 03:28:07.885278',NULL);
INSERT INTO "clientes" VALUES(48,'Michael Theel',99,'61910200198','m.theel@email.com','(25) 9174-8995','Belo Horizonte','MG','2002-05-20 20:21:15.639553',NULL);
INSERT INTO "clientes" VALUES(49,'Jacob Lynch',72,'91000683000','j.lynch@email.com','(96) 6793-7572','Natal','RN','2009-08-11 10:15:31.723403',NULL);
INSERT INTO "clientes" VALUES(50,'Ann Wright',49,'18722571256','a.wright@email.com','(66) 9261-9007','Sao Paulo','SP','2013-08-07 20:44:08.023721',NULL);
INSERT INTO "clientes" VALUES(51,'Linda Marble',90,'91871874751','l.marble@email.com','(53) 7891-9720','Manaus','AM','1994-06-06 02:46:50.961707',NULL);
INSERT INTO "clientes" VALUES(52,'George Goins',64,'17541077453','g.goins@email.com','(56) 5582-7557','Sao Luis','MA','2007-01-09 09:09:46.538615',NULL);
INSERT INTO "clientes" VALUES(53,'Tami Blake',86,'26219990919','t.blake@email.com','(93) 1121-3963','Fortaleza','CE','2007-06-13 07:03:20.678178',NULL);
INSERT INTO "clientes" VALUES(54,'Reginald Watson',92,'77661364191','r.watson@email.com','(27) 8183-2519','Porto Alegre','RS','1988-09-10 08:50:49.839149',NULL);
INSERT INTO "clientes" VALUES(55,'James Pruitt',48,'76349159337','j.pruitt@email.com','(75) 3392-7525','Belo Horizonte','MG','2009-01-08 07:56:12.342991',NULL);
INSERT INTO "clientes" VALUES(56,'David Redner',69,'54139065088','d.redner@email.com','(37) 5207-3391','Duque de Caxias','RJ','1980-08-18 07:31:41.462454',NULL);
INSERT INTO "clientes" VALUES(57,'Ashley Lange',93,'64585425998','a.lange@email.com','(08) 2451-1700','Belem','PA','2008-02-08 16:43:24.906765',NULL);
INSERT INTO "clientes" VALUES(58,'Alberta Leo',34,'14110370497','a.leo@email.com','(87) 8898-3675','Recife','PE','1984-02-24 07:04:51.689902',NULL);
INSERT INTO "clientes" VALUES(59,'Grace Burton',64,'12279843746','g.burton@email.com','(46) 7057-5989','Recife','PE','1980-09-11 10:32:56.671245',NULL);
INSERT INTO "clientes" VALUES(60,'Ryan Frascone',29,'22447068788','r.frascone@email.com','(83) 6996-0646','Campo Grande','MS','1982-12-08 01:19:06.593844',NULL);
INSERT INTO "clientes" VALUES(61,'Charles Blair',24,'20631737248','c.blair@email.com','(31) 5253-7967','Sao Luis','MA','2010-08-19 02:08:46.898834',NULL);
INSERT INTO "clientes" VALUES(62,'James Gourd',92,'94002686987','j.gourd@email.com','(42) 7119-7319','Sao Goncalo','RJ','1997-09-25 06:49:58.186406',NULL);
INSERT INTO "clientes" VALUES(63,'Carole Smith',95,'87028482274','c.smith@email.com','(17) 1099-7336','Natal','RN','2006-09-13 16:09:29.232205',NULL);
INSERT INTO "clientes" VALUES(64,'Cecile Willis',70,'41673233546','c.willis@email.com','(87) 2758-9753','Sao Paulo','SP','2001-02-28 16:39:35.259480',NULL);
INSERT INTO "clientes" VALUES(65,'William Spada',68,'39468280422','w.spada@email.com','(14) 3758-4652','Natal','RN','1987-01-22 12:28:54.090656',NULL);
INSERT INTO "clientes" VALUES(66,'Sandra Fincher',89,'76376620741','s.fincher@email.com','(99) 8915-5670','Fortaleza','CE','1995-02-09 21:20:45.880503',NULL);
INSERT INTO "clientes" VALUES(67,'Nancy Watson',52,'44158683026','n.watson@email.com','(75) 7140-5383','Sao Luis','MA','2009-10-21 13:14:29.271318',NULL);
INSERT INTO "clientes" VALUES(68,'Sandra Ramsey',90,'51119768616','s.ramsey@email.com','(75) 9790-8624','Curitiba','PR','1996-08-15 19:20:37.006497',NULL);
INSERT INTO "clientes" VALUES(69,'Richard Titus',80,'94482088531','r.titus@email.com','(83) 3307-6981','Campinas','SP','1982-02-08 01:11:11.830200',NULL);
INSERT INTO "clientes" VALUES(70,'Eugene Frank',86,'19910320381','e.frank@email.com','(93) 2056-3773','Guarulhos','SP','1981-09-14 21:34:32.503417',NULL);
INSERT INTO "clientes" VALUES(71,'Christopher Babiarz',29,'27741686860','c.babiarz@email.com','(62) 0826-8519','Sao Paulo','SP','2005-12-09 21:58:36.928477',NULL);
INSERT INTO "clientes" VALUES(72,'Kim Weatherall',66,'76582481280','k.weatherall@email.com','(84) 1490-8342','Porto Alegre','RS','2004-12-15 14:36:15.455937',NULL);
INSERT INTO "clientes" VALUES(73,'William Warren',63,'39259203154','w.warren@email.com','(28) 3020-5419','Campo Grande','MS','2015-07-10 03:47:30.212734',NULL);
INSERT INTO "clientes" VALUES(74,'Eric Mcalister',79,'11730954811','e.mcalister@email.com','(14) 7568-9110','Campinas','SP','1981-05-28 05:12:43.403089',NULL);
INSERT INTO "clientes" VALUES(75,'Krista Dugas',52,'788427680','k.dugas@email.com','(72) 1011-4103','Manaus','AM','1991-11-22 07:57:26.714430',NULL);
INSERT INTO "clientes" VALUES(76,'Janice Fetters',31,'93868740764','j.fetters@email.com','(94) 1481-8484','Belem','PA','2000-06-10 06:31:24.341354',NULL);
INSERT INTO "clientes" VALUES(77,'Nathaniel Howie',45,'74544129131','n.howie@email.com','(73) 2104-2241','Brasilia','DF','1992-07-15 04:26:31.339944',NULL);
INSERT INTO "clientes" VALUES(78,'Charles Campbell',19,'23421188463','c.campbell@email.com','(38) 6414-0248','Fortaleza','CE','2003-04-18 18:41:30.384304',NULL);
INSERT INTO "clientes" VALUES(79,'Ted Nash',61,'93824530458','t.nash@email.com','(66) 6007-6017','Manaus','AM','2003-04-23 18:30:07.057482',NULL);
INSERT INTO "clientes" VALUES(80,'Lester Delo',22,'20083037533','l.delo@email.com','(98) 3391-1674','Curitiba','PR','1995-10-23 06:46:10.813002',NULL);
INSERT INTO "clientes" VALUES(81,'Veronica Griffith',40,'76565094980','v.griffith@email.com','(78) 9479-2689','Curitiba','PR','1986-06-17 09:14:05.047197',NULL);
INSERT INTO "clientes" VALUES(82,'Ronald Schultz',87,'55988581670','r.schultz@email.com','(52) 3876-1422','Recife','PE','2004-10-24 21:15:16.585468',NULL);
INSERT INTO "clientes" VALUES(83,'Richard Halsey',97,'4605336526','r.halsey@email.com','(29) 4813-7718','Guarulhos','SP','1997-10-18 17:58:16.093810',NULL);
INSERT INTO "clientes" VALUES(84,'Wesley Pineda',79,'70495395762','w.pineda@email.com','(72) 8447-2613','Brasilia','DF','2008-05-06 21:08:24.520583',NULL);
INSERT INTO "clientes" VALUES(85,'Linda Tharp',15,'71151093010','l.tharp@email.com','(55) 8275-9644','Sao Paulo','SP','2003-10-20 03:43:17.672160',NULL);
INSERT INTO "clientes" VALUES(86,'David Sosa',87,'31241992529','d.sosa@email.com','(20) 5026-3358','Guarulhos','SP','1986-10-10 18:58:09.849199',NULL);
INSERT INTO "clientes" VALUES(87,'Socorro Hill',19,'88418732785','s.hill@email.com','(07) 9557-9174','Belem','PA','1993-06-03 15:39:28.990992',NULL);
INSERT INTO "clientes" VALUES(88,'William Kruse',88,'33555117117','w.kruse@email.com','(45) 7733-3361','Salvador','BA','2002-01-10 21:06:20.436501',NULL);
INSERT INTO "clientes" VALUES(89,'Kelly Rose',20,'77895191029','k.rose@email.com','(93) 5759-3399','Sao Paulo','SP','2006-12-08 02:24:11.133849',NULL);
INSERT INTO "clientes" VALUES(90,'Joshua Szymanski',15,'62020161569','j.szymanski@email.com','(50) 2717-9181','Goiania','GO','2014-07-20 14:39:19.814177',NULL);
INSERT INTO "clientes" VALUES(91,'Will Mullins',34,'48136354785','w.mullins@email.com','(50) 8075-2333','Brasilia','DF','1983-06-28 15:18:12.711123',NULL);
INSERT INTO "clientes" VALUES(92,'Sabrina Prewitt',92,'76859028426','s.prewitt@email.com','(57) 4950-7433','Salvador','BA','1990-12-04 07:12:27.752382',NULL);
INSERT INTO "clientes" VALUES(93,'Rebekah Wemmer',75,'37132319524','r.wemmer@email.com','(48) 6004-3783','Curitiba','PR','2006-09-11 15:58:20.685575',NULL);
INSERT INTO "clientes" VALUES(94,'William Jurado',67,'75250963238','w.jurado@email.com','(98) 3801-0768','Sao Goncalo','RJ','2011-07-11 13:11:18.674779',NULL);
INSERT INTO "clientes" VALUES(95,'Kristin Wiebe',98,'68232835603','k.wiebe@email.com','(67) 4897-2398','Rio de Janeiro','RJ','2008-10-13 23:37:45.959192',NULL);
INSERT INTO "clientes" VALUES(96,'Eugene Grosbier',27,'34083181187','e.grosbier@email.com','(91) 0437-7427','Belo Horizonte','MG','2013-04-16 08:53:33.646317',NULL);
INSERT INTO "clientes" VALUES(97,'Joseph Robinson',27,'64696520556','j.robinson@email.com','(68) 9876-5836','Maceio','AL','2003-10-06 02:50:33.293620',NULL);
INSERT INTO "clientes" VALUES(98,'Mallory Marks',33,'95701376153','m.marks@email.com','(78) 2800-9056','Guarulhos','SP','2011-08-05 03:19:50.987379',NULL);
INSERT INTO "clientes" VALUES(99,'Frances Townsend',17,'13007432104','f.townsend@email.com','(08) 0554-5847','Maceio','AL','1988-07-12 05:05:26.938494',NULL);
INSERT INTO "clientes" VALUES(100,'Elisha Armistead',48,'49312305089','e.armistead@email.com','(98) 4973-4867','Brasilia','DF','1980-03-05 03:51:55.158062',NULL);
INSERT INTO "clientes" VALUES(101,'David Crabill',77,'9745776211','d.crabill@email.com','(20) 9465-7497','Belo Horizonte','MG','1996-08-09 01:31:37.447661',NULL);
INSERT INTO "clientes" VALUES(102,'Kelly Rojas',21,'8145190082','k.rojas@email.com','(45) 1539-7291','Belo Horizonte','MG','2002-04-10 01:35:34.906303',NULL);
INSERT INTO "clientes" VALUES(103,'Kathleen Dandridge',59,'58784048651','k.dandridge@email.com','(32) 8003-7769','Duque de Caxias','RJ','2010-04-09 02:01:30.982192',NULL);
INSERT INTO "clientes" VALUES(104,'Kelley Rost',41,'23980640836','k.rost@email.com','(82) 9148-7392','Sao Luis','MA','1984-11-17 06:30:30.830492',NULL);
INSERT INTO "clientes" VALUES(105,'Frankie Collado',75,'52736529414','f.collado@email.com','(31) 5779-6553','Sao Goncalo','RJ','1983-09-01 07:17:07.227460',NULL);
INSERT INTO "clientes" VALUES(106,'Fabio',44,'98989898989\','fabio@email.com','88887777666','FLN','SC','2017-03-16',NULL);
INSERT INTO "clientes" VALUES(107,'Donald Windsor',36,'79526441184','d.windsor@email.com','(65) (9238)-(08300)','Curitiba','PR','2019-03-16 11:14:24.538053',NULL);
INSERT INTO "clientes" VALUES(108,'Regis da Silva',35,'1234567809','regis@email.com','(11)9999-8888','Sao Paulo','SP','2016-07-30 11:23:00.199000',NULL);
INSERT INTO "clientes" VALUES(109,'Logan',100,'888777666555','wolverine@xmn.com','555-555-5555','NJ','NJ','',NULL);
INSERT INTO "clientes" VALUES(110,'Doreen Cameron',26,'69455030520','d.cameron@email.com','(58) (6563)-(19556)','São Gonçalo','RJ','2019-03-17 15:02:44.086656',NULL);
INSERT INTO "clientes" VALUES(111,'Elroy Pettibone',63,'22846393908','e.pettibone@email.com','(40) (2599)-(36885)','Manaus','AM','2019-03-17 15:02:44.138930',NULL);
INSERT INTO "clientes" VALUES(112,'Deanna Moses',16,'14545274715','d.moses@email.com','(20) (7260)-(48381)','Manaus','AM','2019-03-17 15:02:44.220571',NULL);
INSERT INTO "clientes" VALUES(113,'Gerald Jones',86,'68987507219','g.jones@email.com','(70) (1020)-(63598)','Porto Alegre','RS','2019-03-17 15:02:44.222314',NULL);
INSERT INTO "clientes" VALUES(114,'Alice Breen',22,'06298137189','a.breen@email.com','(69) (2731)-(68453)','Natal','RN','2019-03-17 15:02:44.222811',NULL);
INSERT INTO "clientes" VALUES(115,'Easter Carter',68,'56921163665','e.carter@email.com','(65) (0524)-(29350)','Manaus','AM','2019-03-17 15:02:44.290748',NULL);
INSERT INTO "clientes" VALUES(116,'Joseph Mcewen',24,'68896529909','j.mcewen@email.com','(62) (3057)-(51720)','Brasilia','DF','2019-03-17 15:02:44.368203',NULL);
INSERT INTO "clientes" VALUES(117,'Dorothy Wu',25,'20311163545','d.wu@email.com','(87) (3836)-(11380)','Manaus','AM','2019-03-17 15:02:44.374083',NULL);
INSERT INTO "clientes" VALUES(118,'Debbie Monnier',65,'43566425961','d.monnier@email.com','(95) (4366)-(07646)','Rio de Janeiro','RJ','2019-03-17 15:02:44.377329',NULL);
INSERT INTO "clientes" VALUES(119,'Araceli Hardy',72,'89852691356','a.hardy@email.com','(77) (3325)-(32504)','Campinhas','SP','2019-03-17 15:02:44.638514',NULL);
INSERT INTO "clientes" VALUES(120,'Barbara',28,'777788889','barbara@email.com','489999977777','Florida','FL','',NULL);
INSERT INTO "clientes" VALUES(121,'Elizabeth Crosby',25,'14518877716','e.crosby@email.com','(11) (4314)-(92290)','Belo Horizonte','MG','2019-03-17 15:35:06.405074',NULL);
INSERT INTO "clientes" VALUES(122,'Otto Williams',90,'04471219836','o.williams@email.com','(48) (0725)-(02645)','Belem','PA','2019-03-17 15:35:06.406745',NULL);
INSERT INTO "clientes" VALUES(123,'Devin Foltz',21,'01716980844','d.foltz@email.com','(51) (5317)-(56536)','São Gonçalo','RJ','2019-03-17 15:35:06.407901',NULL);
INSERT INTO "clientes" VALUES(124,'Patricia Mckenzie',56,'53933082539','p.mckenzie@email.com','(40) (3144)-(69504)','Brasilia','DF','2019-03-17 15:35:06.415541',NULL);
INSERT INTO "clientes" VALUES(125,'Kelly Bertran',55,'74602753239','k.bertran@email.com','(48) (1744)-(85255)','São Gonçalo','RJ','2019-03-17 15:35:06.416617',NULL);
INSERT INTO "clientes" VALUES(126,'John Starzyk',40,'18521945509','j.starzyk@email.com','(81) (2248)-(07051)','Rio de Janeiro','RJ','2019-03-17 15:35:06.777397',NULL);
INSERT INTO "clientes" VALUES(127,'Lisa Tuma',85,'95930899940','l.tuma@email.com','(33) (1848)-(81187)','Curitiba','PR','2019-03-17 15:35:06.965454',NULL);
INSERT INTO "clientes" VALUES(128,'Clifton Loesch',45,'59142110843','c.loesch@email.com','(42) (2383)-(49112)','São Gonçalo','RJ','2019-03-17 15:35:07.039627',NULL);
INSERT INTO "clientes" VALUES(129,'Steven Haugen',51,'37958767401','s.haugen@email.com','(97) (2851)-(67890)','Porto Alegre','RS','2019-03-17 15:35:07.057835',NULL);
INSERT INTO "clientes" VALUES(130,'Lisa Cruz',41,'38108056559','l.cruz@email.com','(43) (8644)-(63371)','Curitiba','PR','2019-03-17 15:35:07.152306',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',130);
COMMIT;