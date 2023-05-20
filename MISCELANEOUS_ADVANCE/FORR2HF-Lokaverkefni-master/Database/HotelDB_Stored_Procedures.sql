USE 0408982209_hotelDB;

-- Debug

DELIMITER //
DROP PROCEDURE IF EXISTS `log_msg` //
CREATE PROCEDURE `log_msg`(
`msg` VARCHAR(255)
)
BEGIN
    INSERT INTO `logtable`SELECT 0, `msg`;
END //
DELIMITER ;


-- Custom procedures

-- Hire an employee

DELIMITER //
DROP PROCEDURE IF EXISTS `EmployeeHire_Bundle` //
CREATE PROCEDURE `EmployeeHire_Bundle` (
  `Param_Zip` varchar(20),
  `Param_CityName` varchar(20),
  `Param_CountryName` varchar(20),
  `Param_StreetName` varchar(20),
  `Param_BuildingNum` varchar(5),
  `Param_ApartNum` varchar(5),
  `Param_HotelID` int,
  `Param_EmpSSN` varchar(20),
  `Param_Title` varchar(20),
  `Param_LName` varchar(20),
  `Param_FName` varchar(20),
  `Param_Email` varchar(60),
  `Param_Phone` varchar(15),
  `Param_User` varchar(20),
  `Param_Pass` varchar(20)
)
BEGIN
  DECLARE Address_NewID int;
  DECLARE Employee_NewID int;
  CALL `AddressAdd` (
    `Param_Zip`,
    `Param_CityName`,
    `Param_CountryName`,
    `Param_StreetName`,
    `Param_BuildingNum`,
    `Param_ApartNum`,
    @Address_NewID
  );

  SET Address_NewID := @Address_NewID;
  CALL `EmployeeAdd` (
    `Param_EmpSSN`,
    Address_NewID,
    `Param_Title`,
    `Param_LName`,
    `Param_FName`,
    `Param_Email`,
    `Param_Phone`,
    `Param_User`,
    `Param_Pass`,
    @Employee_NewID
  );

  SET Employee_NewID := @Employee_NewID;
  CALL `StaffAdd` (
    Employee_NewID,
    `Param_HotelID`
  );
  SELECT Employee_NewID;
END //
DELIMITER ;

