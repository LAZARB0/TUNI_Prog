package fi.tuni.prog3.weatherapp;

import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;

import java.util.ArrayList;
import java.util.List;

public class WeatherFetcher {
    
    /**
     * 16.4.2024 
     * Added these
     * Jukka Ruhanen
     * 
     * 22.4.2024 Changed the hourlyData to hourlyDataList
     * Lassi Cederlöf
     */
    private WeatherData currentWeatherData;
    private List<HourlyData> hourlyDataList = new ArrayList<>();


    /**
     *
     *  10.4.2024 fetchWeatherWithScanner funktion pohja
     * 
     *  16.4.2024 Added index parameter to the function, to choose between hourly and daily data
     *  also added the possibility to change the city
     * 
     *  Lassi Cederlöf
     */
    public String fetchWeatherWithScanner(String city, int index) throws Exception {
        System.out.println("fetchWeatherWithScanner");
        String urlStr = "";
        if (index == 1) {
            urlStr = "https://pro.openweathermap.org/data/2.5/forecast/hourly?q=" + city + "&appid=cd561357f97263dcc93ee7ecb28333fa ";
        } else {
            urlStr = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=cd561357f97263dcc93ee7ecb28333fa";
        }
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");

        InputStream in = conn.getInputStream();
        Scanner scanner = new Scanner(in);
        scanner.useDelimiter("\\A");
        String content = scanner.hasNext() ? scanner.next() : "";

        scanner.close();
        conn.disconnect();
        
        return content;
    }

    /**
     *
     *  11.4.2024 parseWeatherData function, parses the json string to WeatherData class
     * 
     *  Lassi Cederlöf
     */
    public static WeatherData parseWeatherData(String jsonString) {
        Gson gson = new Gson();
        return gson.fromJson(jsonString, WeatherData.class);
    }


    /**
     *
     *  16.4.2024 parseHourlyDataList function, parses the json string to a list of HourlyData class
     * 
     *  Lassi Cederlöf
     */
    public static List<HourlyData> parseHourlyDataList(String jsonString) {
        List<HourlyData> hourlyDataList = new ArrayList<>();
        
        JsonParser parser = new JsonParser();
        JsonElement jsonElement = parser.parse(jsonString);
        JsonArray hourlyArray = jsonElement.getAsJsonObject().getAsJsonArray("list");

        Gson gson = new Gson();
        for (JsonElement element : hourlyArray) {
            HourlyData hourlyData = gson.fromJson(element, HourlyData.class);
            hourlyDataList.add(hourlyData);
        }

        return hourlyDataList;
    }

    /**
     *
     *  11.4.2024 WeatherData class for the parseWeatherData function
     * 
     *  Lassi Cederlöf
     */
    public static class WeatherData {
        public Coord coord;
        public Main main;
        public Wind wind;
        public Clouds clouds;

        public static class Coord {
            public double lon;
            public double lat;
        }

        public static class Main {
            public double temp;
            public double feels_like;
            public double temp_min;
            public double temp_max;
        }

        public static class Wind {
            public double speed;
            public double deg;
        }

        public static class Clouds {
            public double all;
        }
    }


    /**
     *
     *  11.4.2024 HourlyData class for the parseWeatherData function
     *  parses the hourly data from the api 
     * 
     *  Lassi Cederlöf
     */
    public static class HourlyData {
        public String dt_txt;
        public Main main;
        public Clouds clouds;
        public List<Weather> weather;
    
        public static class Main {
            public double temp;
            public double temp_min;
            public double temp_max;
        }
    
        public static class Clouds {
            public double all;
        }

        public static class Weather {
            public String icon;
        }
    }
    
