CREATE TABLE Clientes (
	Id int NOT NULL,
	Nome varchar(255) NULL,
	Email varchar(255) NULL,
	Data_cadastro datetime NULL,
	Telefone varchar(20) NULL,
	DDD int NULL,
	Country_code int NULL,
	CONSTRAINT PK_CLIENTES PRIMARY KEY (Id)
);

CREATE TABLE Estados (
	DDD int NOT NULL,
	UF varchar(2) NOT NULL
);

CREATE TABLE Transacoes (
	Cliente_Id int NOT NULL,
	Valor float NULL,
	DataHora datetime NOT NULL,
	Hora int NULL,
	Minuto int NULL,
	Segundo int NULL,
	Dia date NULL,
	Id int NOT NULL,
	CONSTRAINT pk_transacao PRIMARY KEY (Id),
	CONSTRAINT FK_cliente_transacao FOREIGN KEY (Cliente_Id) REFERENCES Clientes(Id)
);

CREATE TABLE Fraudes (
	Cliente_Id int NOT NULL,
	Valor float NULL,
	DataHora datetime NOT NULL,
	Hora int NULL,
	Minuto int NULL,
	Segundo int NULL,
	Dia date NULL,
	Id int NOT NULL,
	CONSTRAINT pk_id_fraude PRIMARY KEY (Id),
	CONSTRAINT FK_fraudes_clientes FOREIGN KEY (Cliente_Id) REFERENCES Clientes(Id),
	CONSTRAINT FK_fraudes_transacoes FOREIGN KEY (Id) REFERENCES Transacoes(Id)
);

CREATE TABLE Relacoes_fraudes (
	cliente_id int NOT NULL,
	transacao_id int NOT NULL,
	CONSTRAINT FK_rel_clientes FOREIGN KEY (cliente_id) REFERENCES Clientes(Id),
	CONSTRAINT FK_rel_transacoes FOREIGN KEY (transacao_id) REFERENCES Transacoes(Id)
);
