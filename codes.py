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
],"Conditional Statements":[
    '''
int age = 4;

if (age >= 5 && age <= 7){
    Console.WriteLine("Go to Elementary school");
}

if (age > 7 && age < 13){
    Console.WriteLine("Go to middle school");
}

if (age > 13 && age < 19){
    Console.WriteLine("Go to high school");
}
else{
    Console.WriteLine("Go to college");
}

if (age < 14 || age > 67){
    Console.WriteLine("You shouldn't work");
}

Console.WriteLine("!true = " + (!true));

bool canDrive = age >= 16 ? true : false;

switch (age){
    case 1:
    case 2:
        Console.WriteLine("Go to Day Care");
        break;
    case 3:
    case 4:
        Console.WriteLine("Go to Preschool");
        break;
    case 5:
        Console.WriteLine("Go to Kindergarten");
        break;
    default:
        Console.WriteLine("Go to another school");
        goto OtherSchool;
    }

OtherSchool:
    Console.WriteLine("Elementary, Middle, High School");

string name2 = "Derek";
string name3 = "derek";

if (name2.Equals(name3,StringComparison.OrdinalIgnoreCase)){
    Console.WriteLine("Names are equal");
}
else{
    Console.WriteLine("Names are not equal");
}

int num = 21;

if ((num % 2) == 0){
    Console.WriteLine($"num = {num} is even");
}
else if (num == 21){
    Console.WriteLine($"{num} is my birthday");
}
else{
    Console.WriteLine($"num = {num} is odd");
}
    ''',
    "Relational Operators: > < >= <= == !=\nLogical Operatos: && || !"
],"While Loop":[
    '''  
int i = 1;

while (i <= 10){
    if (i % 2 == 0){
        i++;
        continue;
    }
    if (i == 9) break;
    Console.WriteLine(i);
    i++;
} 
    ''',
    ""
],"Do While Loop":[
    '''  
Random rnd = new Random();
int secretNumber = rnd.Next(1,11);
int numberGuessed = 0;

Console.WriteLine("Random Num: {0}",secretNumber);

do{
    Console.WriteLine("Enter a number between 1 to 10: ");
    numberGuessed = Convert.ToInt32(Console.ReadLine());
} while (secretNumber != numberGuessed);

Console.WriteLine("You guessed it it was {0}",secretNumber);
    ''',
    ""
],"Exception Handling":[
    '''  
using System;
using System.Numerics;

namespace FirstProgram
{
    public class Program
    {

        static double DoDivision(double x, double y)
        {
            if (y == 0)
            {
                throw new System.DivideByZeroException();
            }
            return x / y;
        }
        public static void Main(string[] args)
        {
            double num1 = 5;
            double num2 = 0;

            try
            {
                Console.WriteLine("5 / 0 = {0}",DoDivision(num1,num2));
            }
            catch (DivideByZeroException ex)
            {
                Console.WriteLine("You can't divide by zero");
                Console.WriteLine(ex.GetType().Name);
                Console.WriteLine(ex.Message);
            }
            catch (Exception ex)
            {
                Console.WriteLine("An error eccured");
                Console.WriteLine(ex.GetType().Name);
                Console.WriteLine(ex.Message);
            }
            finally
            {
                Console.WriteLine("Cleaning Up");
            }
        }
    }
}
    ''',
    ""
],"StringBuilders":[
    '''  
StringBuilder sb = new StringBuilder("Random Text");

// Create a StringBuilder with a size of 256
StringBuilder sb2 = new StringBuilder("More Stuff that is very important", 256);

// Get max size
Console.WriteLine("Capacity : {0}", sb2.Capacity);

// Get length
Console.WriteLine("Length : {0}", sb2.Length);

// Add text to StringBuilder
sb2.AppendLine("\nMore important text");

// Define culture specific formating
CultureInfo enUS = CultureInfo.CreateSpecificCulture("en-US");

// Append a format string
string bestCust = "Bob Smith";
sb2.AppendFormat(enUS, "Best Customer : {0}", bestCust);
            
// Output StringBuilder
Console.WriteLine(sb2.ToString());

// Replace a string
sb2.Replace("text", "characters");
Console.WriteLine(sb2.ToString());

// Clear a string builder
sb2.Clear();

sb2.Append("Random Text");

// Are objects equal
Console.WriteLine(sb.Equals(sb2));

// Insert at an index
sb2.Insert(11, " that's Great");

Console.WriteLine("Insert : {0}", sb2.ToString());

// Remove number of characters starting at index
sb2.Remove(11, 7);

Console.WriteLine("Remove : {0}", sb2.ToString());
    ''',
    ""
],"Function/Methods #1":[
    '''  
using System;
using System.Numerics;

namespace FirstProgram
{
    public class Program
    {

        private double getSum(double x, double y)
        {
            return x + y;
        }

        private static double getDiff(double x, double y)
        {
            return x - y;
        }

        static void DoubleIt(int x, out int y)
        {
            y = x * 2;
        }

        static void Swap(ref int a, ref int b)
        {
            int temp = a;
            a = b;
            b = temp;
        }

        public double getSumMore(params double[] nums)
        {
            double sum = 0;
            foreach (int i in nums)
            {
                sum += i;
            }
            return sum;
        }

        static void PrintInfo(string name, int zipcode)
        {
            Console.WriteLine($"{name} lives in the zip code {zipcode}");
        }
        public static void Main(string[] args)
        {
            int x = 5, y = 6, result;

            Console.WriteLine("Sum: {0}",new Program().getSum(1,2));
            Console.WriteLine("Difference: {0}", getDiff(x,y));

            DoubleIt(x,out result);
            Console.WriteLine("2x = {0}",result);

            Console.WriteLine("Before swap: x = {0}, y = {1}",x,y);
            Swap(ref x, ref y);
            Console.WriteLine("After swap: x = {0}, y = {1}", x, y);

            double moreSum = new Program().getSumMore(1,2,3,4,5);
            Console.WriteLine($"More sum: {moreSum}");

            PrintInfo(zipcode: 6000, name: "Josuan");
        }
    }
}
    ''',
    ""
],"Method Overloading":[
    '''  
using System;
using System.Numerics;

namespace FirstProgram
{
    public class Program
    {
        static double GetSum2(double x = 1, double y = 1)
        {
            return x + y;
        }

        static double GetSum2(string x = "1", string y = "1")
        {
            double dblX = Convert.ToDouble(x);
            double dblY = Convert.ToDouble(y);
            return dblX + dblY;
        }
        
        public static void Main(string[] args)
        {
            Console.WriteLine(GetSum2(1,2));
            Console.WriteLine(GetSum2("1","2"));
        }
    }
}
    ''',
    ""
],"DateTime":[
    '''  
using System;
using System.Numerics;

namespace FirstProgram
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Used to define dates
            DateTime awesomeDate = new DateTime(1974, 12, 21);
            Console.WriteLine("Day of Week : {0}", awesomeDate.DayOfWeek);

            // You can change values
            awesomeDate = awesomeDate.AddDays(4);
            awesomeDate = awesomeDate.AddMonths(1);
            awesomeDate = awesomeDate.AddYears(1);
            Console.WriteLine("New Date : {0}", awesomeDate.Date);

            // TimeSpan
            // Used to define a time
            TimeSpan lunchTime = new TimeSpan(12, 30, 0);

            // Change values
            lunchTime = lunchTime.Subtract(new TimeSpan(0, 15, 0));
            lunchTime = lunchTime.Add(new TimeSpan(1, 0, 0));
            Console.WriteLine("New Time : {0}", lunchTime.ToString());
        }
    }
}
    ''',
    ""
],"ShapeMath Class":[
    '''  
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_Practice
{
    class ShapeMath
    {
        public static double GetArea(string shape = "",double length1 = 0,double length2 = 0)
        {
            if (String.Equals("Rectangle",shape,StringComparison.OrdinalIgnoreCase))
            {
                return length1 * length2;
            }else if (String.Equals("Triangle", shape, StringComparison.OrdinalIgnoreCase))
            {
                return length1 * (length2 / 2);
            }else if (String.Equals("Circle", shape, StringComparison.OrdinalIgnoreCase))
            {
                return 3.14159 * Math.Pow(length1, 2);
            }
            else
            {
                return -1;
            }
        }
    }
}
    ''',
    ""
],"Animal Class":[
    '''  
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_Practice
{
    class Animal
    {
        public string name;
        public string sound;
        static int numberOfAnimals = 0;
        
        public Animal()
        {
            name = "No Animal";
            sound = "No sound";
            numberOfAnimals++;
        }

        public Animal(string name = "No Animal")
        {
            this.name = name;
            this.sound = "No sound";
            numberOfAnimals++;
        }

        public Animal(string name = "No Animal",string sound = "No sound")
        {
            this.name = name;
            this.sound = sound;
            numberOfAnimals++;
        }

        public void MakeSound()
        {
            Console.WriteLine("{0} says {1}",name,sound);
        }

        public static int GetNumAnimals()
        {
            return numberOfAnimals;
        }
    }
}
    ''',
    ""
],"Class #1 and Struct":[
    '''  
using System;
using System.Numerics;

namespace CSharp_Practice
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Rectangle rect1;
            rect1.lenght = 200;
            rect1.width = 50;

            Console.WriteLine("Area of rect1: {0}", rect1.Area());

            Rectangle rect2 = new Rectangle(100, 40);
            rect2 = rect1;
            rect1.lenght = 33;
            Console.WriteLine("Rect2.length: {0}", rect2.lenght);

            Animal fox = new Animal() { name = "Red",sound = "Raaw"};

            Console.WriteLine("# of Animals: {0}",Animal.GetNumAnimals());
            Console.WriteLine("Area of Rectangle: {0}",ShapeMath.GetArea("circle",5,6));

            int? randNum = null;
            if (randNum == null)
            {
                Console.WriteLine("randNum is null");
            }
            else
            {
                Console.WriteLine("randNum is not null");
            }

            //or

            if (!randNum.HasValue)
            {
                Console.WriteLine("randNum is null");
            }
            else
            {
                Console.WriteLine("randNum is not null");
            }
        }

        struct Rectangle
        {
            public double lenght;
            public double width;

            public Rectangle(double l = 1, double w = 1)
            {
                lenght = l; width = w;
            }

            public double Area()
            {
                return lenght * width;
            }
        }
    }
}
    ''',
    ""
],"Animal Class #2":[
    '''  
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_Practice
{
    class Animal
    {
        private string name;
        private string sound;
        public static int numberOfAnimals = 0;
        public const string SHELTER = "Josuan's Home for Animals";
        public readonly int idNum;

        public Animal() : this("No Name", "No Sound") { }

        public Animal(string name) : this(name,"No Sound") { }

        public Animal(string name, string sound)
        {
            SetName(name);
            Sound = sound;

            NumOfAnimal = 1;
            Random rnd = new Random();
            idNum = rnd.Next(1,234234123);
        }

        public void MakeSound()
        {
            Console.WriteLine("{0} says {1}",name,sound);
        }

        public static int GetNumAnimals()
        {
            return numberOfAnimals;
        }

        public void SetName(string name)
        {
            if (!name.Any(char.IsDigit))
            {
                this.name = name;
            }
            else
            {
                this.name = "No Name";
                Console.WriteLine("Name can't contain numbers");
            }
        }

        public string GetName()
        {
            return name;
        }

        public string Sound
        {
            get { return sound;  }
            set
            {
                if(value.Length > 10)
                {
                    sound = "No Sound";
                    Console.WriteLine("Sound is too long");
                }
                else
                {
                    sound = value;
                }
            }
        }

        public string Owner { get; set; } = "No Owner";

        public static int NumOfAnimal
        {
            get { return numberOfAnimals; }
            set { numberOfAnimals += value; }
        }
    }
}
    ''',
    ""
],"Class #2":[
    '''  
using System;
using System.Numerics;

namespace CSharp_Practice
{
    public class Program
    {
        public static void Main(string[] args)
        {
            Animal cat = new Animal();
            cat.SetName("Whiskers");
            cat.Sound = "Meow";

            Console.WriteLine("The cat is name {0} and says {1}",cat.GetName(),cat.Sound);

            cat.Owner = "Josuan";
            Console.WriteLine("{0} owner is {1}",cat.GetName(),cat.Owner);
            Console.WriteLine("{0} shelder id is {1}", cat.GetName(), cat.idNum);
            Console.WriteLine("Number of Animals: {0}",Animal.NumOfAnimal);
        }
    }
}
    ''',
    ""
]}

"""
,"":[
    '''  

    ''',
    ""
]
"""

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