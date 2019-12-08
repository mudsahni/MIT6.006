import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Scanner;

public class DocumentDistance {

    public static String[] readFile(String filename) {
        StringBuilder data = new StringBuilder();
        try {
            File file = new File(filename);
            Scanner reader = new Scanner(file);
            while (reader.hasNextLine()) {
                data.append(reader.nextLine());
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("File " + filename + " could not be found.");
            e.printStackTrace();
            System.exit(0);
        }
        String D = data.toString().toLowerCase().replaceAll("\\p{Punct}", "");
        return D.split(" ", 0);
    }

    public static HashMap<String, Integer> countFrequency(String[] wordList) {
        HashMap<String, Integer> D = new HashMap<String, Integer>();

        for (String word : wordList) {
            if (D.containsKey(word)) {
                int temp = D.get(word) + 1;
                D.put(word, temp);
            } else {
                D.put(word, 1);
            }
        }
        return D;
    }

    public static HashMap<String, Integer> getCountFrequency(String filename) {
        String[] wordsList = readFile(filename);
        return countFrequency(wordsList);
    }

    public static int innerProduct(HashMap<String, Integer> D1, HashMap<String, Integer> D2) {
        int sum = 0;
        for (String key : D1.keySet()) {
            if (D2.containsKey(key)) {
                sum += D1.get(key) * D2.get(key);
            }
        }
        return sum;
    }

    public static double vectorAngle(HashMap<String, Integer> D1, HashMap<String, Integer> D2) {
        double numerator = (double) innerProduct(D1, D2);
        double denominator = Math.sqrt(innerProduct(D1, D1) * innerProduct(D2, D2));
        return Math.acos(numerator / denominator);
    }

    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java DocumentDistance filename1 filename2");
        }
        HashMap<String, Integer> D1 = getCountFrequency("src/" + args[0]);
        HashMap<String, Integer> D2 = getCountFrequency("src/" + args[1]);
        System.out.println("The distance between the two documents is: " + vectorAngle(D1, D2) + " radians.");

    }
}
