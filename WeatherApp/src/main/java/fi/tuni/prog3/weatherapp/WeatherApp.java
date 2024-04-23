package fi.tuni.prog3.weatherapp;

import java.util.*;
import java.util.ArrayList;
import javafx.application.Application;
import javafx.application.Platform;
import javafx.event.ActionEvent;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javafx.scene.Node;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.control.ScrollPane;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;


/**
 * JavaFX Weather Application.
 */
public class WeatherApp extends Application {

    private final Font topBoxDefaultFont = new Font("SansSerif", 14);
    private final String memory = "memory.json";
    private MemoryManager memoryManager;
    
    private WeatherFetcher weatherFetcher;
    private StringProperty city = new SimpleStringProperty("London");

        //18.4.2024
        // root is now instance variable
        // Oskari Aleksejev
    private BorderPane root = new BorderPane();
    
    @Override
    public void start(Stage stage) {
        
        // 16.4.2024
        // Moved memorymanager up since it needs to be ran before creating the scene
        // Jukka Ruhanen
        
        //12.4.2024
        // Load favorites and last searched location
        // Jukka Ruhanen

        // 22.4.2024
        // Moved the hourly data fetch to the same try-catch block as the current data fetch
        // Lassi Cederlöf
        
        this.memoryManager = new MemoryManager();
        try{
            System.out.println("Loading search data...");
            memoryManager.readFromFile(memory);
            System.out.println("Success!");
        }
        catch (Exception e){
            System.out.println("Loading failed.");
        }
        this.weatherFetcher = new WeatherFetcher();
        // Remove comment when weatherfetcher has check for existing cities
        //city = new SimpleStringProperty(memoryManager.getLastSearch());
        try{
            weatherFetcher.GetWeatherData(city.get(), 2);
            weatherFetcher.GetWeatherData(city.get(), 1);
        }
        catch (Exception e){

        }
        
        //Creating a new BorderPane.
        root.setPadding(new Insets(10, 10, 10, 10));

        //Adding HBox to the center of the BorderPane.
        root.setCenter(getCenterVBox());
        
        //Adding HBOx to the top of the BorderPane
        HBox topRow = new HBox(400/3);
        root.setTop(topRow);

        //Adding button to the BorderPane and aligning it to the right.
        var quitButton = getQuitButton();
        BorderPane.setMargin(quitButton, new Insets(10, 10, 0, 10));
        root.setBottom(quitButton);
        BorderPane.setAlignment(quitButton, Pos.TOP_RIGHT);
       

        /**
         * 
         * 12.4.2024 - Made top part of the interface - Oskari Aleksejev
         * 18.4.2024 - small variable name change - Oskari Aleksejev
         * 22.4.2024 - Added middle and bottom part of the interface - Lassi Cederlöf
        */
        
        //Adding button to the BorderPane
        var imperialButton = getImperialButton();
        BorderPane.setMargin(imperialButton,new Insets(10,10,0,10));
        
        //Adding button to the BorderPane and aligning it to the top right.
        var favButton = getFavSearchButton();
        BorderPane.setMargin(favButton,new Insets(10,10,0,10));
        
        //Adding city name to the BorderPane top center
        Label cityName = new Label(city.get());
        //keeps city name updated
        cityName.textProperty().bind(city);
        
        cityName.setStyle("-fx-font-weight:bold");
        BorderPane.setMargin(cityName,new Insets(10,10,0,10));
        
        //Add Top of the BorderPane
        topRow.getChildren().addAll(imperialButton,cityName,favButton);
        
        Scene scene = new Scene(root, 500, 700);
        stage.setScene(scene);
        stage.setTitle("WeatherApp");
        stage.show();
        
    }

    public static void main(String[] args) {
        launch();
    }

    private VBox getCenterVBox() {
        //Creating an HBox.
        VBox centerHBox = new VBox(2);

        //Adding two VBox to the HBox.
        centerHBox.getChildren().addAll(getTopHBox(), getMiddleHBox(), getBottomHBox());

        return centerHBox;
    }

