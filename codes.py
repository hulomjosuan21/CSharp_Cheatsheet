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
],"Formatting":[
    '''
Console.WriteLine("Currency: {0:c}",23.45);
Console.WriteLine("Pad with 0s: {0:d4}",19);
Console.WriteLine("3 Decimals: {0:F3}",3.14159);
Console.WriteLine("Commas: {0:n4}",1900000);
    ''',
    ""
],"String Functions":[
    '''
string randString = "This is a string";
Console.WriteLine("String Length: {0}",randString.Length);
Console.WriteLine("String Contains 'is': {0}",randString.Contains("is"));
Console.WriteLine("Index of 'is': {0}",randString.IndexOf("is"));
Console.WriteLine("Remove String: {0}",randString.Remove(0,3+1));
Console.WriteLine("Insert String: {0}",randString.Insert(10,"short "));
Console.WriteLine("Replace String: {0}",randString.Replace("string","sentence"));

Console.WriteLine("Compare A to B: {0}",String.Compare("B","A",StringComparison.OrdinalIgnoreCase));
// Compare strings and ignore case
// < 0 : str 1 preceeds str2
// = 0 : Zero or Equal
// > 0 : st2 preceeds str1
Console.WriteLine("A = a {0}",String.Equals("A","a",StringComparison.OrdinalIgnoreCase));
Console.WriteLine("Pad Left: {0}",randString.PadLeft(20,'.'));
Console.WriteLine("Pad Right: {0}", randString.PadRight(randString.Length+4, '.'));
Console.WriteLine("Trim: {0}",randString.Trim());

Console.WriteLine("Uppercase: {0}",randString.ToUpper());
Console.WriteLine("Lowercase: {0}",randString.ToLower());

string newString = String.Format("{0} saw a {1} {2} in the {3}","Paul","rabbit","eating","field");
Console.Write(newString+"\\n");
Console.WriteLine(@"Exactly what I typed\\n");
    ''',
    ""
],"Array practice #1":[
    '''
int[] arr = new int[3];
arr[0] = 21;
Console.WriteLine("arr[0] = {0}", arr[0]);
    ''',
    ""
],"Array practice #2":[
    '''
string[] customers = {"Bob","Sally","Sue"};
var employees = new[] {"Mike","Paul","Rick"};
object[] objectArr = { "Paul", (short)21, 12.4, true };

for (int i = 0; i < objectArr.Length; i++){
    Console.WriteLine("objectArr[{0}] = {1} with the of type {2}", i, objectArr[i], objectArr[i].GetType());
}
    ''',
    ""
],"Array practice #3":[
    '''
string[,] custNames = new string[2, 2] { { "Bob", "Smith" }, { "Sally", "Mike" } };
Console.WriteLine("custNames[1,1] = {0}", custNames.GetValue(1, 1));

for (int i = 0; i < custNames.GetLength(0); i++){
    for (int j = 0; j < custNames.GetLength(1) - 1; j++){
        Console.WriteLine("Row: {0} {1},{2}", i, custNames[i, j], custNames[i, j + 1]);
    }
}
    ''',
    ""
],"foreach loop printing the elements of the array":[
    '''
using System;
using System.Numerics;

namespace FirstProgram
{
    public class Program
    {

        static void PrintArr(int[] arr, string mess)
        {
            Console.WriteLine(mess);
            foreach (int i in arr)
            {
                Console.WriteLine(i);
            }
        }

        public static void Main(string[] args)
        {
            int[] randNum = { 1,3,2,4,5};
            PrintArr(randNum,"foreach loop:");            
        }
    }
}
    ''',
    ""
],"Array practice #4":[
    '''
Array.Sort(randNum);
PrintArr(randNum, "Sorted Array:");
Array.Reverse(randNum);
PrintArr(randNum, "Reversed Array:");
    ''',
    ""
],"Array practice #5":[
    '''
int[] randNums = { 1, 3, 2, 4, 5 };
Console.WriteLine("3 at index: {0}",Array.IndexOf(randNums, 3));

randNums.SetValue(0,2);
for (int i = 0; i < randNums.Length; i++)
{
    Console.WriteLine(randNums[i]);
}
    ''',
    ""
],"Array practice #6":[
    '''
int[] srcArr = { 1, 2, 3 };
int[] destArr = new int[3];
int startInd = 0;
int length = 3;

Array.Copy(srcArr,startInd,destArr,0,length);
PrintArr(srcArr, "Source array");
PrintArr(destArr, "Clone array");

Array anotherArr = Array.CreateInstance(typeof(int),10);
srcArr.CopyTo(anotherArr,5);
foreach (int i in anotherArr)
{
    Console.WriteLine(i);
}
    ''',
    ""
],"Array practice #7":[
    '''
int[] exampleArr = { 1, 11, 22 };
Console.WriteLine("> 10: {0}",Array.Find(exampleArr, num => num > 10));
    ''',
    ""
]}

examples = {"C# code getting the Volume of Sphere":[
    '''
using System;

namespace VolumeOfSphere
{
    public class Program
    {

        public static void Main(string[] args)
        {
           const float Pi = 3.14159F;
           int r = 0;
           int d = 10;
            double V;

            if (r != 0 && d != 0)
            {
                d = 0;
            }

            if (r != 0)
            {
                r = (int)Math.Pow(r, 3);
                V = 4 * r;
                V = V / 3;
                V = V * Pi;
            }
            else if(d != 0)
            {
                r = d / 2;
                r = (int)Math.Pow(r, 3);
                V = 4 * r;
                V = V / 3;
                V = V * Pi;
            }
            else
            {
                V = 0;
            }


           Console.WriteLine($"Volume of Sphere: {V:F1}");
           //Program by Josuan
        }
    }
}
    ''',
    ""
]}