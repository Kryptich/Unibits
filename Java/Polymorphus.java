// Example of static polymorphism in Java. Course demonstration.

public class Polymorphus
{
  public static void numberMachine(double a)
  {
    System.out.println("1 INT Input: You gave us \""
                        + a + "\". But we won't do anything with it.");
  }
  public static void numberMachine(double a, double b)
  {
    System.out.println("2 INT Inputs: MATH TIME!! "
                        + a + " + " + b + " = " + (a+b));
  }
  public static void numberMachine(double a, double b, double c)
  {
    System.out.println("3 INT Inputs: INTENSE MATH --> "
                        + "(" + a + " ÷ " + b + ")"
                        + " × " + c + " = " + ((a/b) * c));
  }
  public static void main(String[] args)
  {
    numberMachine(37);
    numberMachine(1,8);
    numberMachine(4,3,40);
  }
}
