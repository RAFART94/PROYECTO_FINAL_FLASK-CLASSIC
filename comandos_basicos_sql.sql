/* seleccionar todos los registros de una tabla*/
/*SELECT * FROM movements*/
/*seleccionar algunos campos de una tabla*/
/*SELECT Concept, Quantity FROM movements*/
/*para insertar nuevos registros en la tabla movements*/
/*INSERT INTO movements (Date, Concept, Quantity) VALUES ('2024-01-20', 'comida', -500);*/
/*SELECT con WHERE(filtro por campos)*/
/*SELECT date, Concept, Quantity FROM movements WHERE Quantity>0;*/
/*actualizar cualquier campo de la tabala, importante siempre referenciar por WHERE*/
/*UPDATE movements SET Concept = 'Desayuno', Quantity = -50 WHERE id=2;*/
/*borramos un registro especifico de la tabla movements*/
/*DELETE FROM movements WHERE id=3;*/
INSERT INTO movements (Date, Concept, Quantity) VALUES ('2024-01-15', 'Compra del Mercadona', -200);
SELECT * FROM movements