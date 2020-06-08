//  BST. Unbalanced binary search trees.


//  BST. Map KEY's to VALUE's using an unbalanced Binary Search Tree (BST). KEY
//  can be any class with a COMPARE TO method that takes KEY's as arguments.

class BST<Key extends Comparable<Key>, Value>
{

//  NODE. The BST is built from these.

  private class Node
  {
    private Key   key;    //  The key. Duh.
    private Value value;  //  The value associated with KEY.
    private Node  left;   //  Left subtree, whose KEY's are less than KEY.
    private Node  right;  //  Right subtree, whose KEY's are greater than KEY.

//  Constructor. Make a new NODE with KEY and VALUE. Its subtrees are NULL.

    private Node(Key key, Value value)
    {
      this.key   = key;
      this.value = value;
      this.left  = null;
      this.right = null;
    }
  }

  private Node head;  //  Temporary head NODE used by DELETE.
  private Node root;  //  Root NODE of the BST, or NULL.

//  Constructor. Make a new empty BST.

  public BST()
  {
    head = new Node(null, null);
    root = null;
  }

//  COUNT. Return the number of NODE's in this BST.

  public int count()
  { return counting(root); }

//  COUNTING. Do all the work for COUNT. It's a preorder traversal.

  private int counting(Node root)
  {
    if (root == null)
    {
      return 0;
    }
    else
    {
      return 1 + counting(root.left) + counting(root.right);
    }
  }

//  DELETE. Delete the NODE containing KEY from the BST. It's an error if there
//  is no such NODE.  We eliminate a special case by temporarily linking a HEAD
//  NODE into the BST above the ROOT. Kids, don't try this at home!

  public void delete(Key key)
  {
    Node above = head;  //  The NODE immediately above BELOW.
    Node below = root;  //  The NODE we're visiting now.
    head.right = root;
    while (true)
    {
      if (below == null)
      {
        throw new IllegalArgumentException("No such key.");
      }
      else
      {
        int test = key.compareTo(below.key);
        if (test < 0)
        {
          above = below;
          below = below.left;
        }
        else if (test > 0)
        {
          above = below;
          below = below.right;
        }
        else
        {
          if (below.left == null)
          {
            if (above.left == below)
            {
              above.left = below.right;
            }
            else
            {
              above.right = below.right;
            }
          }
          else if (below.right == null)
          {
            if (above.left == below)
            {
              above.left = below.left;
            }
            else
            {
              above.right = below.left;
            }
          }
          else
          {
            Node goner = below;
            above = below;
            below = above.left;
            while (below.right != null)
            {
              above = below;
              below = below.right;
            }
            if (above.left == below)
            {
              above.left = below.left;
            }
            else
            {
              above.right = below.left;
            }
            goner.key = below.key;
            goner.value = below.value;
          }
          break;
        }
      }
    }
    root = head.right;
  }

//  EMPTY. Delete all NODE's from the BST.

  public void empty()
  {
    root = null;
  }

//  GET. Find the NODE containing KEY in the BST, and return its VALUE. It's an
//  error if there is no such NODE.

  public Value get(Key key)
  {
    Node subtree = root;
    while (subtree != null)
    {
      int test = key.compareTo(subtree.key);
      if (test < 0)
      {
        subtree = subtree.left;
      }
      else if (test > 0)
      {
        subtree = subtree.right;
      }
      else
      {
        return subtree.value;
      }
    }
    throw new IllegalArgumentException("No such key.");
  }

//  HEIGHT. Return the height of this BST.

  public int height()
  {
    return heighting(root);
  }

//  HEIGHTING. Do all the work for HEIGHT. It's a postorder traversal.

  private int heighting(Node root)
  {
    if (root == null)
    {
      return 0;
    }
    else
    {
      int left  = heighting(root.left);
      int right = heighting(root.right);
      if (left > right)
      {
        return left + 1;
      }
      else
      {
        return right + 1;
      }
    }
  }

//  IS EMPTY. Test if the BST is empty.

  public boolean isEmpty()
  {
    return root == null;
  }

//  MAX KEY. Return the minimum key in the BST.

