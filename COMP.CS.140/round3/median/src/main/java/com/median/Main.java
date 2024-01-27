package com.median;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);

        System.out.println("Enter numbers:");
        String line = myScanner.nextLine();

        String[] numbersString = line.split(" ");
        double[] numbers = new double[numbersString.length];

        for (int i = 0; i < numbersString.length; i++) {
            numbers[i] = Double.parseDouble(numbersString[i]);
        }

        Arrays.sort(numbers);

        double median;
        if (numbers.length % 2 == 0) {
            median = (numbers[numbers.length / 2 - 1] + numbers[numbers.length / 2]) / 2.0;
        } else {
            median = numbers[numbers.length / 2];
        }

        System.out.println("Median: " + median);

        myScanner.close();
    }
}