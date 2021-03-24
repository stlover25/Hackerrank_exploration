/*


Fill in the blanks so that the trigger item_delete inserts name from item table to the item_archive table, after a row from the table item is deleted.
source : https://www.testdome.com/questions/mysql/item-archive/23268?visibility=3&skillId=312

*/



CREATE TABLE item (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  quantity INT NOT NULL
);

CREATE TABLE item_archive (
  archive_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50) NOT NULL
);

DELIMITER $$
CREATE TRIGGER item_delete AFTER DELETE ON item 
FOR EACH ROW
BEGIN
  INSERT INTO item_archive(name) VALUES (old.name);
END;
$$
DELIMITER ;