-- Register a customer

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerRegister_Bundle` //
CREATE PROCEDURE `CustomerRegister_Bundle` (
  `Param_Zip` varchar(20),
  `Param_CityName` varchar(20),
  `Param_CountryName` varchar(20),
  `Param_StreetName` varchar(20),
  `Param_BuildingNum` varchar(5),
  `Param_ApartNum` varchar(5),
  `Param_CusSSN` varchar(20),
  `Param_LName` varchar(20),
  `Param_FName` varchar(20),
  `Param_Email` varchar(60),
  `Param_Phone` varchar(15),
  `Param_User` varchar(20),
  `Param_Pass` varchar(20)
)
BEGIN
  DECLARE Address_NewID int;
  CALL `AddressAdd` (
    `Param_Zip`,
    `Param_CityName`,
    `Param_CountryName`,
    `Param_StreetName`,
    `Param_BuildingNum`,
    `Param_ApartNum`,
    @Address_NewID
  );

  SET Address_NewID := @Address_NewID;

  CALL `CustomerAdd` (
    `Param_CusSSN`,
    Address_NewID,
    `Param_LName`,
    `Param_FName`,
    `Param_Email`,
    `Param_Phone`,
    `Param_User`,
    `Param_Pass`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;


-- List availalbe rooms by type and hotel

CALL `CheckAvailability` ('2018-05-15','2018-05-18', 3, 1);

DELIMITER //
DROP PROCEDURE IF EXISTS `CheckAvailability` //
CREATE PROCEDURE `CheckAvailability` (
  `New_Start` datetime,
  `New_End` datetime,
  `Param_HotelID` int,
  `Param_TypeID` int
)
BEGIN																													#RIGHT
	SELECT DISTINCT(`Room`.RoomID), `Room`.DoorNum
    FROM `Order_Has_Rooms` RIGHT JOIN `Room` ON `Room`.RoomID = `Order_Has_Rooms`.RoomID
	WHERE `Room`.HotelID = `Param_HotelID`
	AND `Room`.TypeID = `Param_TypeID`
	AND `Room`.RoomID NOT IN (																						#RIGHT
    SELECT `Room`.RoomID FROM `Order_Has_Rooms` RIGHT JOIN `Room` ON `Room`.RoomID = `Order_Has_Rooms`.RoomID
	WHERE `New_Start` < `Order_Has_Rooms`.CheckOutDate
	AND `New_End` > `Order_Has_Rooms`.CheckInDate
	AND `Room`.HotelID = `Param_HotelID`
	AND `Room`.TypeID = `Param_TypeID`
    );



END //
DELIMITER ;


-- Get room bill not including service.

DELIMITER //
DROP PROCEDURE IF EXISTS `TotalRoomBill` //
CREATE PROCEDURE `TotalRoomBill` (
  `Param_OrderID` int
)
BEGIN
  SELECT `Order_Has_Rooms`.CheckInDate, `Order_Has_Rooms`.CheckOutDate, `RoomType`.RoomType, `Room`.DoorNum, `RoomType`.Cost, DATEDIFF(`Order_Has_Rooms`.CheckOutDate, `Order_Has_Rooms`.CheckInDate) AS DaysStayed, (`RoomType`.Cost * DATEDIFF(`Order_Has_Rooms`.CheckOutDate, `Order_Has_Rooms`.CheckInDate)) AS TotalRoomCost, `Hotel`.HotelName, `Order_Has_Rooms`.RoomID, `Order_Has_Rooms`.OrderID
  FROM `Order_Has_Rooms`
  INNER JOIN `Room` ON `Order_Has_Rooms`.RoomID = `Room`.RoomID
  INNER JOIN `RoomType` ON `Room`.TypeID = `RoomType`.TypeID
  INNER JOIN `Hotel` ON `Room`.HotelID = `Hotel`.HotelID
  WHERE `Order_Has_Rooms`.OrderID = `Param_OrderID`;
END //
DELIMITER ;

CALL `TotalRoomBill`(1);

-- Get total service bill

DELIMITER //
DROP PROCEDURE IF EXISTS `TotalServiceBill` //
CREATE PROCEDURE `TotalServiceBill` (
	`Param_OrderID` int
)
BEGIN
	SELECT `Room`.DoorNum, `ServiceOrder`.DateTimeOfService, `Item`.ItemName, `Item`.Cost, `Order_Has_Items`.Qty, (`Item`.Cost * `Order_Has_Items`.Qty) AS TotalItemCost, `Employee`.LName, `Employee`.FName
    FROM `ServiceOrder`
    INNER JOIN `Order_Has_Items` ON `ServiceOrder`.ServiceID = `Order_Has_Items`.ServiceID
    INNER JOIN `Item` ON `Order_Has_Items`.ItemID = `Item`.ItemID
    INNER JOIN `Room` ON `ServiceOrder`.RoomID = `Room`.RoomID
    INNER JOIN `Employee` ON `ServiceOrder`.EmpID = `Employee`.EmpID
    WHERE `ServiceOrder`.OrderID = `Param_OrderID`;
END //
DELIMITER ;

CALL `TotalServiceBill`(1);

-- Get workplaces that an employee works at

DELIMITER //
DROP PROCEDURE IF EXISTS `GetWorkplaces` //
CREATE PROCEDURE `GetWorkplaces` (
	`Param_EmpID` int
)
BEGIN
	SELECT `Hotel`.HotelName FROM `Staff`
    INNER JOIN `Hotel` ON `Staff`.HotelID = `Hotel`.HotelID
    WHERE `Staff`.EmpID = `Param_EmpID`;

END //
DELIMITER ;

-- Make a reservation

/* CALL `ReservationAdd`();*/

-- Add room to reservation

/* CALL `ReservationRoomAdd`();*/

-- Create a service request

/*CALL `ServiceOrderAdd`();*/

-- Add item to cart (services)

/*CALL `ServiceAddItem`(); */

-- Get all orders from a customer

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerOrders` //
CREATE PROCEDURE `CustomerOrders` (
	`Param_CusID` int
)
BEGIN
	SELECT * FROM `Order`
    INNER JOIN `Employee` ON `Order`.EmpID = `Employee`.EmpID
    WHERE `CusID` = `Param_CusID`;
