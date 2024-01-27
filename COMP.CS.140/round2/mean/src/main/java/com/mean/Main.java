package com.mean;

import java.util.Scanner;

public class Main 
{
    public static void main( String[] args )
    {
        Scanner myScanner = new Scanner(System.in);

        System.out.println( "Enter numbers:" );
        String line = myScanner.nextLine();

        String[] numbers = line.split(" ");

        double sum = 0;
        int count = 0;
        for (String s : numbers) {
            double d = Double.parseDouble(s);
            sum += d;
            count++;
        }
        double mean = 0;

        mean = sum / count;

        System.out.println( "Mean: " + mean);

        myScanner.close();
    }
}