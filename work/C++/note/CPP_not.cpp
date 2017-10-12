//different ways to access the variables and functions in a class/struct

class Aclass {
public:
  static int static_field;
  int instance_field;

  static void static_method();
  void method(/* arguments */);
};

Aclass instance;
Aclass *pointer = new Aclass();

instance.instance_field;
instance.method();

pointer->instance_field;
pointer->method();

Aclass::static_field;
Aclass::static_method();

//namespace 命名空间的需求

/*1.某文件中定义两个类，在进行调用时加上类名，作为限定：*/
void A::fun1();
void B::fun2();
/*2.global variables 全局变量，两文件A,B中有同名变量，同时调用两文件时，会出现赋值错误；使extern 扩展变量的作用域*/
file A: 
int a = 0;
file B:
extern int a; 
/*3.引用命名空间中的成员，可用命名空间对成员进行限定。*/
namespace tv 
{ int a =0;
}
tv::a =1 ;
/*4.标准命名空间std,标准C++库的所有的标识符都是在一个名为std的命名空间中定义的，或者说标准头文件(如iostream)中函数、类、对象和类模板是在命名空间 std中定义的。*/
std::cout<<"OK"<<'\n';


// & 符号的应用
int a=3；
int b[5];
int &b=a；    /*1.引用*/
int *p=&a;    /*2.取地址*/
int *p=b;


17.08.17
1.char** argv 
//char**  a pointer to a poniter of char,
/*Char **argv:
As you already noticed the variable is pointer to pointer. Argv points to a character pointer. When you pass Argument in command line each Argument interpreted as string. String is a character array. Argv hold the base address of each character array(argumnet string).
You can access each string by index number.
argv[argc-1] is the last element.*/

2.'a',"abc"
//'a' 是一个字符，charater, char a 
//  "abc" 是一个字符串 character array char a[]
注意与array 数组的概念结合：
double a[] = {1,2,3,4,5,6};
https://www.tutorialspoint.com/cplusplus/cpp_arrays.htm

3.char a[] 与string a 
//上述均为字符串的表达方式， C 与C++ 的区别
//char a[4][10]: 4个长度为10的字符串
//string a[4]： 4个长度不定的字符串
https://www.tutorialspoint.com/cplusplus/cpp_strings.htm

4.注意 ++i 与 i++的区别 
加发运算与操作的先后顺序，以及左右值的区分

170823
1.class constructor & destructor 类的构造与析构
https://www.tutorialspoint.com/cplusplus/cpp_constructor_destructor.htm
注意类构造类时的含参构造方法

