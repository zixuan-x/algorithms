//  LINKY QUEUE. A queue as a linear singly linked list.

//  LINKY QUEUE. A queue of BASEs. It is implemented as a linear singly linked
//  list of NODEs, each of which contains a BASE called OBJECT.

class LinkyQueue<Base>
{

//  NODE. A node in a linear singly linked list.

  private class Node
  {
    private Base object;  //  Pointer to an object in the queue.
    private Node next;    //  Pointer to another NODE or to NULL.

//  Constructor. Initialize a new NODE with OBJECT and NEXT.

    private Node(Base object, Node next)
    {
      this.object = object;
      this.next = next;
    }
  }

  private Node front;  //  The NODE at the front of the queue, or NULL.
  private Node rear;   //  The NODE at the rear of the queue, or NULL.

//  Constructor. Initialize a new empty LINKY QUEUE.

  public LinkyQueue()
  {
    front = null;
    rear = null;
  }

//  IS EMPTY. Test if the queue is empty.

  public boolean isEmpty()
  {
    return front == null && rear == null;
  }

//  DEQUEUE. Remove an OBJECT from the FRONT of the queue and return it.

  public Base dequeue()
  {
    if (isEmpty())
    {
      throw new IllegalStateException("Queue is empty.");
    }
    else
    {
      Base object = front.object;
      front = front.next;
      if (front == null)
      {
        rear = null;
      }
      return object;
    }
  }

//  ENQUEUE. Add a new OBJECT at the REAR of the queue.

  public void enqueue(Base object)
  {
    if (isEmpty())
    {
      front = rear = new Node(object, null);
    }
    else
    {
      rear.next = new Node(object, null);
      rear = rear.next;
    }
  }
}

//  LINKY QUEUE DRIVER. Demonstrate how a LINKY QUEUE works.

class LinkyQueueDriver
{

//  MAIN. Run it.

  public static void main(String [] args)
  {

//  Make a new QUEUE.

    LinkyQueue<String> queue = new LinkyQueue<String>();

//  The QUEUE is initially empty.

    System.out.println(queue.isEmpty());  //  true

//  Enqueue some strings into it.

    queue.enqueue("A");
    queue.enqueue("B");
    queue.enqueue("C");

//  The QUEUE isn't empty now.

    System.out.println(queue.isEmpty());  //  false

//  Now DEQUEUE the strings.

    System.out.println(queue.dequeue());  //  A
    System.out.println(queue.dequeue());  //  B
    System.out.println(queue.dequeue());  //  C

//  The QUEUE is empty again.

    System.out.println(queue.isEmpty());  //  true    
  }
}