END //
DELIMITER ;
CALL `CustomerOrders` (4);

-- Get all rooms on that order

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomsOnOrder` //
CREATE PROCEDURE `RoomsOnOrder` (
	`Param_OrderID` int
)
BEGIN
	SELECT * FROM `Order_Has_Rooms`
    INNER JOIN `Room` ON `Order_Has_Rooms`.RoomID = `Room`.RoomID
    INNER JOIN `RoomType` ON `Room`.TypeID = `RoomType`.TypeID
    INNER JOIN `Hotel` ON `Room`.HotelID = `Hotel`.HotelID
    WHERE `OrderID` = `Param_OrderID`;
END //
DELIMITER ;

CALL `RoomsOnOrder` (1);

-- Get all services for that room on that order

DELIMITER //
DROP PROCEDURE IF EXISTS `ServicesOnRooms` //
CREATE PROCEDURE `ServicesOnRooms` (
	`Param_OrderID` int,
    `Param_RoomID` int
)
BEGIN
	SELECT * FROM `ServiceOrder`
    INNER JOIN `Employee` ON `ServiceOrder`.EmpID = `Employee`.EmpID
    WHERE `OrderID` = `Param_OrderID`
    AND `RoomID` = `Param_RoomID`;
END //
DELIMITER ;

CALL `ServicesOnRooms` (1, 145);

-- Get details on those services

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceDetails` //
CREATE PROCEDURE `ServiceDetails` (
	`Param_ServiceID` int
)
BEGIN
	SELECT * FROM `Order_Has_Items`
    INNER JOIN `Item` ON `Order_Has_Items`.ItemID = `Item`.ItemID
    WHERE `ServiceID` = `Param_ServiceID`;
END //
DELIMITER ;

CALL CustomerList();
CALL `ServiceDetails`(1);
SELECT * FROM Customer;

-- What did those service details contain

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceItemDetails` //
CREATE PROCEDURE `ServiceItemDetails` (
	`Param_OrderItemID` int
)
BEGIN
	SELECT * FROM `Item`
    WHERE `ItemID` = `Param_OrderItemID`;
END //
DELIMITER ;

CALL `ServiceItemDetails` (9);


-- List new service orders within the last 24h

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceListOrdersByHotel` //
CREATE PROCEDURE `ServiceListOrdersByHotel` (
	`Param_HotelID` int
)
BEGIN
    SELECT * FROM `ServiceOrder`
    INNER JOIN `Room` ON `ServiceOrder`.RoomID = `Room`.RoomID
    WHERE `Room`.HotelID = `Param_HotelID`
    AND `ServiceOrder`.DateTimeOfService > DATE_SUB(NOW(), INTERVAL 12 HOUR);
END //
DELIMITER ;

-- CALL `ServiceListOrdersByHotel`(3);


-- Get a list of rooms that an order has


-- List hotels and their address

DELIMITER //
DROP PROCEDURE IF EXISTS `HotelAbout` //
CREATE PROCEDURE `HotelAbout` ()
BEGIN
	SELECT * FROM `Hotel`
    INNER JOIN `Address` ON `Hotel`.AddressID = `Address`.AddressID;
END //
DELIMITER ;



-- Standard procedures

-- Employee

DELIMITER //
DROP PROCEDURE IF EXISTS `EmployeeAdd` //
CREATE PROCEDURE `EmployeeAdd` (
  `Param_EmpSSN` varchar(20),
  `Param_AddressID` int,
  `Param_Title` varchar(20),
  `Param_LName` varchar(20),
  `Param_FName` varchar(20),
  `Param_Email` varchar(60),
  `Param_Phone` varchar(15),
  `Param_User` varchar(20),
  `Param_Pass` varchar(20),
  OUT `Employee_NewID` int
)
BEGIN
  INSERT INTO `Employee` (
    `EmpSSN`,
    `AddressID`,
    `Title`,
    `LName`,
    `FName`,
    `Email`,
    `Phone`,
    `User`,
    `Pass`
  )
  VALUES (
    `Param_EmpSSN`,
    `Param_AddressID`,
    `Param_Title`,
    `Param_LName`,
    `Param_FName`,
    `Param_Email`,
    `Param_Phone`,
    `Param_User`,
    `Param_Pass`
  );
  SELECT LAST_INSERT_ID() INTO `Employee_NewID`;

