import java.util.Scanner;

import Java.util.Scanner;
public class Hello {
    public static void main(String[] arges) {
        int a=111;
        System.out.println(a);
        int[] b;
        b=new int[] {11,22,33,44,55};
        System.out.println(b[2]);
        System.out.println(b.length);
        Scanner c= new Scanner(System.in);
        System.out.println("please enter a string and a number:");
        String name=c.nextLine();
        int num=c.nextInt();
        System.out.printf("Hi!, %s,number is %d",name,num);

    }
}