

CREATE TABLE operadoras_plano_de_saude (
    registro TEXT,
    REG_ANS TEXT,
    CD_CONTA_CONTABIL TEXT,
    DESCRICAO TEXT,
    VL_SALDO_INICIAL TEXT,
    VL_SALDO_FINAL TEXT
);

UPDATE operadoras_plano_de_saude
SET registro = TO_CHAR(TO_DATE(registro, 'DD/MM/YYYY'), 'YYYY-MM-DD')
WHERE registro ~ '^\d{2}/\d{2}/\d{4}$';

ALTER TABLE operadoras_plano_de_saude
ALTER COLUMN registro TYPE DATE
USING TO_DATE(registro, 'YYYY-MM-DD');

SELECT reg_ans
FROM operadoras_plano_de_saude
WHERE trim(reg_ans) = ''
   OR reg_ans IS NULL
   OR NOT reg_ans ~ '^\d+(\.\d+)?$';

DELETE FROM operadoras_plano_de_saude
WHERE trim(reg_ans) = ''
   OR reg_ans IS NULL
   OR NOT reg_ans ~ '^\d+(\.\d+)?$';

ALTER TABLE operadoras_plano_de_saude
ALTER COLUMN reg_ans TYPE NUMERIC USING reg_ans::numeric;

SELECT cd_conta_contabil
FROM operadoras_plano_de_saude
WHERE cd_conta_contabil !~ '^\d+$';

UPDATE operadoras_plano_de_saude
SET cd_conta_contabil = NULL
WHERE cd_conta_contabil !~ '^\d+$';

ALTER TABLE operadoras_plano_de_saude
ALTER COLUMN cd_conta_contabil TYPE INTEGER USING cd_conta_contabil::integer;

DELETE FROM "operadoras_plano_de_saude"
WHERE "vl_saldo_inicial" !~ '^\s*-?\d+(\.\d+)?$';

ALTER TABLE "operadoras_plano_de_saude"
ALTER COLUMN "vl_saldo_inicial" TYPE NUMERIC
USING "vl_saldo_inicial"::NUMERIC;

DELETE FROM "operadoras_plano_de_saude"
WHERE "vl_saldo_final" !~ '^\s*-?\d+(\.\d+)?$';

ALTER TABLE "operadoras_plano_de_saude"
ALTER COLUMN "vl_saldo_final" TYPE NUMERIC
USING "vl_saldo_final"::NUMERIC;

SELECT descricao, COUNT(*) AS ocorrencias
FROM operadoras_plano_de_saude
GROUP BY descricao
HAVING COUNT(*) > 1;

UPDATE operadoras_plano_de_saude
SET descricao = 'cobertura assistencial com preço pré-estabelecido'
WHERE descricao = 'cobertura assistencial com preço preestabelecido';

UPDATE operadoras_plano_de_saude
SET descricao = regexp_replace(descricao, '^\(-\)\s*', '')
WHERE descricao LIKE '(-)%';

UPDATE operadoras_plano_de_saude
SET descricao = lower(descricao);

UPDATE operadoras_plano_de_saude
SET DESCRICAO = REPLACE(DESCRICAO, 'preestabelecido', 'pré-estabelecido')
WHERE DESCRICAO ILIKE '%preestabelecido%';



CREATE TABLE operadoras_saude AS
SELECT 
    registro,
    REG_ANS,
    DESCRICAO,
    VL_SALDO_INICIAL,
    VL_SALDO_FINAL
FROM 
    operadoras_plano_de_saude
    WHERE 
  DESCRICAO ILIKE '%cobertura assistencial%'
  AND (
    DESCRICAO ILIKE '%médico%' 
    OR DESCRICAO ILIKE '%hospitalar%' 
    OR DESCRICAO ILIKE '%odontológica%'
  );

SELECT 
    REG_ANS,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS total_despesa
FROM 
    operadoras_plano_de_saude
WHERE 
    registro BETWEEN '2024-09-01' AND '2024-12-31'
GROUP BY 
    REG_ANS
ORDER BY 
    total_despesa ASC
LIMIT 10;


SELECT 
    REG_ANS,
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS total_despesa
FROM 
    operadoras_plano_de_saude
WHERE 
    registro BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY 
    REG_ANS
ORDER BY 
    total_despesa ASC
LIMIT 10;


