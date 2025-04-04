

CREATE TABLE operadoras_plano_de_saude (
    registro TEXT,
    REG_ANS TEXT,
    CD_CONTA_CONTABIL TEXT,
    DESCRICAO TEXT,
    VL_SALDO_INICIAL TEXT,
    VL_SALDO_FINAL TEXT
);

CREATE TABLE relatorio_cadop (
    Registro_ANS TEXT,
    CNPJ TEXT,
    Razao_Social TEXT,
    Nome_Fantasia TEXT,
    Modalidade TEXT,
    Logradouro TEXT,
    Numero TEXT,
    Complemento TEXT,
    Bairro TEXT,
    Cidade TEXT,
    UF TEXT,
    CEP TEXT,
    DDD TEXT,
    Telefone TEXT,
    Fax TEXT,
    Endereco_eletronico TEXT,
    Representante TEXT,
    Cargo_Representante TEXT,
    Regiao_de_Comercializacao TEXT,
    Data_Registro_ANS TEXT
);

 \COPY relatorio_cadop FROM 'C:\Users\Usuario\Desktop\Importante\projetos\Intuitive Care\data/Relatorio_cadop.csv' WITH (FORMAT CSV, HEADER, DELIMITER ';', ENCODING 'UTF8');