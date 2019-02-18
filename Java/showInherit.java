class Car{
    // Create some 'Car' fields/attributes
    String name;
    int year;
    // Constructor:
    Car(String name, int year){
        this.name = name;
        this.year = year;
    }
    // Method to display general info about Object:
    public void getGeneral(){
        System.out.print("I am a car (a " + year + " " + name + ").");
    }
}

class Electric extends Car{
    // Append new Fuel Type attribute:
    String fueledBy = "electricity";
    // Constructor (THIS IS NOT INHERITABLE FROM SUPER, but can be 'called' like so:)
    Electric(String x, int y){
        super(x,y);
    }
    // Method to display extra 'Electric' field information (Fuel Type)
    public void getSpecific(){
        System.out.print(" It has been specified that I run on " + fueledBy + ".");
    }
}

class showInherit{
    public static void main(String[] args){
        new Car("Ford",1994).getGeneral();               // run info method on Car object
        System.out.print('\n');                     // separate our methods with new line
        Electric now4Tesla = new Electric("Tesla",2016); // define new Electric Car
        now4Tesla.getGeneral();                          // run getGeneral (INHERITED!!)
        now4Tesla.getSpecific();                         // run custom getSpecific method
    }
}
