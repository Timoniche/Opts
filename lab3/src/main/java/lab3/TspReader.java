package lab3;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class TspReader {
    private int dimension;
    private ArrayList<Point> cities;

    public TspReader(String problem) {
        ClassLoader classLoader = TspFitnessFunction.class.getClassLoader();
        URL problemURL = classLoader.getResource(problem);
        if (problemURL == null) {
            throw new IllegalArgumentException("problem's name is incorrect");
        }
        try (InputStream inputStream = problemURL.openStream()) {
            try (Scanner sc = new Scanner(inputStream)) {
                dimension = sc.nextInt();
                //size is dimension + 1 cause first is dummy
                cities = new ArrayList<>(Collections.nCopies(dimension + 1, new Point(0, 0)));
                for (int i = 0; i < dimension; i++) {
                    int id = sc.nextInt();
                    int x = sc.nextInt();
                    int y = sc.nextInt();
                    cities.set(id, new Point(x, y));
                }
            }
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public int getDimension() {
        return dimension;
    }

    public ArrayList<Point> getCities() {
        return cities;
    }
}
