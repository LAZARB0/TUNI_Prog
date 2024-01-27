package fi.tuni.prog3.sudoku;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Sudoku {
    private char[][] board;

    public Sudoku() {
        this.board = new char[9][9];
    }

    public void set(int row, int col, char value) {
        if (!isValidCell(row, col)) {
            System.out.println("Trying to access illegal cell (" + row + ", " + col + ")!");
        } else if (!isValidCharacter(value)) {
            System.out.println("Trying to set illegal character " + value + " to (" + row + ", " + col + ")!");
        } else {
            this.board[row][col] = value;
        }
    }

    public void print() {
        for (int i = 0; i < 9; i++) {
            if (i % 3 == 0 && i >= 0) {
                System.out.println("#####################################");
            } else {
                System.out.println("#---+---+---#---+---+---#---+---+---#");
            }
            for (int j = 0; j < 9; j++) {
                if (j % 3 == 0 && j >= 0) {
                    System.out.print("# ");
                }
                if (j != 0 && j != 3 && j != 6 && j != 9) {
                    System.out.print("| ");
                }
                char value = board[i][j];
                System.out.print(value != 0 ? value : " ");
                System.out.print(" ");
                if (j == 8) {
                    System.out.print("#");
                }
            }
            System.out.println();
        }
        System.out.println("#####################################");
    }

    public boolean check() {
        return checkRows() && checkColumns() && checkBlocks();
    }

    private boolean checkRows() {
        for (int i = 0; i < 9; i++) {
            char Value = checkSet(board[i]);
            if (Value != '\0') {
                System.out.println("Row " + (i) + " has multiple " + Value + "'s!");
                return false;
            }
        }
        return true;
    }

    private boolean checkColumns() {
        for (int j = 0; j < 9; j++) {
            char[] column = new char[9];
            for (int i = 0; i < 9; i++) {
                column[i] = board[i][j];
            }
            char Value = checkSet(column);
                if (Value != '\0') {
                System.out.println("Column " + (j) + " has multiple " + Value + "'s!");
                return false;
            }
        }
        return true;
    }

    private boolean checkBlocks() {
        for (int blockRow = 0; blockRow < 3; blockRow++) {
            for (int blockCol = 0; blockCol < 3; blockCol++) {
                char[] block = new char[9];
                int index = 0;
                for (int i = blockRow * 3; i < blockRow * 3 + 3; i++) {
                    for (int j = blockCol * 3; j < blockCol * 3 + 3; j++) {
                        block[index++] = board[i][j];
                    }
                }
                char Value = checkSet(block);
                if (Value != '\0') {
                    System.out.println("Block at (" + (blockRow * 3) + ", " + (blockCol * 3) + ") has multiple " + Value + "'s!");
                    return false;
                }
            }
        }
        return true;
    }

    private char checkSet(char[] set) {
        Set<Character> seen = new HashSet<>();
        for (char value : set) {
            if (value != 0 && !Character.isWhitespace(value)) {
                if (seen.contains(value)) {
                    return value;
                }
                seen.add(value);
            }
        }
        return '\0';
    }

    private boolean isValidCell(int row, int col) {
        return row >= 0 && row < 9 && col >= 0 && col < 9;
    }

    private boolean isValidCharacter(char value) {
        return value == ' ' || (value >= '0' && value <= '9');
    }
}