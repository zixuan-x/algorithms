//
//  HASH TABLE. A bucketed hash table.
//
//  Because of bugs in the way Java handles generic classes, you will get these
//  warning messages when you compile this program. Just ignore them.
//
//    Note: HashTable.java uses unchecked or unsafe operations.
//    Note: Recompile with -Xlint:unchecked for details.
//

//  HASH TABLE. A bucketed hash table that maps KEY's to VALUE's.

class HashTable<Key, Value>
{

//  NODE. A node in a linear singly linked list.

  private class Node
  {
    private Key   key;    //  The key that's associated with VALUE.
    private Value value;  //  The value that KEY is associated with.
    private Node  next;   //  The next NODE in the list, or NULL.

//  Constructor. Make a new NODE with specified slots.

    private Node(Key key, Value value, Node next)
    {
      this.key   = key;
      this.value = value;
      this.next  = next;
    }
  }

  private Node     head;   //  Shared head node, used by DELETE.
  private Object[] table;  //  Singly linked lists of NODEs.

//  Constructor. Make a new HASH TABLE with SIZE buckets. For general use, SIZE
//  should be a "large" prime number. It defaults to 997. Because of Java bugs,
//  we can't make an array of NODE's. We make an array of OBJECT's instead, and
//  use casts where necessary.

  public HashTable()
  {
    this(997);
  }

  public HashTable(int size)
  {
    if (size <= 0)
    {
      throw new IllegalArgumentException("Size must be greater than 0.");
    }
    else
    {
      head = new Node(null, null, null);
      table = new Object[size];
    }
  }

//  DELETE. Break the association between KEY and its VALUE. If it doesn't have
//  an associated VALUE, then do nothing. HEAD avoids special cases.

  public void delete(Key key)
  {
    int index = hash(key);
    Node left = head;
    Node right = (Node) table[index];
    head.next = right;
    while (right != null)
    {
      if (isEqual(key, right.key))
      {
        left.next = right.next;
        break;
      }
      else
      {
        left = right;
        right = right.next;
      }
    }
    table[index] = head.next;
    head.next = null;
  }

//  GET. Find the VALUE associated with KEY and return it. If KEY has no VALUE,
//  then throw an exception.

  public Value get(Key key)
  {
    Node temp = (Node) table[hash(key)];
    while (temp != null)
    {
      if (isEqual(key, temp.key))
      {
        return temp.value;
      }
      else
      {
        temp = temp.next;
      }
    }
    throw new IllegalArgumentException("No such key.");
  }

//  HASH. Return an index into TABLE that is magically computed from KEY. Since
//  NULL has no methods, we must use a special case for it.

  private int hash(Key key)
  {
    if (key == null)
    {
      return 0;
    }
    else
    {
      return Math.abs(key.hashCode()) % table.length;
    }
  }

//  HAS KEY. Test if KEY is associated with a value.

  public boolean hasKey(Key key)
  {
    Node temp = (Node) table[hash(key)];
    while (temp != null)
    {
      if (isEqual(key, temp.key))
      {
        return true;
      }
      else
      {
        temp = temp.next;
      }
    }
    return false;
  }

//  IS EQUAL. Test if LEFT and RIGHT are equal.

  private boolean isEqual(Key left, Key right)
  {
    if (left == null || right == null)
    {
      return left == right;
    }
    else
    {
      return left.equals(right);
    }
  }

//  PUT. Associate KEY with VALUE.

  public void put(Key key, Value value)
  {
    int index = hash(key);
    Node temp = (Node) table[index];
    while (temp != null)
    {
      if (isEqual(key, temp.key))
      {
        temp.value = value;
        return;
      }
      else
      {
        temp = temp.next;
      }
    }
    table[index] = new Node(key, value, (Node) table[index]);
  }
}

//  CORNED BEEF HASH. Demonstrate how the HASH TABLE class works.

class CornedBeefHash
{

//  MAIN. Main program. The comments show what will be printed.

  public static void main(String[] args)
  {
    HashTable<String, Integer> ht = new HashTable<String, Integer>();

    ht.put("one",   1);
    ht.put("two",   2);
    ht.put("three", 3);
    ht.put("four",  4);
    ht.put("five",  5);
    ht.put(null,    7734);

    System.out.println(ht.hasKey(null));     //  true
    System.out.println(ht.hasKey("one"));    //  true
    System.out.println(ht.hasKey("two"));    //  true
    System.out.println(ht.hasKey("three"));  //  true
    System.out.println(ht.hasKey("four"));   //  true
    System.out.println(ht.hasKey("five"));   //  true
    System.out.println(ht.hasKey("zilch"));  //  false

    System.out.println(ht.get("one"));    //  1
    System.out.println(ht.get("two"));    //  2
    System.out.println(ht.get("three"));  //  3
    System.out.println(ht.get("four"));   //  4
    System.out.println(ht.get("five"));   //  5
    System.out.println(ht.get(null));     //  7734

    ht.delete("three");
    ht.delete(null);

    System.out.println(ht.hasKey("one"));    //  true
    System.out.println(ht.hasKey("two"));    //  true
    System.out.println(ht.hasKey("three"));  //  false
    System.out.println(ht.hasKey("four"));   //  true
    System.out.println(ht.hasKey("five"));   //  true
    System.out.println(ht.hasKey("zilch"));  //  false
    System.out.println(ht.hasKey(null));     //  false
  }
}
