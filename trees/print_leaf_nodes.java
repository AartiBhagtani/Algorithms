// construct binary tree
// print leaf nodes from left to right
class print_leaf_nodes 
{
  static class Node 
  {
    public int data;
    public Node left, right;
  }
  static Node newNode(int data)
  {
    Node temp = new Node();
    temp.data = data;
    temp.left = null;
    temp.right = null;
    return temp;
  }
  static void printLeafNodes(Node root)
  {
    if(root == null)
    {
      return;
    }
    if(root.left == null && root.right == null)
    {
      System.out.print(root.data+" ");
      return;
    }
    if(root.left != null)
    {
      printLeafNodes(root.left);
    }
    if(root.right != null)
    {
      printLeafNodes(root.right);
    }
  }

  static void insert(int data, Node root)
  {
    Node current = root;
    while(true)
    {
      if(data <= current.data)
      {
        if(current.left == null)
        {
          current.left = element;
          return;
        }
      }
      else
      {
        if(current.right == null)
        {
          current.right = element;
          return;
        }
      }
    }
  }

  public Node root = newNode(50);

  public static void main(String []args)
  {
    insert(50, rooot); 
    insert(50, root);  
    insert(50, root);  
    insert(50, root);  
    insert(50, root); 
  }
}