    /**
     * 19.4.2024 Creates the upper box for the programs GUI, the box contains 
     * information about the current weather. Current temperature, what it feels
     * like, wind speed and direction, and cloudiness-% is shown in the top box.
     * Returns the top box.
     * @return topBox, containing many labels with information
     * Jukka Ruhanen
     */
    private HBox getTopHBox() {
        //Creating a VBox for the left side.
        HBox leftHBox = new HBox();
        leftHBox.setPrefHeight(330);
        leftHBox.setStyle("-fx-background-color: #8fc6fd;");

        /**
         * 18.4.2024
         * TopBox creation updated. Closer to "finished" product. 
         * Shows windspeed, temp, and temp_feelslike.
         * Jukka Ruhanen
         * 
         * 19.4.2024
         * TopBox style updated, now also displays cloudiness and wind direction
         * Jukka Ruhanen
         */
        GridPane grid = new GridPane();
        grid.setHgap(20);
        grid.setVgap(10);
        
        Label currentWeatherLabel = new Label("Current weather");
        grid.add(currentWeatherLabel, 1, 0);
        
        Label currentTemperatureLabel = new Label(String.format("Temperature: %.1f \u2103", 
                weatherFetcher.getCurrentWeatherData().main.temp));
        
        grid.add(currentTemperatureLabel, 0, 1);
        
        Label feelsLikeTemperatureLabel = new Label(String.format("Feels like: %.1f \u2103",
                weatherFetcher.getCurrentWeatherData().main.feels_like));
        grid.add(feelsLikeTemperatureLabel, 0, 2);
        
        Label windSpeedLabel = new Label(String.format("Wind: %.2f m/s",
                weatherFetcher.getCurrentWeatherData().wind.speed));
        Label windDirectionLabel = new Label(String.format("Direction: %s",
                weatherFetcher.getWindDirection()));
        grid.add(windSpeedLabel, 1, 1);
        grid.add(windDirectionLabel, 1, 2);
        
        Label cloudinessLabel = new Label(String.format("Cloudiness: %.1f %%",
                weatherFetcher.getCurrentWeatherData().clouds.all));
        grid.add(cloudinessLabel, 2, 1);
        
        // Set same style for all labels
        for(Node node : grid.getChildren()){
            Label label = (Label) node;
            label.setAlignment(Pos.CENTER);
            label.setFont(topBoxDefaultFont);
        }
        // Bigger text and boldness for box info
        currentWeatherLabel.setFont(Font.font("SansSerif", FontWeight.BOLD, 24));
        leftHBox.getChildren().add(grid);
        
        leftHBox.setAlignment(Pos.CENTER);
        leftHBox.setPrefHeight(200);
        //leftHBox.getChildren().add(new Label("Top Panel"));
        
        return leftHBox;
    }


