package Opdracht3;

public class Path {
    public String path;
    public float chance;
    public Node connectNode;

    public Path(String path, float chance, Node connectNode) {
        this.path = path;
        this.chance = chance;
        this.connectNode = connectNode;
    }
}
