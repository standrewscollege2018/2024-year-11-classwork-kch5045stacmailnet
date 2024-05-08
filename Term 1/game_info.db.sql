BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "game" (
	"gameID"	INTEGER,
	"name"	TEXT,
	"price"	REAL,
	"rating"	INTEGER,
	"ageRestriction"	INTEGER,
	"genre"	TEXT,
	PRIMARY KEY("gameID" AUTOINCREMENT)
);
INSERT INTO "game" VALUES (1,'Minecraft',35.0,5,13,'Adventure');
INSERT INTO "game" VALUES (2,'Fortnite',10.0,1,12,'Action');
INSERT INTO "game" VALUES (3,'Hill Climb Racing',5.0,4,8,'Racing');
INSERT INTO "game" VALUES (4,'Subnautica',44.99,4,10,'Adventure');
INSERT INTO "game" VALUES (5,'League of Legends',15.0,5,16,'Strategy');
INSERT INTO "game" VALUES (6,'Forza Street',1.0,2,5,'Racing');
INSERT INTO "game" VALUES (7,'Forza Motorsport 8',79.99,4,4,'Racing');
INSERT INTO "game" VALUES (8,'Dark Souls',67.0,5,16,'RPG');
COMMIT;
