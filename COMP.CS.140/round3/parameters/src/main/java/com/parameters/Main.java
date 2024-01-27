package com.parameters;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        Scanner myScanner = new Scanner(System.in);

        ArrayList<String> countries = new ArrayList<>();

        int maxLength = 0;

        while (true) {
            String country = myScanner.nextLine();
            
            if (country.isEmpty()) {
                break;
            }

            countries.add(country);
            maxLength = Math.max(country.length(), maxLength);
        }

        Collections.sort(countries);

        int numberLength = 3;

        if (countries.size() < 10) {
            numberLength = 2;
        } else if (countries.size() > 99) {
            numberLength = 4;
        }

        System.out.println("Parameters:");
        for (int i = 0; i < (maxLength + numberLength + 6); i++) {
            System.out.print("#");
        }
        System.out.println();

        for (int i = 0; i < countries.size(); i++) {
            int number = i + 1;
            String country = countries.get(i);
            
            System.out.printf("#%" + (numberLength) + "d | %-" + (maxLength + 1) + "s#\n", number, country);

            if (i == countries.size() - 1) {
                break;
            }

            System.out.print("#");
            for (int j = 0; j < numberLength + 1; j++) {
                System.out.print("-");
            }
            System.out.print("+");
            for (int k = 0; k < maxLength + 2; k++) {
                System.out.print("-");
            }
            System.out.println("#");
            
            
            
        }
        for (int i = 0; i < (maxLength + numberLength + 6); i++) {
            System.out.print("#");
        }


        myScanner.close();
    }
}