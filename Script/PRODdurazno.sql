-- Juandi
-- Mantis 244335

DELETE FROM `prueba`.`actividades` WHERE (`id_actividad` = '9');
DELETE FROM `prueba`.`actividades` WHERE (`id_actividad` = '10');

INSERT INTO actividades (id_actividad, desc_actividad) VALUES (9, 'GoldGYM');