END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `EmployeeList` //
CREATE PROCEDURE  `EmployeeList` ()
BEGIN
  SELECT * FROM `Employee`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `EmployeeInfo` //
CREATE PROCEDURE `EmployeeInfo` (
  `Param_EmpID` int
)
BEGIN
  SELECT * FROM `Employee`
  WHERE `EmpID` = `Param_EmpID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `EmployeeUpdate` //
CREATE PROCEDURE `EmployeeUpdate` (
  `Param_EmpID` int,
  `Param_EmpSSN` varchar(20),
  `Param_AddressID` int,
  `Param_Title` varchar(20),
  `Param_LName` varchar(20),
  `Param_FName` varchar(20),
  `Param_Email` varchar(60),
  `Param_Phone` varchar(15),
  `Param_User` varchar(20),
  `Param_Pass` varchar(20)
)
BEGIN
  UPDATE `Employee`
  SET
  `EmpSSN` = `Param_EmpSSN`,
  `AddressID` = `Param_AddressID`,
  `Title` = `Param_Title`,
  `LName` = `Param_LName`,
  `FName` = `Param_FName`,
  `Email` = `Param_Email`,
  `Phone` = `Param_Phone`,
  `User` = `Param_User`,
  `Pass` = `Param_Pass`
  WHERE `EmpID` = `Param_EmpID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `EmployeeDelete` //
CREATE PROCEDURE `EmployeeDelete` (
  `Param_EmpID` int
)
BEGIN
  DELETE FROM `Employee`
  WHERE `EmpID` = `Param_EmpID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Address

DELIMITER //
DROP PROCEDURE IF EXISTS `AddressAdd` //
CREATE PROCEDURE `AddressAdd` (
  `Param_Zip` varchar(20),
  `Param_CityName` varchar(20),
  `Param_CountryName` varchar(20),
  `Param_StreetName` varchar(20),
  `Param_BuildingNum` varchar(5),
  `Param_ApartNum` varchar(5),
  OUT `Address_NewID` int
)
BEGIN
  INSERT INTO `Address` (
    `Zip`,
    `CityName`,
    `CountryName`,
    `StreetName`,
    `BuildingNum`,
    `ApartNum`
  )
  VALUES (
    `Param_Zip`,
    `Param_CityName`,
    `Param_CountryName`,
    `Param_StreetName`,
    `Param_BuildingNum`,
    `Param_ApartNum`
  );
  SELECT LAST_INSERT_ID() INTO `Address_NewID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `AddressList` //
CREATE PROCEDURE `AddressList` ()
BEGIN
  SELECT * FROM `Address`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `AddressInfo` //
CREATE PROCEDURE `AddressInfo` (
  `Param_AddressID` int
)
BEGIN
  SELECT * FROM `Address` WHERE `AddressID` = `Param_AddressID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `AddressUpdate` //
CREATE PROCEDURE `AddressUpdate` (
  `Param_AddressID` int,
  `Param_Zip` varchar(20),
  `Param_CityName` varchar(20),
  `Param_CountryName` varchar(20),
  `Param_StreetName` varchar(20),
  `Param_BuildingNum` varchar(5),
  `Param_ApartNum` varchar(5)
)
BEGIN
  UPDATE `Address`
  SET
  `Zip` = `Param_Zip`,
  `CityName` = `Param_CityName`,
  `CountryName` = `Param_CountryName`,
  `StreetName` = `Param_StreetName`,
  `BuildingNum` = `Param_BuildingNum`,
  `ApartNum` = `Param_ApartNum`
  WHERE `AddressID` = `Param_AddressID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `AddressDelete` //
