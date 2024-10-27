package lab3;

import org.uncommons.watchmaker.framework.operators.AbstractCrossover;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Random;
import java.util.Set;

import static lab3.TspMutation.generateTwoRandomInts;

public class TspCrossover extends AbstractCrossover<TspSolution> {
    protected TspCrossover() {
        super(1);
    }

    protected List<TspSolution> mate(TspSolution p1, TspSolution p2, int i, Random random) {
        List<TspSolution> children = new ArrayList<>();
        children.add(orderCrossover(p1, p2, random));
        children.add(orderCrossover(p2, p1, random));

        return children;
    }

    private TspSolution orderCrossover(TspSolution p1, TspSolution p2, Random random) {
        List<Integer> tour1 = p1.getPermutation();
        List<Integer> tour2 = p2.getPermutation();
        assert tour1.size() == tour2.size();
        int dimension = tour1.size();
        Point twoRandomAlleles = generateTwoRandomInts(dimension, random);

        int a = twoRandomAlleles.getX();
        int b = twoRandomAlleles.getY();
        List<Integer> child = orderCrossover(tour1, tour2, a, b);

        return new TspSolution(child);
    }

    private static List<Integer> orderCrossover(
            List<Integer> baseParent,
            List<Integer> traverseParent,
            int a,
            int b
    ) {
        int dimension = baseParent.size();
        List<Integer> child = new ArrayList<>(Collections.nCopies(dimension, 0));
        Set<Integer> used = new HashSet<>();
        for (int i = a; i <= b; i++) {
            int cur = baseParent.get(i);
            used.add(cur);
            child.set(i, cur);
        }
        int insertIndex = (b + 1) % dimension;
        for (int i = 0; i < dimension; i++) {
            int curIndex = (b + 1 + i) % dimension;
            int cur = traverseParent.get(curIndex);
            if (!used.contains(cur)) {
                child.set(insertIndex, cur);
                insertIndex = (insertIndex + 1) % dimension;
            }
        }

        return child;
    }

    public static void main(String[] args) {
        List<Integer> p1 = new ArrayList<>();
        for (int i = 1; i <= 9; i++) {
            p1.add(i);
        }
        List<Integer> p2 = new ArrayList<>();
        int[] rawP2 = {3, 7, 5, 2, 8, 1, 4, 9, 6};
        for (int v : rawP2) {
            p2.add(v);
        }

        System.out.println(p1);
        System.out.println(p2);

        int a = 3;
        int b = 6;
        List<Integer> child = orderCrossover(p1, p2, a, b);

        System.out.println(child);

        int[] correctCrossover = {2, 8, 1, 4, 5, 6, 7, 9, 3};
        boolean correct = true;
        for (int i = 0; i < correctCrossover.length; i++) {
            correct &= correctCrossover[i] == child.get(i);
        }
        System.out.println(correct);
    }
}
