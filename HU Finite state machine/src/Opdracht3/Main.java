package Opdracht3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        Node s0 = new Node();
        Node s1 = new Node();

        Node s2 = new Node();
        Node s3 = new Node();

        s0.addOutput(new Path("A", (float) 1/2, s0));
        s0.addOutput(new Path("B", (float) 1/2, s1));

        s1.addOutput(new Path("A", (float) 1/3, s0));
        s1.addOutput(new Path("B", (float) 1/3, s1));
        s1.addOutput(new Path("C", (float) 1/3, s2));

        s2.addOutput(new Path("A", (float) 1/3, s1));
        s2.addOutput(new Path("B", (float) 1/3, s2));
        s2.addOutput(new Path("C", (float) 1/3, s3));

        String type = "T";
        String verwerkString = "ABBA";
        int startNodeNum = 0;

        try {
            System.out.print("Text or Random? (T/R): ");
            type = Main.getInput();
            if (type.equals("T")){
                System.out.print("Text pattern (ABC): ");
                verwerkString = Main.getInput();
            }
            System.out.print("Start Node (No): ");
            startNodeNum = Integer.parseInt(Main.getInput());
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (type.equals("R")){
            Node nodeAt = Node.nodes.get(startNodeNum);
            System.out.println("Starting path at " + s0.getName());

            while (nodeAt.hasPaths()){
                nodeAt = nodeAt.tryTakePathRandom();
                System.out.println("Now at node " + nodeAt.getName());
            }
        }else{
            char[] pathlist = verwerkString.toCharArray();

            System.out.println("Starting path at Node 0");
            Node nodeAt = Node.nodes.get(startNodeNum);

            for (char path : pathlist){
                String pathStr = Character.toString(path);
                System.out.print(pathStr);
                System.out.println("Taking path " + path);
                nodeAt = nodeAt.tryTakePathText(pathStr);
                System.out.println("Now at node " + nodeAt.getName());
            }
        }
    }

    public static String getInput() throws IOException {
        BufferedReader reader =  new BufferedReader(new InputStreamReader(System.in));
        return reader.readLine();
    }
}
