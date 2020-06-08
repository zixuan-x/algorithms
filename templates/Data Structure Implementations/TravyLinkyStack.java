//  TRAVY LINKY STACK. A traversable stack as a linear singly linked list.


import java.util.Iterator;

//  TRAVY LINKY STACK. A traversable stack. It's implemented as a linear singly
//  linked list of NODEs, each of which contains a BASE called VALUE.

class TravyLinkyStack<Base>
{

//  NODE. A node in a linear singly linked list.

  private class Node
  {
    private Base value;  //  The object in this NODE.
    private Node next;   //  The next NODE in the list, or NULL.

//  Constructor. Initialize a new NODE with VALUE and NEXT.

    private Node(Base value, Node next)
    {
      this.value = value;
      this.next = next;
    }
  }

  private Node top;  //  The NODE at the top of the stack, or NULL.

//  Constructor. Initialize a new empty TRAVY LINKED STACK.

  public TravyLinkyStack()
  {
    top = null;
  }

//  IS EMPTY. Test if the stack is empty.

  public boolean isEmpty()
  {
    return top == null;
  }

//  PEEK. Return the VALUE at the TOP of the stack.

  public Base peek()
  {
    if (isEmpty())
    {
      throw new IllegalStateException("Stack is empty.");
    }
    else
    {
      return top.value;
    }
  }

//  POP. Delete the VALUE at the TOP of the stack.

  public void pop()
  {
    if (isEmpty())
    {
      throw new IllegalStateException("Stack is empty.");
    }
    else
    {
      top = top.next;
    }
  }

//  PUSH. Add VALUE to the TOP of the stack.

  public void push(Base value)
  {
    top = new Node(value, top);
  }

//  TRAVY LINKY STACK ITERATOR. Iterator. It provides methods that let us visit
//  the VALUEs in a TRAVY LINKY STACK, from TOP to bottom.

  private class TravyLinkyStackIterator implements Iterator<Base>
  {
    private Node where;  //  The NODE with the VALUE we're visiting now.

//  Constructor. Initialize a new TRAVY LINKY STACK ITERATOR. It now visits the
//  VALUE at the top of the stack.

    private TravyLinkyStackIterator()
    {
      where = top;
    }

//  HAS NEXT. Test if any VALUEs remain to be visited.

    public boolean hasNext()
    {
      return where != null;
    }

//  NEXT. Return the VALUE we are visiting, after advancing the iterator to its
//  next VALUE.

    public Base next()
    {
      Base value = where.value;
      where = where.next;
      return value;
    }

//  REMOVE. Do nothing. This is here only to satisfy the ITERATOR interface.

    public void remove()
    { }
  }

//  ITERATOR. Return a new TRAVY LINKED STACK ITERATOR.

  public TravyLinkyStackIterator iterator()
  {
    return new TravyLinkyStackIterator();
  }
}

//  TRAVY LINKY STACK DRIVER. Demonstrate how a TRAVY LINKY STACK works.

class TravyLinkyStackDriver
{

//  MAIN. Run it.

  public static void main(String [] args)
  {

//  Make a new STACK and PUSH some strings into it.

    TravyLinkyStack<String> stack = new TravyLinkyStack<String>();

    stack.push("C");
    stack.push("B");
    stack.push("A");

//  Make an iterator and use it to print STACK's strings. We see A B C, printed
//  one per line.

    Iterator<String> stackerator = stack.iterator();
    while (stackerator.hasNext())
    {
      System.out.println(stackerator.next());
    }

//  We can have more than one iterator running at once. Here we print all pairs
//  of strings from STACK: AA AB AC BA BB BC CA CB CC, one per line.

    Iterator<String> firsterator = stack.iterator();
    while (firsterator.hasNext())
    {
      String firstString = firsterator.next();
      Iterator<String> seconderator = stack.iterator();
      while (seconderator.hasNext())
      {
        String secondString = seconderator.next();
        System.out.println(firstString + secondString);
      }
    }

//  But throughout all this, STACK remains unchanged.

    System.out.println(stack.isEmpty());            //  false
    System.out.println(stack.peek()); stack.pop();  //  A
    System.out.println(stack.peek()); stack.pop();  //  B
    System.out.println(stack.peek()); stack.pop();  //  C
    System.out.println(stack.isEmpty());            //  true
  }
}