  public Key maxKey()
  {
    if (root == null)
    {
      throw new IllegalStateException("BST is empty.");
    }
    else
    {
      Node temp = root;
      while (temp.right != null)
      {
        temp = temp.right;
      }
      return temp.key;
    }
  }

//  MIN KEY. Return the minimum key in the BST.

  public Key minKey()
  {
    if (root == null)
    {
      throw new IllegalStateException("BST is empty.");
    }
    else
    {
      Node temp = root;
      while (temp.left != null)
      {
        temp = temp.left;
      }
      return temp.key;
    }
  }

//  PUT. Find the NODE containing KEY in the BST and reset its VALUE slot to be
//  the parameter VALUE. If there is no such NODE then add a new one containing
//  KEY and VALUE.

  public void put(Key key, Value value)
  {
    if (root == null)
    {
      root = new Node(key, value);
    }
    else
    {
      Node subtree = root;
      while (true)
      {
        int test = key.compareTo(subtree.key);
        if (test < 0)
        {
          if (subtree.left == null)
          {
            subtree.left = new Node(key, value);
            return;
          }
          else
          {
            subtree = subtree.left;
          }
        }
        else if (test > 0)
        {
          if (subtree.right == null)
          {
            subtree.right = new Node(key, value);
            return;
          }
          else
          {
            subtree = subtree.right;
          }
        }
        else
        {
          subtree.value = value;
          return;
        }
      }
    }
  }

//  TO STRING. Return a STRING describing this BST. An empty subtree is "∅" and
//  a nonempty subtree is "K(L, R)". Here K is the KEY at the subtree's root, L
//  is the root's LEFT subtree, and R is the root's RIGHT subtree.  VALUE's are
//  not shown in the STRING.

  public String toString()
  {
    StringBuilder builder = new StringBuilder();
    toStringing(builder, root);
    return builder.toString();
  }

//  TO STRINGING. Do all the work for TO STRING. It's a preorder traversal.

  private void toStringing(StringBuilder builder, Node subtree)
  {
    if (subtree == null)
    {
      builder.append('∅');
    }
    else
    {
      builder.append(subtree.key);
      builder.append('(');
      toStringing(builder, subtree.left);
      builder.append(',');
      builder.append(' ');
      toStringing(builder, subtree.right);
      builder.append(')');
    }
  }
}

//  BST DRIVER. Driver. Test the BST class.

class BSTDriver
{

//  MAIN. Make a BST and test it.

  public static void main(String [] args)
  {

//  Make an empty BST. Its KEYs are INTEGER's and its VALUEs are STRING's. This
//  works because INTEGER implements the interface COMPARABLE<INTEGER>.

    BST<Integer, String> bst = new BST<Integer, String>();

//  Is it really empty?

    System.out.println(bst.isEmpty());  //  true

//  It is, so add some NODE's. We order the KEY's to get a well balanced tree.

    bst.put(3, "three");
    bst.put(5, "five");
    bst.put(2, "two");
    bst.put(4, "four");
    bst.put(1, "one");

//  Print the tree along with some statistics.

    System.out.println(bst);           //  3(2(1(∅, ∅), ∅), 5(4(∅, ∅), ∅))
    System.out.println(bst.count());   //  5
    System.out.println(bst.height());  //  3
    System.out.println(bst.minKey());  //  1
    System.out.println(bst.maxKey());  //  5

//  This should print one ⇒ 1, two ⇒ 2, three ⇒ 3, four ⇒ 4, five ⇒ 5.
 
    for (int key = 1; key <= 5; key += 1)
    {
      System.out.println(key + " ⇒ " + bst.get(key));
    }

//  Finally delete root NODE's one at a time, until the BST is empty.

    bst.delete(3);
    System.out.println(bst);  //  2(1(∅, ∅), 5(4(∅, ∅), ∅))

    bst.delete(2);            //  1(∅, 5(4(∅, ∅), ∅))
    System.out.println(bst);

    bst.delete(1);
    System.out.println(bst);  //  5(4(∅, ∅), ∅)

    bst.delete(5);
    System.out.println(bst);  //  4(∅, ∅)

    bst.delete(4);
    System.out.println(bst);  //  ∅
  }
}