    /**
     *
     *  11.4.2024 GetWeatherData function, exctracts data from the api using
     *  fetchWeatherWithScanner and parseWeatherData functions, and prints the data
     *  for testing purposes
     * 
     *  16.4.2024 Added index parameter to the function, to choose between hourly and daily data
     *  also added the possibility to change the city
     * 
     *  22.4.2024 Changed the hourlyDataList to a global variable
     * 
     *  Lassi Cederlöf
     */
    public void GetWeatherData(String city, int index) {
        try {
            if (index == 1) {
                String json = fetchWeatherWithScanner(city, 1);

                hourlyDataList = parseHourlyDataList(json);
            
                for (HourlyData hourlyData : hourlyDataList) {

                    double temp = hourlyData.main.temp;
                    String Time = hourlyData.dt_txt;
                    String icon = hourlyData.weather.get(0).icon;

                    System.out.println("Time: " + Time);
                    System.out.println("Temperature: " + temp);
                    System.out.println("Icon: " + icon);
                    
                }
            } else if (index == 2) {
                String json = fetchWeatherWithScanner(city, 2);
                WeatherData weatherData = parseWeatherData(json);
                currentWeatherData = parseWeatherData(json);
                dataKelvinsToCelsius();
                System.out.println("Temperature: " + weatherData.main.temp);
                System.out.println("Feels like: " + weatherData.main.feels_like);
                System.out.println("Min temperature: " + weatherData.main.temp_min);
                System.out.println("Max temperature: " + weatherData.main.temp_max);
            } else {
                System.out.println("Invalid index");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    /**
     * 16.4.2024 Returns the WeatherData entity
     * @return WeatherData
     * Jukka Ruhanen
     */
    public WeatherData getCurrentWeatherData(){
        // How it works:
        // If you want for example winds speed, do 
        // wf.getCurrentWeatherData().wind.speed;
        return currentWeatherData;
    }
    
    /**
     * 16.4.2024 Converts the temperature data in WeatherData from Kelvins to
     * celsius
     * Jukka Ruhanen
     */
    public void dataKelvinsToCelsius(){
        currentWeatherData.main.feels_like -= 273.15;
        currentWeatherData.main.temp -= 273.15;
        currentWeatherData.main.temp_max -= 273.15;
        currentWeatherData.main.temp_min -= 273.15;
    }
    
    /**
     * 19.4.2024 Checks what direction the wind is point towards and returns it
     * @return the direction of wind
     * Jukka Ruhanen
     */
    public String getWindDirection(){
        double deg = currentWeatherData.wind.deg % 360;
 
        if (deg > 25 && deg <= 65){
            return "North-East";
        }
        else if (deg > 65 && deg <= 115){
            return "East";
        }
        else if (deg > 115 && deg <= 155){
            return "South-East";
        }
        else if (deg > 155 && deg <= 205){
            return "South";
        }
        else if (deg > 205 && deg <= 245){
            return "South-West";
        }
        else if (deg > 245 && deg <= 295){
            return "West";
        }
        else if (deg > 295 && deg <= 335){
            return "North-West";
        }
        else{ //(deg > 335 || deg <= 25){
            return "North";
        }
    }

    /**
     * 22.4.2024
     * Added this function to get the current hour and
     * the hour to get data from hourlyDataList 
     * 
     * @param index the index of the hourlyDataList, 0 if current hour
     * @return the hour on the hourlyData
     * 
     * Lassi Cederlöf
     */
    public int getHour(int index) {
        HourlyData hourlyData = hourlyDataList.get(index);
        String dateTime = hourlyData.dt_txt;
        String[] parts = dateTime.split(" ");
        String[] timeParts = parts[1].split(":");
        int dataHour = Integer.parseInt(timeParts[0]);

        return dataHour;
    }


    /**
     * 22.4.2024
     * Added this function to get the current day and
     * the day to get data from hourlyDataList 
     * 
     * @param index the index of the hourlyDataList, 0 if current day
     * @return the day on the hourlyData
     * 
     * Lassi Cederlöf
     */
    public int getDay(int index) {
        HourlyData hourlyData = hourlyDataList.get(index);
        String dateTime = hourlyData.dt_txt;
        String[] parts = dateTime.split(" ");
        String[] dayParts = parts[0].split("-");
        int dataDay = Integer.parseInt(dayParts[2]);

        return dataDay;
    }


    /**
     * 22.4.2024
     * Added this function to get the date from the hourlyDataList
     * 
     * @param index the index of the hourlyDataList
     * @return the date on the hourlyData
     * 
     * Lassi Cederlöf
     */
    public String getDate(int index) {
        HourlyData hourlyData = hourlyDataList.get(index);
        String dateTime = hourlyData.dt_txt;
        String[] parts = dateTime.split(" ");
        String[] dayParts = parts[0].split("-");
        int dataDay = Integer.parseInt(dayParts[2]);
        int dataMonth = Integer.parseInt(dayParts[1]);
        int dataYear = Integer.parseInt(dayParts[0]);

        String dataDate =(dataDay + "." + dataMonth + "." + dataYear);

        return dataDate;
    }

    /**
     * 22.4.2024
     * 
     * Function to get the hourly temperature from the hourlyDataList
     * 
     * @param day
     * @param hour
     * @return the temperature at the given day and hour
     */
    public double getHourlyTemp(int day, int hour) {
        try {
            for (int i = 0; i < hourlyDataList.size(); i++) {

                HourlyData hourlyData = hourlyDataList.get(i);
                int dataHour = getHour(i);
                int dataDay = getDay(i);

                if (dataHour == hour && dataDay == day) {
                    return hourlyData.main.temp - 273.1;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return Double.NaN;
    }

    /**
     * 22.4.2024
     * 
     * Function to get the hourly icon from the hourlyDataList
     * 
     * @param day
     * @param hour
     * @return the icon at the given day and hour
     * 
     * Lassi Cederlöf
     */
    public String getHourlyIcon(int day, int hour) {
        try {
            for (int i = 0; i < hourlyDataList.size(); i++) {

                HourlyData hourlyData = hourlyDataList.get(i);
                int dataHour = getHour(i);
                int dataDay = getDay(i);

                if (dataHour == hour && dataDay == day) {
                    return hourlyData.weather.get(0).icon;
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }

        return "";
    }
}