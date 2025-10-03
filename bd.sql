CREATE TABLE BASE_DADOS
(
    ID_LINHA INT PRIMARY KEY AUTOINCREMENT;
    Estado VARCHAR(2) NOT NULL;
    Cidade VARCHAR(50) NOT NULL;
    Marca VARCHAR(50) NOT NULL;
    Data_Base DATA NOT NULL;
    Metrica VARCHAR(50) NOT NULL;
    Valor numeric NOT NULL

);


/* Ticket Médio */

SELECT SUM(*) Valor AS TICKET_MEDIO
FROM BASE_DADOS
WHERE Metrica = 'Ticket Medio';

/* Total de pedidos */

SELECT SUM(*) Valor AS PEDIDOS
FROM BASE_DADOS
WHERE Metrica = 'Pedidos';

/* Ticket médio por grupo  */ 

SELECT SUM(*) Valor AS TICKET_MEDIO_GRUPO
FROM BASE_DADOS
GROUP BY Marca;

/* Ticket Médio por estado */

SELECT SUM(*) Valor AS TICKET_MEDIO_ESTADO
FROM BASE_DADOS
GROUP BY Estado;


/* Percentual de cancelados  */
SELECT AVG(Valor) AS PERCENTUAL_CANCELADOS
FROM BASE_DADOS
WHERE Metrica = '% Cancelados';

/* Crescimento faturamento por mês*/
SELECT 
    FORMAT(Data, 'MM/yyyy') AS MES_ANO,
    SUM(Valor) AS GMV_Total
FROM BASE_DADOS
WHERE Metrica = 'GMV'
GROUP BY FORMAT(Data, 'MM/yyyy')
ORDER BY MIN(Data);