CREATE PROCEDURE `AddressDelete` (
  `Param_AddressID` int
)
BEGIN
  DELETE FROM `Address`
  WHERE `AddressID` = `Param_AddressID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Hotel

DELIMITER //
DROP PROCEDURE IF EXISTS `HotelAdd` //
CREATE PROCEDURE `HotelAdd` (
  `Param_AddressID` int,
  `Param_HotelName` varchar(40)
)
BEGIN
  INSERT INTO `Hotel` (
    `AddressID`,
    `HotelName`
  )
  VALUES (
    `AddressID` = `Param_AddressID`,
    `HotelName` = `Param_HotelName`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `HotelList` //
CREATE PROCEDURE `HotelList` ()
BEGIN
  SELECT * FROM `Hotel`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `HotelInfo` //
CREATE PROCEDURE `HotelInfo` (
  `Param_HotelID` int
)
BEGIN
  SELECT * FROM `Hotel` WHERE `HotelID` = `Param_HotelID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `HotelUpdate` //
CREATE PROCEDURE `HotelUpdate` (
  `Param_HotelID` int,
  `Param_AddressID` int,
  `Param_HotelName` varchar(40)
)
BEGIN
  UPDATE `Hotel`
  SET
  `AddressID` = `Param_AddressID`,
  `HotelName` = `Param_HotelName`
  WHERE `HotelID` = `Param_HotelID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `HotelDelete` //
CREATE PROCEDURE `HotelDelete` (
  `Param_HotelID` int
)
BEGIN
  DELETE FROM `Hotel`
  WHERE `HotelID` = `Param_HotelID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Room

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomAdd` //
CREATE PROCEDURE `RoomAdd` (
  `Param_HotelID` int,
  `Param_TypeID` int,
  `Param_DoorNum` int
)
BEGIN
  INSERT INTO `Room` (
    `HotelID`,
    `TypeID`,
    `DoorNum`
  )
  VALUES (
    `Param_HotelID`,
    `Param_TypeID`,
    `Param_DoorNum`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomList` //
CREATE PROCEDURE `RoomList` ()
BEGIN
  SELECT * FROM `Room`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomInfo` //
CREATE PROCEDURE `RoomInfo` (
  `Param_RoomID` int
)
BEGIN
  SELECT * FROM `Room` WHERE `RoomID` = `Param_RoomID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomUpdate` //
CREATE PROCEDURE `RoomUpdate` (
  `Param_RoomID` int,
  `Param_HotelID` int,
  `Param_TypeID` int,
  `Param_DoorNum` int
)
BEGIN
  UPDATE `Room`
  SET
  `HotelID` = `Param_HotelID`,
  `TypeID` = `Param_TypeID`,
  `DoorNUM` = `Param_DoorNum`
  WHERE `RoomID` = `Param_RoomID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomDelete` //
CREATE PROCEDURE `RoomDelete` (
  `Param_RoomID` int
)
BEGIN
  DELETE FROM `Room`
  WHERE `RoomID` = `Param_RoomID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Customer

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerAdd` //
CREATE PROCEDURE `CustomerAdd` (
  `Param_CusSSN` varchar(20),
  `Param_AddressID` int,
  `Param_LName` varchar(20),
  `Param_FName` varchar(20),
  `Param_Email` varchar(60),
  `Param_Phone` varchar(15),
  `Param_User` varchar(20),
  `Param_Pass` varchar(20)
)
BEGIN
  INSERT INTO `Customer` (
    `CusSSN`,
    `AddressID`,
    `LName`,
    `FName`,
    `Email`,
    `Phone`,
    `User`,
    `Pass`
  )
  VALUES (
    `Param_CusSSN`,
    `Param_AddressID`,
    `Param_LName`,
    `Param_FName`,
    `Param_Email`,
    `Param_Phone`,
    `Param_User`,
    `Param_Pass`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerList` //
