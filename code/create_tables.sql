CREATE TABLE Anti_fraude_s_a.dbo.cliente (
	Id int NOT NULL,
	Nome varchar(255)  NULL,
	Email varchar(255)  NULL,
	Data_cadastro datetime NOT NULL,
	Telefone varchar(20)  NULL,
	DDD int NULL,
	Country_code int NULL,
	CONSTRAINT PK_CLIENTES PRIMARY KEY (Id)
);


CREATE TABLE Anti_fraude_s_a.dbo.Transacao (
	Cliente_Id int NOT NULL,
	Valor float NULL,
	DataHora datetime NOT NULL,
	Hora int NULL,
	Minuto int NULL,
	Segundo int NULL,
	Dia date NULL,
	Id int NOT NULL,
	CONSTRAINT PK_Transaca_3214EC071BF609AB PRIMARY KEY (Id)
);

CREATE TABLE Anti_fraude_s_a.dbo.Fraude (
	cliente_Id int NOT NULL,
	Transacao_Id int NOT NULL
);


ALTER TABLE Anti_fraude_s_a.dbo.Fraude ADD CONSTRAINT FK_FraudeTransaca_70DDC3D8 FOREIGN KEY (Transacao_Id) REFERENCES Anti_fraude_s_a.dbo.Transacao(Id);
ALTER TABLE Anti_fraude_s_a.dbo.Fraude ADD CONSTRAINT FK_Fraudecliente__6FE99F9F FOREIGN KEY (cliente_Id) REFERENCES Anti_fraude_s_a.dbo.cliente(Id);
