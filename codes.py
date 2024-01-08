basics = {"Hello World Program":[
    '''
using System;

namespace FirstProgram
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("hello world!");
        }
    }
}
    ''',
    "Description"
],"Hello World Program but with Colored Console":[
    '''
using System;

namespace FirstProgram
{
    public class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Black;
            Console.BackgroundColor = ConsoleColor.White;
            Console.Clear();
            Console.WriteLine("hello world!");
        }
    }
}
    ''',
    ""
],"Console.ReadLine() User Input":[
    '''
Console.Write("What is your name: ");
string name = Console.ReadLine();
Console.WriteLine($"Hello {name}");
    ''',
    ""
],"Data Types #1":[
    '''
bool canIVote = true;
Console.WriteLine("Biggest Integer: {0}",int.MaxValue);
Console.WriteLine("Biggest Integer: {0}", int.MinValue);

Console.WriteLine("Biggest Long: {0}", long.MaxValue);
Console.WriteLine("Smmallest Long: {0}", long.MinValue);

decimal dePiVal = 3.141592653589793238462643383279502884197M;
decimal decBigNum = 3.0000000000000000000000000000000000000M;

Console.WriteLine("DEC: PI + bigNum: {0}", dePiVal + decBigNum);
    ''',
    ""
],"Data Types #2":[
    '''
Console.WriteLine("Biggest Double: {0}",Double.MaxValue);
double dblPiVal = 3.141592653589793238462643383279;
double dblBigNum = 3.000000000000002;
Console.WriteLine("DBL Pi + bigNum = {0}", dblPiVal + dblBigNum);

Console.WriteLine("Biggest Float: {0}",float.MaxValue);
float fltPiVal = 3.141592F;
float fltBigNum = 3.000002F;
Console.WriteLine("FLT: Pi + bigNum: {0}",fltPiVal+fltBigNum);
    ''',
    ""
],"Other Types":[
    '''
// byte: Represents an unsigned 8-bit integer (0 to 255)
byte myByte = 10;

// char: Represents a Unicode character (16-bit)
char myChar = 'A';

// sbyte: Represents a signed 8-bit integer (-128 to 127)
sbyte mySByte = -5;

// short: Represents a signed 16-bit integer (-32,768 to 32,767)
short myShort = 1000;

// uint: Represents an unsigned 32-bit integer (0 to 4,294,967,295)
uint myUInt = 50000U;

// ulong: Represents an unsigned 64-bit integer (0 to 18,446,744,073,709,551,615)
ulong myULong = 10000000000UL;

// ushort: Represents an unsigned 16-bit integer (0 to 65,535)
ushort myUShort = 60000;
    ''',
    ""
],"Conversion":[
    '''
bool boolFromStr = bool.Parse("true");
int intFromStr = int.Parse("100");
double dblFromStr = double.Parse("3.14159");

string strVal = dblFromStr.ToString();
Console.WriteLine($"Data Type: {strVal.GetType()}");
    ''',
    ""
],"Implicit Conversion":[
    '''
int myInt = 10;
long myLong = myInt; // Implicit conversion from int to long
    ''',
    "This occurs when the conversion between data types is done automatically by the compiler because there's no risk of losing information. For instance, converting from a smaller data type to a larger one."
],"Explicit Conversion (Casting)":[
    '''
double myDouble = 10.5;
int myInt = (int)myDouble; // Explicitly converting double to int (loses decimal part)
    ''',
    "This happens when you explicitly tell the compiler to convert a data type that might lose information in the process. You use casting syntax to indicate this conversion explicitly."
]}