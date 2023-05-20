DELIMITER $$

DROP PROCEDURE IF EXISTS spArrayTester $$

/*
	Ef viÃ° Ã¦tlum aÃ° nota "Array" sem fÃ¦ribreytu Ã­ MySQL Ã¾Ã¡ verÃ°um viÃ° aÃ° feika Ã¾aÃ°.
	ViÃ° skilgreinum sem sagt streng meÃ° delimiter sem viÃ° notum til aÃ° aÃ°greina "elementin".
	DÃ¦mi: 'GSF2A3U,GSF2B3U,GSF3A3U,GSF3B3U'. Komman er hÃ©rna Ã¾essi delimiter Ã¡ gÃ¶gnin.
	Ãžessi SP vinnur Ã¾annig aÃ° hann klÃ­pur framan af strengnum(workingArray) og setur Ã­ breytuna currentString
	Ef sÃ¡ sstrengur inniheldur eitthvaÃ° Ã¾Ã¡ er Ã¾aÃ° sett Ã­ temporary tÃ¶fluna.
*/
CREATE PROCEDURE spArrayTester( incoming_array TEXT)
BEGIN
    DECLARE currentPosition INT; 
    DECLARE workingArray TEXT; 
    DECLARE currentString VARCHAR(255);
	
    CREATE TEMPORARY TABLE tmpTestTable( id INT );

    SET workingArray = incoming_array; 
    SET currentPosition = 1;

    WHILE CHAR_LENGTH(workingArray) > 0 AND currentPosition > 0 DO 
        SET currentPosition = INSTR(workingArray, ','); 
        IF currentPosition = 0 THEN 
            SET currentString = workingArray; 
        ELSE 
            SET currentString = LEFT(workingArray, currentPosition - 1); 
        END IF; 

        IF TRIM(currentString) != '' THEN 
            INSERT INTO tmp_test(id)VALUES(currentString);                 
        END IF; 

        SET workingArray = SUBSTRING(workingArray, currentPosition + 1); 
    END WHILE;
END $$

DELIMITER ;

call spArrayTester('GSF2A3U,GSF2B3U,GSF3A3U,GSF3B3U');

select * from tmpTestTable;