    /**
     * 22.4.2024
     * 
     * Creates the middle box for the programs GUI, the box contains
     * information about the weather for the next 4 days. The box shows the date,
     * the weather icon, and the temperature range for each day. Returns the middle box.
     * @return middleBox, containing many labels with information
     * 
     * Lassi Cederlöf
     */
    private HBox getMiddleHBox() {
        //Creating an HBox.
        HBox middleHBox = new HBox();
        middleHBox.setStyle("-fx-background-color: #A9A9A9;");

        GridPane grid = new GridPane();
        grid.setHgap(20);
        grid.setVgap(10);

        int gridPos = 0;

        int hour = weatherFetcher.getHour(0);
        int day = weatherFetcher.getDay(0);

        double minTemp = Double.NaN;
        double maxTemp = Double.NaN;

        Map<String, Integer> iconCounts = new HashMap<>();

        for (int i = 0; i < 96; i++) {
            Label dateLabel = new Label(weatherFetcher.getDate(i));
            if (weatherFetcher.getHourlyTemp(day, hour) < minTemp || Double.isNaN(minTemp)) {
                minTemp = weatherFetcher.getHourlyTemp(day, hour);
            }
            if (weatherFetcher.getHourlyTemp(day, hour) > maxTemp || Double.isNaN(maxTemp)) {
                maxTemp = weatherFetcher.getHourlyTemp(day, hour);
            }
            Label tempLabel = new Label(String.format("%.1f - %.1f", minTemp, maxTemp));

            String icon = weatherFetcher.getHourlyIcon(day, hour);
            iconCounts.put(icon, iconCounts.getOrDefault(icon, 0) + 1);

            hour++;
            if (hour == 24) {
                hour = 0;
                day++;
                gridPos++;

                grid.add(dateLabel, gridPos, 0);
                grid.add(tempLabel, gridPos, 2);

                minTemp = Double.NaN;
                maxTemp = Double.NaN;

                String mostCommonCode = null;
                int maxCount = 0;
                for (Map.Entry<String, Integer> entry : iconCounts.entrySet()) {
                    if (entry.getValue() > maxCount) {
                        mostCommonCode = entry.getKey();
                        maxCount = entry.getValue();
                    }
                }
                Image weatherIcon = new Image("http://openweathermap.org/img/wn/" + mostCommonCode + ".png");
                ImageView iconView = new ImageView(weatherIcon);
                grid.add(iconView, gridPos, 1);

                iconCounts.clear();
            }
        }

        middleHBox.setAlignment(Pos.CENTER);
        middleHBox.getChildren().add(grid);

        return middleHBox;
    }


    /**
     * 22.4.2024 Creates the bottom box for the programs GUI, the box contains 
     * information about the hourly forecast. The box shows the temperature for
     * every hour of the day. Returns the bottom box.
     * @return bottomBox, containing many labels with information
     * Lassi Cederlöf
     */
    private HBox getBottomHBox() {
        //Creating a VBox for the right side.
        HBox rightHBox = new HBox();
        rightHBox.setStyle("-fx-background-color: #b1c2d4;");
    
        //Creating a GridPane for the right side.
        GridPane grid = new GridPane();
        grid.setHgap(20);
        grid.setVgap(10);
        
        //Creating a label for the hourly forecast.
        Label hourlyWeatherLabel = new Label("Hourly forecast");
        grid.add(hourlyWeatherLabel, 1, 0);

        //Adding weather data to the GridPane.
        int hour = weatherFetcher.getHour(0);
        int day = weatherFetcher.getDay(0);

        for (int i = 0; i < 96; i++) {
            Label timeLabel = new Label(String.format("%02d", hour));
            Label tempLabel = new Label(String.format("%.1f \u2103", 
                weatherFetcher.getHourlyTemp(day, hour)));
            String icon = weatherFetcher.getHourlyIcon(day, hour);
            Image weatherIcon = new Image("http://openweathermap.org/img/wn/" + icon + ".png");
            ImageView iconView = new ImageView(weatherIcon);

            grid.add(timeLabel, 0, i + 1);
            grid.add(tempLabel, 2, i + 1);
            grid.add(iconView, 1, i + 1);

            hour++;
            if (hour == 24) {
                hour = 0;
                day++;
            }
        }
        
        // Set same style for all labels except the first one

        for(Node node : grid.getChildren()){
            if (node instanceof Label) {
                Label label = (Label) node;
                label.setAlignment(Pos.CENTER);
                label.setFont(topBoxDefaultFont);
            }
        }
        hourlyWeatherLabel.setFont(Font.font("SansSerif", FontWeight.BOLD, 24));
        rightHBox.getChildren().add(grid);

        //Adding the GridPane to the right side.
        rightHBox.setAlignment(Pos.CENTER);

        //Adding a ScrollPane to the right side.
        ScrollPane scrollPane = new ScrollPane(rightHBox);
        scrollPane.setFitToWidth(true);
        scrollPane.setFitToHeight(true);

        scrollPane.prefWidthProperty().bind(root.widthProperty());

        return new HBox(scrollPane);
    }

