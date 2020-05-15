package Opdracht3;


import org.junit.Assert;
import org.junit.jupiter.api.Test;

class NodeTest {

    @Test
    void NodeHasPath() {
        Node node = new Node();
        node.addOutput(new Path("A", 1, node));
        Assert.assertTrue(node.hasPaths());
        }
}