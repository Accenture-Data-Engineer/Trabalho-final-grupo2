CREATE TABLE clientes (
    Id INT PRIMARY KEY,
    Nome VARCHAR(255),
    Email VARCHAR(255),
    Data_cadastro TIMESTAMP,
    Telefone VARCHAR(20),
    DDD INT,
    Country_code INT
);

CREATE TABLE transacoes (
    Id INT PRIMARY KEY,
    Cliente_Id INT,
    Valor FLOAT,
    DataHora TIMESTAMP,
    Hora INT,
    Minuto INT,
    Segundo INT,
    Dia DATE,
    FOREIGN KEY (Cliente_Id) REFERENCES clientes(Id)
);

 CREATE TABLE fraudes (
    Cliente_Id int FOREIGN KEY REFERENCES clientes(Id),
    Id_transacao int FOREIGN KEY REFERENCES transacoes(Id)
);
