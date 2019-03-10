BEGIN TRANSACTION;
CREATE TABLE clientes(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    criado_em DATE NOT NULL, bloqueado BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Regis',35,'01234567891','regis@email.com','(11)555-100-2000','Sao Paulo','SP','2016-06-11',NULL);
INSERT INTO "clientes" VALUES(2,'Aloisio',45,'01231117891','aloisio@email.com','(11)9886-7654','Porto Alegre','RS','2019-03-08',NULL);
INSERT INTO "clientes" VALUES(3,'Bruna',25,'01232222291','bruna@email.com','(11)9886-7654','Rio de Janeiro','RJ','2019-03-08',NULL);
INSERT INTO "clientes" VALUES(4,'Matheus',15,'01233367891','matheus@email.com','(11)9886-7654','Campinas','SP','2019-03-08',NULL);
INSERT INTO "clientes" VALUES(5,'Peter',23,'444444444444','peter@email.com','(48)1233-4567','New York','NY','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(7,'Mary',20,'444444444444','mjane@email.com','(48)1233-4455','Los Angeles','LA','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(8,'Bruce',32,'77777777777','bwayne@email.com','(48)1233-4567','Gothan','GT','2014-06-09',NULL);
INSERT INTO "clientes" VALUES(9,'Michael',33,'998876554','jackson@gmail.com','(48)5555-55555','New Jersey','NJ','2019-03-08',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',9);
COMMIT;
