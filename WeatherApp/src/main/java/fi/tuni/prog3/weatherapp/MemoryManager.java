/**
 * 12.4.2024 - Class created. readFromFile, writeToFile, printMemory and getters
 *             implemented - Jukka
 */
package fi.tuni.prog3.weatherapp;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
//import java.util.Stack;

/**
 * Class for reading data from a json file and writing to json style data to
 * a file. When reading from a file, saves important data to objects.
 * 
 * 12.4.2024 Class created. readFromFile, writeToFile, printMemory and 2 
 * getters implemented
 * Jukka Ruhanen
 * 
 * 19.4.2024 setLastSearch implemented, now writes the last searched city to the
 * given file
 * 
 * Jukka Ruhanen
 */
public class MemoryManager implements iReadAndWriteToFile{

    private ArrayList<String> testList = new ArrayList<>(Arrays.asList(
            //"testLocation1", "testLocation2", "testLocation3"
            //"Helsinki","Tampere","Bangkok"
    ));
    
    /**
     * The last search from previous time the program was used
     */
    private String lastSearch = "lastSearchExample";
    /**
     * ArrayList containing all of the favorited cities from last usage of 
     * program
     */
    private ArrayList<String> favorites;
    // private Stack<String> history;
    
    /**
     * 12.4.2024 Reads data from a json style file and saves them
     * @param fileName name of the file that contains the data
     * @return true if reading and saving was successful, otherwise false
     * @throws Exception if reading/saving was not successful
     * Jukka Ruhanen
     */
    @Override
    public boolean readFromFile(String fileName) throws Exception {
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        try (FileReader fr = new FileReader(fileName)) {
            HashMap<String, Object> jsonData = gson.fromJson(fr, HashMap.class);
            fr.close();

            this.lastSearch = (String) jsonData.get("lastSearch");
            this.favorites = (ArrayList<String>) jsonData.get("favorites");

            return true;
        }
        catch (Exception e){
            e.printStackTrace();
            return false;
        }

    }
    
    /**
     * 19.4.2024 Writes last searched city and favorites to a file in json style
     * @param fileName name of the file the data is supposed to be written in
     * @return true if writing was successful, otherwise false
     * @throws Exception if writing was not successful
     * Jukka Ruhanen
     */
    @Override
    public boolean writeToFile(String fileName) throws Exception {
        
        Gson gson = new GsonBuilder().setPrettyPrinting().create();
        HashMap<String, Object> jsonData = new HashMap<>();
        
        jsonData.put("lastSearch", lastSearch);
        
        // testList -> favorites, when adding favorites is possible
        jsonData.put("favorites", testList);
        
        // TO-DO: Add history writing

        try (FileWriter fw = new FileWriter(fileName)) {
            gson.toJson(jsonData, fw);
            fw.close();
            return true;
        } catch (Exception e) {
            e.printStackTrace();
            return false;
        }
    }
    
    /**
     * 12.4.2024 Prints what was saved in the memory from last time
     * Jukka Ruhanen
     */
    public void printMemory(){
        System.out.println("Last search was:" + lastSearch);
        System.out.println("Favorites are:");
        for (String favorite : favorites) {
            System.out.println(favorite);
        }
    }
    
    /**
     * 12.4.2024 Returns the favorited cities
     * @return an arraylist containing String of all of the favorited cities
     * Jukka Ruhanen
     */
    public ArrayList<String> getFavorites(){
        return favorites;
    }
    
    /**
     * Returns the last searched city from previous use
     * @return last searched city
     * 12.4.2024 Jukka Ruhanen
     */
    public String getLastSearch(){
        return lastSearch;
    }
    
    /**
     * 19.4.2024 Sets the last searched city
     * @param lastSearchedCity city that was searched last during use of program
     * Jukka Ruhanen
     */
    public void setLastSearch(String lastSearchedCity){
        lastSearch = lastSearchedCity;
    }
    
    
    /**
     * 20.4.2024 Adds new favorite to favoriteList
     * @param searchedCity city that is on the cearchField at the moment.
     * Oskari Aleksejev
     */
    //(This Still Uses the testList)
    public void addFavorite(String searchedCity){
        testList.add(searchedCity);
    }
    
}