    private Button getQuitButton() {
        //Creating a button.
        Button button = new Button("Quit");

        //Adding an event to the button to terminate the application.
        button.setOnAction((ActionEvent event) -> {
            //Save traces of use to json file (lastSearch, favorites).
            try{
                memoryManager.setLastSearch(city.get());
                memoryManager.writeToFile(memory);
            }
            catch (Exception e){
                
            }
            finally{
                Platform.exit();
            }
        });

        return button;
    }
    
    
    /**
     * 13.4.2024 - SearchBar for new locations and Favorite option. (in progress)
     * - Oskari Aleksejev
     * 
     */
    private Button getFavSearchButton(){
        Button button = new Button("Favorites/search");
        
        button.setOnAction((ActionEvent event) -> {
            //new scene. Search bar and favorite button 
            VBox searchRoot = new VBox();
            
            HBox searchBox = new HBox();
            ArrayList<Button> fButtonList = new ArrayList();
            
            TextField searchField = new TextField();
            Button searchButton = new Button("Search");
            Button favButton = new Button("Favorite");
            
            //TO-DO delete favorite? or just limit and replace?
            
            searchBox.getChildren().addAll(searchField,searchButton,favButton);
            searchRoot.getChildren().add(searchBox);
            
            // 19.4.2024
            // Creates buttons from the list of favorites.
            // oskari Aleksejev
            for(String fav : memoryManager.getFavorites()){
                Button fButton = new Button(fav);
                fButton.setOnAction(this::handleFavCityButtonClick);
                fButtonList.add(fButton);
                
            }
            searchRoot.getChildren().addAll(fButtonList);
            
            Stage sStage = new Stage();
            sStage.setTitle("Search");
            sStage.setScene(new Scene(searchRoot));
            sStage.show();
            
            searchButton.setOnAction((ActionEvent searchEvent) -> {
            //fetches new weatherinformation based on search
            try{
                System.out.println(city); //test
                city.set(searchField.getText());
                System.out.println(city);   //test
                
                /**
                 * 18.4.2024
                 *  updates the information on the interface
                 *  - oskari aleksejev
                 */
                
                try{
                    weatherFetcher.GetWeatherData(city.get(),2);   //daily data
                    weatherFetcher.GetWeatherData(city.get(),1);    //hourly data
                    memoryManager.setLastSearch(city.get());
                    root.setCenter(getCenterVBox());
                }catch(Exception e){
                    
                }

                //TO-DO write in file
                sStage.close();
            }catch(Exception e){
                
            }
            });  
            
            /**
             * 20.4.2024
             * Adds current city in searchField to the list of favorites
             * Greates a button for the favorite
             * 
             * TO-DO make sure city/location excists before anything else
             * 
             * Oskari Aleksejev
             */
            favButton.setOnAction((ActionEvent addFavoriteEvent)->{
                try{
                    memoryManager.addFavorite(searchField.getText());
                    memoryManager.writeToFile(memory);
                    
                    Button newFButton = new Button(searchField.getText());
                    searchRoot.getChildren().add(newFButton);
                    newFButton.setOnAction(this::handleFavCityButtonClick);
                    
                    sStage.sizeToScene();
                    
                    memoryManager.printMemory();
                }catch(Exception e){
                        
                }
            });
            
        });
        return button;
    }
    
    
    
    /**
     * 20.4.2024
     * Handler for list of favorites
     * when favorited city button is clicked, fetch weather data, update
     * interface and close the favorite/search window.
     * 
     * Oskari Aleksejev
     */
    private void handleFavCityButtonClick(ActionEvent event){
        Button buttonClicked = (Button) event.getSource();
        try{
            weatherFetcher.GetWeatherData(buttonClicked.getText(), 1);
            weatherFetcher.GetWeatherData(buttonClicked.getText(),2);
            city.set(buttonClicked.getText());
            root.setCenter(getCenterVBox());
            
            Stage sStage = (Stage) buttonClicked.getScene().getWindow();
            sStage.close();
        }catch(Exception e){
            
        }
    }
    
    private Button getImperialButton(){
        Button button = new Button("Imperial");
        button.setOnAction((ActionEvent event) -> {
            //shows everything in imperial form.
        });
        return button;
    }
}