CREATE PROCEDURE `CustomerList` ()
BEGIN
  SELECT * FROM `Customer`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerInfo` //
CREATE PROCEDURE `CustomerInfo` (
  `Param_CusID` int
)
BEGIN
  SELECT * FROM `Customer` WHERE `CusID` = `Param_CusID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerUpdate` //
CREATE PROCEDURE `CustomerUpdate` (
  `Param_CusID` int,
  `Param_CusSSN` varchar(20),
  `Param_AddressID` int,
  `Param_LName` varchar(20),
  `Param_FName` varchar(20),
  `Param_Email` varchar(60),
  `Param_Phone` varchar(15),
  `Param_User` varchar(20),
  `Param_Pass` varchar(20)

)
BEGIN
  UPDATE `Customer`
  SET
  `CusSSN` = `Param_CusSSN`,
  `AddressID` = `Param_AddressID`,
  `LName` = `Param_LName`,
  `FName` = `Param_FName`,
  `Email` = `Param_Email`,
  `Phone` = `Param_Phone`,
  `User` = `Param_User`,
  `Pass` = `Param_Pass`
  WHERE `CusID` = `Param_CusID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `CustomerDelete` //
CREATE PROCEDURE `CustomerDelete` (
  `Param_CusID` int
)
BEGIN
  DELETE FROM `Customer`
  WHERE `CusID` = `Param_CusID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Room type

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomTypeAdd` //
CREATE PROCEDURE `RoomTypeAdd` (
  `Param_RoomType` varchar(20),
  `Param_Desc` varchar(200),
  `Param_Cost` int
)
BEGIN
  INSERT INTO `RoomType` (
    `RoomType`,
    `Desc`,
    `Cost`
  )
  VALUES (
    `Param_RoomType`,
    `Param_Desc`,
    `Param_Cost`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomTypeList` //
CREATE PROCEDURE `RoomTypeList` ()
BEGIN
  SELECT * FROM `RoomType`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomTypeInfo` //
CREATE PROCEDURE `RoomTypeInfo` (
  `Param_TypeID` int
)
BEGIN
  SELECT * FROM `RoomType` WHERE `TypeID` = `Param_TypeID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomTypeUpdate` //
CREATE PROCEDURE `RoomTypeUpdate` (
  `Param_TypeID` int,
  `Param_RoomType` varchar(20),
  `Param_Desc` varchar(200),
  `Param_Cost` int
)
BEGIN
  UPDATE `RoomType`
  SET
  `RoomType` = `Param_RoomType`,
  `Desc` = `Param_Desc`,
  `Cost` = `Param_Cost`
  WHERE `TypeID` = `Param_TypeID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `RoomTypeDelete` //
CREATE PROCEDURE `RoomTypeDelete` (
  `Param_TypeID` int
)
BEGIN
  DELETE FROM `RoomType`
  WHERE `TypeID` = `Param_TypeID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Item

DELIMITER //
DROP PROCEDURE IF EXISTS `ItemAdd` //
CREATE PROCEDURE `ItemAdd` (
  `Param_ItemName` varchar(70),
  `Param_ItemDetails` varchar(200),
  `Param_Cost` int
)
BEGIN
  INSERT INTO `Item` (
    `ItemName`,
    `ItemDetails`,
    `Cost`
  )
  VALUES (
    `Param_ItemName`,
    `Param_ItemDetails`,
    `Param_Cost`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ItemList` //
CREATE PROCEDURE `ItemList` ()
BEGIN
  SELECT * FROM `Item`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ItemInfo` //
CREATE PROCEDURE `ItemInfo` (
  `Param_ItemID` int
)
BEGIN
  SELECT * FROM `Item` WHERE `ItemID` = `Param_ItemID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ItemUpdate` //
CREATE PROCEDURE `ItemUpdate` (
  `Param_ItemID` int,
  `Param_ItemName` varchar(70),
  `Param_ItemDetails` varchar(200),
  `Param_Cost` int
)
BEGIN
  UPDATE `Item`
  SET
  `ItemName` = `Param_ItemName`,
  `ItemDetails` = `Param_ItemDetails`,
  `Cost` = `Param_Cost`
  WHERE `ItemID` = `Param_ItemID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ItemDelete` //
CREATE PROCEDURE `ItemDelete` (
  `Param_ItemID` int
)
BEGIN
  DELETE FROM `Item`
  WHERE `ItemID` = `Param_ItemID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Staff

DELIMITER //
DROP PROCEDURE IF EXISTS `StaffAdd` //
CREATE PROCEDURE `StaffAdd` (
  `Param_EmpID` int,
  `Param_HotelID` int
)
BEGIN
  INSERT INTO `Staff` (
    `EmpID`,
    `HotelID`
  )
  VALUES (
    `Param_EmpID`,
    `Param_HotelID`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StaffList` //
CREATE PROCEDURE `StaffList` ()
BEGIN
  SELECT * FROM `Staff`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StaffInfo` //
CREATE PROCEDURE `StaffInfo` (
  `Param_StaffID` int
)
BEGIN
  SELECT * FROM `Staff` WHERE `HotelID` = `Param_HotelID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StaffUpdate` //
CREATE PROCEDURE `StaffUpdate` (
  `Param_StaffID` int,
  `Param_EmpID` int,
  `Param_HotelID` int
)
BEGIN
  UPDATE `Staff`
  SET
  `EmpID` = `Param_EmpID`,
  `HotelID` = `Param_HotelID`
  WHERE `StaffID` = `Param_StaffID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `StaffDelete` //
CREATE PROCEDURE `StaffDelete` (
  `Param_StaffID` int
)
BEGIN
  DELETE FROM `Staff`
  WHERE `StaffID` = `Param_StaffID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- ServiceOrder

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceOrderAdd` //
CREATE PROCEDURE `ServiceOrderAdd` (
  `Param_RoomID` int,
  `Param_OrderID` int,
  `Param_EmpID` int,
  `Param_DateTimeOfService` datetime
)
BEGIN
  INSERT INTO `ServiceOrder` (
    `RoomID`,
    `OrderID`,
    `EmpID`,
    `DateTimeOfService`
  )
  VALUES (
    `Param_RoomID`,
    `Param_OrderID`,
    `Param_EmpID`,
    `Param_DateTimeOfService`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceOrderList` //
CREATE PROCEDURE `ServiceOrderList` ()
BEGIN
  SELECT * FROM `ServiceOrder`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceOrderInfo` //
CREATE PROCEDURE `ServiceOrderInfo` (
  `Param_ServiceID` int
)
BEGIN
  SELECT * FROM `ServiceOrder` WHERE `ServiceID` = `Param_ServiceID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceOrderUpdate` //
CREATE PROCEDURE `ServiceOrderUpdate` (
  `Param_ServiceID` int,
  `Param_RoomID` int,
  `Param_OrderID` int,
  `Param_EmpID` int,
  `Param_DateTimeOfService` datetime
)
BEGIN
  UPDATE `ServiceOrder`
  SET
    `RoomID` = `Param_RoomID`,
    `OrderID` = `Param_OrderID`,
    `EmpID` = `Param_EmpID`,
    `DateTimeOfService` = `Param_DateTimeOfService`
  WHERE `ServiceID` = `Param_ServiceID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceOrderDelete` //
CREATE PROCEDURE  `ServiceOrderDelete` (
  `Param_ServiceID` int
)
BEGIN
  DELETE FROM `ServiceOrder`
  WHERE `ServiceID` = `Param_ServiceID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Order / Reservation

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationAdd` //
CREATE PROCEDURE `ReservationAdd` (
  `Param_EmpID` int,
  `Param_CusID` int,
  `Param_OrderDate` datetime
)
BEGIN
  INSERT INTO `Order` (
    `EmpID`,
    `CusID`,
    `OrderDate`
  )
  VALUES (
    `Param_EmpID`,
    `Param_CusID`,
    `Param_OrderDate`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationList` //
CREATE PROCEDURE `ReservationList` ()
BEGIN
  SELECT * FROM `Order`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationInfo` //
CREATE PROCEDURE `ReservationInfo` (
  `Param_OrderID` int
)
BEGIN
  SELECT * FROM `Order` WHERE `OrderID` = `Param_OrderID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationUpdate` //
CREATE PROCEDURE `ReservationUpdate` (
  `Param_OrderID` int,
  `Param_EmpID` int,
  `Param_CusID` int,
  `Param_OrderDate` datetime
)
BEGIN
  UPDATE `Order`
  SET
  `EmpID` = `Param_EmpID`,
  `CusID` = `Param_CusID`,
  `OrderDate` = `Param_OrderDate`
  WHERE `OrderID` = `Param_OrderID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationDelete` //
CREATE PROCEDURE `ReservationDelete` (
  `Param_OrderID` int
)
BEGIN
  DELETE FROM `Order`
  WHERE `OrderID` = `Param_OrderID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Order_Has_Rooms

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationRoomAdd` //
CREATE PROCEDURE `ReservationRoomAdd` (
  `Param_OrderID` int,
  `Param_RoomID` int,
  `Param_CheckInDate` datetime,
  `Param_CheckOutDate` datetime
)
BEGIN
  INSERT INTO `Order_Has_Rooms` (
    `OrderID`,
    `RoomID`,
    `CheckInDate`,
    `CheckOutDate`
  )
  VALUES (
    `Param_OrderID`,
    `Param_RoomID`,
    `Param_CheckInDate`,
    `Param_CheckOutDate`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationRoomList` //
CREATE PROCEDURE `ReservationRoomList` ()
BEGIN
  SELECT * FROM `Order_Has_Rooms`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationRoomInfo` //
CREATE PROCEDURE `ReservationRoomInfo` (
  `Param_OrderRoomID` int
)
BEGIN
  SELECT * FROM `Order_Has_Rooms` WHERE `OrderRoomID` = `Param_OrderRoomID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationRoomUpdate` //
CREATE PROCEDURE `ReservationRoomUpdate` (
  `Param_OrderRoomID` int,
  `Param_OrderID` int,
  `Param_RoomID` int,
  `Param_CheckInDate` datetime,
  `Param_CheckOutDate` datetime
)
BEGIN
  UPDATE `Order_Has_Rooms`
  SET
  `OrderID` = `Param_OrderID`,
  `RoomID` = `Param_RoomID`,
  `CheckInDate` = `Param_CheckInDate`,
  `CheckOutDate` = `Param_CheckOutDate`
  WHERE `OrderRoomID` = `Param_OrderRoomID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ReservationRoomDelete` //
CREATE PROCEDURE `ReservationRoomDelete` (
  `Param_OrderRoomID` int
)
BEGIN
  DELETE FROM `Order_Has_Rooms`
  WHERE `OrderRoomID` = `Param_OrderRoomID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

-- Order_Has_Items

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceAddItem` //
CREATE PROCEDURE `ServiceAddItem` (
  `Param_ServiceID` int,
  `Param_ItemID` int,
  `Param_Qty` int
)
BEGIN
  INSERT INTO `Order_Has_Items` (
    `ServiceID`,
    `ItemID`,
    `Qty`
  )
  VALUES (
    `Param_ServiceID`,
    `Param_ItemID`,
    `Param_Qty`
  );
  SELECT LAST_INSERT_ID();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceListItems` //
CREATE PROCEDURE `ServiceListItems` ()
BEGIN
  SELECT * FROM `Order_Has_Items`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceInfoItems` //
CREATE PROCEDURE `ServiceInfoItems` (
  `Param_OrderItemID` int
)
BEGIN
  SELECT * FROM `Order_Has_Items` WHERE `OrderItemID` = `Param_OrderItemID`;
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceUpdateItem` //
CREATE PROCEDURE `ServiceUpdateItem` (
  `Param_OrderItemID` int,
  `Param_ServiceID` int,
  `Param_ItemID` int,
  `Param_Qty` int
)
BEGIN
  UPDATE `Order_Has_Items`
  SET
  `ServiceID` = `Param_ServiceID`,
  `ItemID` = `Param_ItemID`,
  `Qty` = `Param_Qty`
  WHERE `OrderItemID` = `Param_OrderItemID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;

DELIMITER //
DROP PROCEDURE IF EXISTS `ServiceDeleteItem` //
CREATE PROCEDURE `ServiceDeleteItem` (
  `Param_OrderItemID` int
)
BEGIN
  DELETE FROM `Order_Has_Items`
  WHERE `OrderItemID` = `Param_OrderID`;
  SELECT ROW_COUNT();
END //
DELIMITER ;
