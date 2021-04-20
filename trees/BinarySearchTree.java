public class BinarySearchTree
{
  public static class Node
  {
    int data;
    Node left;
    Node right;
  
    public Node(int data)
    {
      this.data = data;
      this.left = null;
      this.right = null;
    }
  }

  public Node root;

  public BinarySearchTree()
  {
    root = null;
  }

  public void insert(int data) 
  {
    Node newNode = new Node(data);
    if(root == null)
    {
      root = newNode;
      return;
    }
    Node current = root, parent = null;
    while(true) 
    {
      parent = current;
      if(data <= current.data)
      {
        current = current.left;
        if(current == null)
        {
          parent.left = newNode;
          return;
        }
      }
      else 
      {
        current = current.right;
        if(current == null)
        {
          parent.right = newNode;
          return;
        }
      }
    }
  } 
  public static void main(String[] args) {  

  BinarySearchTree bt = new BinarySearchTree();  
  //Add nodes to the binary tree  
  bt.insert(50);  
  bt.insert(30);  
  bt.insert(70);  
  bt.insert(60);  
  bt.insert(10);  
  bt.insert(90);  
}



}
