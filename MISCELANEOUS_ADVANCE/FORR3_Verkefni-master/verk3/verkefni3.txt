## 1. Hvað er template literals (ES2015)? Komdu með kóðasýnidæmi ásamt skýringum.
  - Dæmi um template literals er að hafa eitt string í tvær línur (multi-line strings).
    
    var myMultiString ("Þessi strengur eru 
      í tvær línur!";

## 2. Hver er munurinn á for, forEach, for-in og for-of lykkjum? Útskýrðu. 
  - ### forEach er bara virkar bara á Array object.
    // Dæmi fyrir forEach
    var myArray = [10, 20, 30, 40];
    
    var myFunction = funtion(item) {
      console.log(item);
    };
    
    myArray.forEach(myFunction); // Þetta skilar út 10, 20, 30 og 40
    //
    
    
    ### for-in virkar á öllum objectum.
    // Dæmi fyrir for-in
    var namePerson = "";
    var person = {firstName: "Robert", lastName: "Downey"};
    
    for (var x in person){
      namePerson = namePerson + x; // namePerson = "RobertDowney"
    };
    
    
    ### Í for loop ertu með þrjá parta. Fyrst þarftu að initalize-a svo að gefa condtion og að lokun final-expression.
    Þetta lítur svona út:
    for ([initialization]; [condition]; [final-expression]){
      statement;
    };
    // Dæmi fyrir for loop
    for (var = 0; i <= 10; i++){
      console.log(i); // Þetta skilar frá sér tölur frá 0 upp í 10
    };
    //
    
    
    ### For of er ekki það sama og for in. Ef við notum for of fáum við value-in inn í Array-inu en þegar við notum for in fáum við         index-inn
    // Dæmi
    var myArray = [3, 5, 7];
    
    for (var i in myArray){
      console.log(i); // Þetta skilar 0, 1, 2
    }
    
    for (var i of myArray){
      console.log(i); // Þetta skilar 3, 5, 7
    }
    //
    
## 3. Fylkjaaðferðir. Svarðu spurningum í lið 17 (e. quiz) í Arrays á Udacity https://classroom.udacity.com/courses/ud803 
  - 1 af 4 = reverse()
  
    2 af 4 = sort()
    
    3 af 4 = shift() eða splice()
    
    4 af 4 = join()

## 4. forEach() Leystu lið 20 í Arrays á Udacity https://classroom.udacity.com/courses/ud803
  - var test = [12, 929, 11, 3, 199, 1000, 7, 1, 24, 37, 4, 19, 300, 3775, 299, 36, 209, 148, 169, 299, 6, 109, 20, 58, 139, 59, 3, 1,   139];


    test.forEach(function(num,index,array){
        if (num % 3 === 0){
            num += 100
            array[index] = num;
        }
        console.log(num);
    });

## 5. Hvað gerir .map() fylkjaaðferðin? Leystu lið 22 í Arrays á Udacity https://classroom.udacity.com/courses/ud803
  - var bills = [50.23, 19.12, 34.01, 100.11, 12.15, 9.90, 29.11, 12.99, 10.00, 99.22, 102.20, 100.10, 6.77, 2.22];

    var totals= bills.map(function(number) {
        number *= 1.15;
        return Number((number.toFixed(2)));
    });

    console.log(totals);

## 6. Fylki í fylki (2d fylki) Leystu lið 25 í Arrays á Udacity https://classroom.udacity.com/courses/ud803
  - var numbers = [
        [243, 12, 23, 12, 45, 45, 78, 66, 223, 3],
        [34, 2, 1, 553, 23, 4, 66, 23, 4, 55],
        [67, 56, 45, 553, 44, 55, 5, 428, 452, 3],
        [12, 31, 55, 445, 79, 44, 674, 224, 4, 21],
        [4, 2, 3, 52, 13, 51, 44, 1, 67, 5],
        [5, 65, 4, 5, 5, 6, 5, 43, 23, 4424],
        [74, 532, 6, 7, 35, 17, 89, 43, 43, 66],
        [53, 6, 89, 10, 23, 52, 111, 44, 109, 80],
        [67, 6, 53, 537, 2, 168, 16, 2, 1, 8],
        [76, 7, 9, 6, 3, 73, 77, 100, 56, 100]
    ];

    for (var r = 0; r < numbers.length; r++){
        for (var c = 0; c < numbers[r].length; c++){
            if (numbers[r][c] % 2 === 0){
                numbers[r][c] = "even";
            }
            else{
                numbers[r][c] = "odd";
            }
        }
    }
    console.log(numbers);

## 7. Leystu lið 8 í Objects á Udacity https://classroom.udacity.com/courses/ud803
  - var breakfast = {
      name:"The Lumberjack", 
      price:"$9.95", 
      ingredients:["eggs", "sausage", "toast", "hashbrowns", "pancakes"]
    };

## 8. Leystu lið 9 í Objects á Udacity https://classroom.udacity.com/courses/ud803
  - var savingsAccount = {
    balance: 1000,
    interestRatePercent: 1,
    deposit: function addMoney(amount) {
        if (amount > 0) {
            savingsAccount.balance += amount;
        }
    },
    withdraw: function removeMoney(amount) {
        var verifyBalance = savingsAccount.balance - amount;
        if (amount > 0 && verifyBalance >= 0) {
            savingsAccount.balance -= amount;
        }
    },
    printAccountSummary: function message(){
          return ("Welcome!\nYour balance is currently $"+savingsAccount.balance+" and your interest rate is "+savingsAccount.interestRatePercent+"%.");
      }
  };

console.log(savingsAccount.printAccountSummary());

