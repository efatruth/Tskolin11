# Viðauki
## Dagbækur
Hér skal vera dagbók frá öllum í verkefninu
## Kóði
Hér setjum við kóða:
Munið að taka þennan kóða út og ykkar inn. :-)
```

*/ 
Hér er dæmi um multitask með task
*/
vex::brain Brain;

int myTask() {
    int count = 0;
  
    while(1) {
      Brain.Screen.printAt( 10, 60, "I am another task %d", count++ );
      
      // don't hog the cpu :)
      vex::task::sleep( 25 );
    }
  
    return(0);
}

int main() {
    int count = 0;

    // this is similar to startTask
    vex::task t1( myTask );
    vex::task t2( myTask );
  
    while(1) {
      Brain.Screen.printAt( 10, 30, "Hello from main %d", count++ );

      // Allow other tasks to run
      vex::task::sleep(10);
    }
}

/*
Hér er dæmi um þráðavinnslu
*/
vex::brain Brain;

int myThread() {
    int count = 0;
  
    while(1) {
      Brain.Screen.printAt( 10, 60, "I am the other task %d", count++ );
      
      // don't hog the cpu :)
      vex::this_thread::sleep_for( 25 );
    }
  
    return(0);
}

int main() {
    int count = 0;

    // this is similar to startTask
    vex::thread t( myThread );
  
    while(1) {
      Brain.Screen.printAt( 10, 30, "Hello from main %d", count++ );

      // Allow other tasks to run
      vex::this_thread::sleep_for(10);
    }
}
```
