//  SEQUENCE. An ordered sequence of zero or more objects.

//  To run this program under a Linux or Unix shell, type the following.
//
//    javac sequence.java
//    java Careless
//
//  When you compile this program, you may see the following silly warnings.
//
//    Note: sequence.java uses unchecked or unsafe operations.
//    Note: Recompile with -Xlint:unchecked for details.
//
//  Don't worry about them.  They result from the bug that keeps us from making
//  an array of BASEs directly. The program still works.
//

//  SEQUENCE. An ordered sequence of zero or more BASEs.

class Sequence<Base>
{
  private Base[] bases;      //  The BASEs themselves.
  private int    count;      //  How many BASEs in the SEQUENCE.
  private int    factor;     //  Multiply by this to make BASES bigger.
  private int    increment;  //  Add this to make BASES bigger.

  private static final int defaultFactor    = 2;   //  Default FACTOR.
  private static final int defaultIncrement = 1;   //  Default INCREMENT.
  private static final int defaultLength    = 10;  //  Default length of BASES.

//  Constructors. We fill in defaults for missing parameters.

  public Sequence()
  {
    bases     = (Base[]) new Object[defaultLength];
    count     = 0;
    factor    = defaultFactor;
    increment = defaultIncrement;
  }

  public Sequence(int length)
  {
    if (length >= 0)
    {
      bases     = (Base[]) new Object[length];
      count     = 0;
      factor    = defaultFactor;
      increment = defaultIncrement;
    }
    else
    {
      throw new IllegalArgumentException("Parameter out of range.");
    }
  }

  public Sequence(int length, int factor, int increment)
  {
    if (length >= 0 && factor >= 1 && increment >= 0)
    {
      bases          = (Base[]) new Object[length];
      count          = 0;
      this.factor    = factor;
      this.increment = increment;
    }
    else
    {
      throw new IllegalArgumentException("Parameter(s) out of range.");
    }
  }

//  ADD. Add BASE to the right end of SEQUENCE. If there's not room to add BASE
//  then make the SEQUENCE bigger first.

  public void add(Base base)
  {
    if (count >= bases.length)
    {
      Base[] biggerBases = (Base[]) new Object[bigger()];
      for (int index = 0; index < count; index += 1)
      {
        biggerBases[index] = bases[index];
      }
      bases = biggerBases;
    }
    bases[count] = base;
    count += 1;
  }

//  BIGGER. How big to make BASES when it needs to be bigger.

  private int bigger()
  {
    return factor * bases.length + increment;
  }

//  DELETE. Remove the BASE at INDEX.

  public void delete(int index)
  {
    if (0 <= index && index < count)
    {
      while (index < count - 1)
      {
        bases[index] = bases[index + 1];
        index += 1;
      }
      count -= 1;
      bases[count] = null;
    }
    else
    {
      throw new IllegalArgumentException("Index out of range.");
    }
  }

//  FIND. Return the index of the first BASE in the SEQUENCE. Return -1 if BASE
//  isn't there. We've factored out the equality test for improved efficiency.

  public int find(Base base)
  {
    if (base == null)
    {
      for (int index = 0; index < count; index += 1)
      {
        if (bases[index] == null)
        {
          return index;
        }
      }
    }
    else
    {
      for (int index = 0; index < count; index += 1)
      {
        if (base.equals(bases[index]))
        {
          return index;
        }
      }
    }
    return -1;
  }

//  GET. Return the BASE at INDEX.

  public Base get(int index)
  {
    if (0 <= index && index < count)
    {
      return bases[index];
    }
    else
    {
      throw new IllegalArgumentException("Index out of range.");
    }
  }

//  LENGTH. Return how many BASEs there are.

  public int length()
  {
    return count;
  }

//  TO STRING. Return this SEQUENCE as a STRING, for printing. We unrolled this
//  loop once to help place the commas and blanks between elements.

  public String toString()
  {
    StringBuilder builder = new StringBuilder();
    builder.append('[');
    if (count > 0)
    {
      builder.append(stringify(bases[0]));
      for (int index = 1; index < count; index += 1)
      {
        builder.append(", ");
        builder.append(stringify(bases[index]));
      }
    }
    builder.append(']');
    return builder.toString();
  }

//  STRINGIFY. A helper for TO STRING. Return BASE as a STRING.

  private String stringify(Base base)
  {
    if (base == null)
    {
      return "null";
    }
    else
    {
      return base.toString();
    }
  }

}

//  CARELESS. The careless driver. It may cause accidents.

class Careless
{

//  MAIN. Make an instance of SEQUENCE and test it. The comments show what will
//  be printed. This also shows how wrapper classes like INTEGER work.

  public static void main(String[] args)
  {
    Sequence<Integer> sequence = new Sequence<Integer>(4);

//  It's initially empty.

    System.out.println(sequence.length());  //  0
    System.out.println(sequence);           //  []

//  Add four elements, so it's full.

    sequence.add(1);
    sequence.add(2);
    sequence.add(3);
    sequence.add(4);
    System.out.println(sequence.length());  //  4
    System.out.println(sequence);           //  [1, 2, 3, 4]

//  Now add another element, so it gets bigger.
    
    sequence.add(5);
    System.out.println(sequence.length());  //  5
    System.out.println(sequence);           //  [1, 2, 3, 4, 5]

//  Remove the element at index 0.

    sequence.delete(0);
    System.out.println(sequence.length());  //  4
    System.out.println(sequence);           //  [2, 3, 4, 5]

//  Now remove 3. We don't know its index, but we can FIND it.

    sequence.delete(sequence.find(3));
    System.out.println(sequence.length());  //  3
    System.out.println(sequence);           //  [2, 4, 5]

//  Let's also see if we can FIND indexes of other elements.

    System.out.println(sequence.find(2));   //  0
    System.out.println(sequence.find(4));   //  1
    System.out.println(sequence.find(5));   //  2
  }
}
