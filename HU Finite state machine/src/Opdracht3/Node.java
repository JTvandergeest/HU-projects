package Opdracht3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Random;

public class Node {

    public ArrayList<Path> outputNodes = new ArrayList<>();
    public static ArrayList<Node> nodes = new ArrayList<>();
    private String name;
    public Random random = new Random();

    public Node() {
        Node.nodes.add(this);
        this.name = "node " + Node.nodes.indexOf(this);
    }

    public Node(String name) {
        Node.nodes.add(this);
        this.name = name;
    }

    public boolean hasPaths(){
        return !outputNodes.isEmpty();
    }

    public void addOutput(Path path) {
        this.outputNodes.add(path);
    }

    public Path decidePath(){
        float randNr = random.nextFloat();
        float counter = 0;
        for (Path path : outputNodes){
            if (randNr >= counter && randNr <= (counter + path.chance)){
                return path;
            }
            counter += path.chance;
        }
        return null;
    }

    public Node tryTakePathText(String text){
        for (Path path : outputNodes){
            if (path.path.equals(text)) return path.connectNode;
        }
        return this;
    }
    public Node tryTakePathRandom(){
        Path path = decidePath();
        if (path != null) return path.connectNode;
        return this;
    }

    public String getName() {
        return this.name;
    }
}