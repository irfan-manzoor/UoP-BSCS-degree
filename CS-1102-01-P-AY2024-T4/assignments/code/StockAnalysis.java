import java.util.ArrayList;

public class StockAnalysis {
    
    // Method to calculate the average stock price
    public static float calculateAveragePrice(float[] prices) {
        // Initialize a variable to store the sum of prices
        float sum = 0;
        // Loop through each price in the array
        for (float price : prices) {
            // Add the price to the sum
            sum += price;
        }
        // Calculate the average by dividing the sum by the number of prices
        return sum / prices.length;
    }

    // Method to find the maximum stock price
    public static float findMaximumPrice(float[] prices) {
        // Initialize a variable to store the maximum price, assuming the first price is the maximum initially
        float maxPrice = prices[0];
        // Loop through each price in the array
        for (float price : prices) {
            // Update the maxPrice if the current price is greater
            if (price > maxPrice) {
                maxPrice = price;
            }
        }
        // Return the maximum price found
        return maxPrice;
    }

    // Method to count the occurrences of a specific price
    public static int countOccurrences(float[] prices, float targetPrice) {
        // Initialize a variable to store the count of occurrences
        int count = 0;
        // Loop through each price in the array
        for (float price : prices) {
            // Increment the count if the current price matches the target price
            if (price == targetPrice) {
                count++;
            }
        }
        // Return the count of occurrences
        return count;
    }

    // Method to compute the cumulative sum of stock prices
    public static ArrayList<Float> computeCumulativeSum(ArrayList<Float> prices) {
        // Initialize an ArrayList to store the cumulative sum
        ArrayList<Float> cumulativeSum = new ArrayList<>();
        // Initialize a variable to store the sum
        float sum = 0;
        // Loop through each price in the ArrayList
        for (float price : prices) {
            // Add the current price to the sum
            sum += price;
            // Add the cumulative sum to the ArrayList
            cumulativeSum.add(sum);
        }
        // Return the ArrayList containing the cumulative sum
        return cumulativeSum;
    }

    public static void main(String[] args) {
        // Example usage:
        // Define an array of stock prices
        float[] pricesArray = {10.5f, 12.3f, 11.8f, 13.2f, 10.5f, 12.9f, 10.5f, 13.5f, 11.0f, 12.7f};
        // Create an ArrayList from the array
        ArrayList<Float> pricesArrayList = new ArrayList<>();
        for (float price : pricesArray) {
            pricesArrayList.add(price);
        }
        
        // Calculate average price
        float averagePrice = calculateAveragePrice(pricesArray);
        System.out.println("Average Price: " + averagePrice);
        
        // Find maximum price
        float maximumPrice = findMaximumPrice(pricesArray);
        System.out.println("Maximum Price: " + maximumPrice);
        
        // Count occurrences of a specific price
        float targetPrice = 10.5f;
        int occurrences = countOccurrences(pricesArray, targetPrice);
        System.out.println("Occurrences of " + targetPrice + ": " + occurrences);
        
        // Compute cumulative sum
        ArrayList<Float> cumulativeSum = computeCumulativeSum(pricesArrayList);
        System.out.println("Cumulative Sum: " + cumulativeSum);
    }
}