scala笔记-基础语法

### Scala中定义变量

~~~scala
var 变量名 = 初始化值
var 变量名：数据类型 = 初始化值
~~~

注意：

1、定义变量的时候需要初始化

2、定义变量的时候可以不指定变量的数据类型，系统会根据变量的初始化值推断变量的数据类型

### Scala中定义常量

```scala
val 常量名 = 初始化值
val 常量名：数据类型 = 初始化值
```

注意：

1、val修饰的常量，相对于Java中final修饰的变量

2、val修饰的变量，变量的类型的值类型（相对于Java的基本数据类型，int Double Boolean），值是不可以修改的。

```scala
val a = 10
a = 1000  // 这是不可以的

scala> var a = 10
a: Int = 10

scala> a = 100
mutated a

scala> val a = 10
a: Int = 10

scala> a = 100
         ^
       error: reassignment to val

scala>
```

3、val修饰的变量，变量的类型是引用类型，引用不可变，引用的内容可变

```scala
val a1 = Array(1,2,3)
val a2 = Array(4,5,6)
a1 = a2 //不可以，引用不可变
a1(0) = 10 //可以的，引用的内容可变
```

4、  val修饰的变量，还可以用lazy修饰，在需要使用的时候赋值

```scala
scala> val a = 10
a: Int = 10

scala> lazy val b = 100
b: Int = <lazy>

scala> lazy var c = 10
            ^
       error: lazy not allowed here. Only vals can be lazy

scala> println(a)
10
```

### 生产中定义变量使用val还是var？

官方推荐使用val

1、能使用val的时候尽量使用val

​		使代码可读性更强，因为变量值不会变来变去

​		val修饰的变量值不能改，更安全

​		val修饰的变量在垃圾回收的时候可以更快的被回收

2、定义变量的值在使用过程中需要改变，只能使用var

### 数据类型和操作符

#### 数据类型

1、值类型和引用类型

2、值类型是类类型，没有基本数据类型和包装类之分。

```scala
scala> 1 to 10
res3: scala.collection.immutable.Range.Inclusive = Range 1 to 10

scala> 1.to(10)
res4: scala.collection.immutable.Range.Inclusive = Range 1 to 10
```

#### 操作符

数学运算符：+ - * / %

关系运算符：> >= < <= !

逻辑运算符：&& ||

位运算符：& |  ^

比较对象： ==  !=

1、scala中的运算符都是方法的调用

```scala
scala> 1+1
res6: Int = 2

scala> 1.+(2)
res7: Int = 3
```

2、scala中没有++ --运算符，可以用+=   -=代替

```
scala> a++
        ^
       error: value ++ is not a member of Int

scala> a += 1

scala> a -= 2
```

### 表达式

就是一个语句块，包含一条或者多条语句

特点：

1、表达式是有返回值的

2、返回值是表达式中最后一条语句的执行结果

#### 条件表达式

含有if else的语句块

```scala
scala> val a = 1
a: Int = 1

scala> val res = if(a>0) 100 else -100
res: Int = 100

scala> val res2 = if(a>0) "seccess" else -100
res2: Any = seccess

scala> val res3 = if(a>0) 100
res3: AnyVal = 100

scala> val res4 = if(a<0) 100
res4: AnyVal = ()

scala> val res5 = if(a>0) 100 else if(a<0) -100 else 0
res5: Int = 100

scala> val res6 = if(a<0) 100 else ()
res6: AnyVal = ()
```



#### 块表达式

```scala
scala> val res = {10}
res: Int = 10

scala> val res = {val a = 10
     | val b = 10
     | a+b}
res: Int = 20

scala> val res = {var a = 10
     | a = 20}

scala> println(res)
()

scala> val res = {println("aaa")}
aaa

scala> println(res)
()
```

### 循环

for 

```scala
for (i <- 表达式、数组、集合)
```

```
scala> for (i <- 1 to 10)
     | println(i)
1
2
3
4
5
6
7
8
9
10


scala> for (i <- 1 to 10){println(i)}
1
2
3
4
5
6
7
8
9
10


scala> for (i <- 1 until 10){println(i)}
1
2
3
4
5
6
7
8
9

scala> val s = "scala"
s: String = scala

scala> for (i <- 0 until s.length) println(s(i))
s
c
a
l
a


scala> for (i <- s) println(i)
s
c
a
l
a


scala> for (i <- 0 until s.length) println(s.charAt(i))
s
c
a
l
a
嵌套循环
scala> for (i <- 1 to 3;j<- 1 to 3 if(i != j)) print((10*i+j).toString + " ")
12 13 21 23 31 32
for推导
scala> val res = for(a <- 1 to 10) yield a*10
res: IndexedSeq[Int] = Vector(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
结果相似  但不是range了
scala> val c = for(b <- 1 to 10) print((b*10).toString + " ")
10 20 30 40 50 60 70 80 90 100 c: Unit = ()
```

while

```scala
while (条件语句) {表达式}
```

do while

```scala
do{表达式} while(条件语句)
```

### 方法

定义语法：

```scala
def 方法名(参数列表):返回类型 = 方法体  //返回类型可以省略，但当方法是递归方法时不能省略
```

```
scala> def add(x:Int,y:Int) = x+y
add: (x: Int, y: Int)Int

scala> def add(x:Int,y:Int):Int = x+y
add: (x: Int, y: Int)Int

scala> add(1,2)
res0: Int = 3

scala> add(x=1,y=2)
res1: Int = 3

scala> add(y=2,x=1)
res2: Int = 3

scala> def add(x:Int,y:Int):Unit = {x+y
     | println(x+y)}
add: (x: Int, y: Int)Unit

scala> add(1,2)
3
```

#### 带有参数列表的方法

~~~scala
scala> def addAndMultiply(x:Int,y:Int,z:Int) = (x+y)*z
addAndMultiply: (x: Int, y: Int, z: Int)Int

scala> def addAndMultiply(x:Int,y:Int)(z:Int) = (x+y)*z
addAndMultiply: (x: Int, y: Int)(z: Int)Int

scala> def addAndMultiply(x:Int)(y:Int)(z:Int) = (x+y)*z
addAndMultiply: (x: Int)(y: Int)(z: Int)Int

scala> addAndMultiply(3)(4)(5)
res5: Int = 35

scala>  
~~~

#### 无参方法

~~~scala
scala> def printInfo = println("I love scala")
printInfo: Unit

scala> printInfo
I love scala

scala> printInfo()
                ^
       error: Unit does not take parameters

scala>                             
~~~



~~~scala
scala> def printInfo() = println("I love scala")
printInfo: ()Unit

scala> printInfo
I love scala

scala> printInfo()
I love scala

scala>                   
~~~



定义无参方法没有带括号时调用无参方法不能加括号

定义无参方法带括号时调用无参方法加不加括号都行

#### 带有默认值参数的方法

```scala
scala> def add(a:Int = 1,b:Int,c:Int =3) = println("a=" + a + " b=" +b + " c=" + c)
add: (a: Int, b: Int, c: Int)Unit

scala> add(1,2)
a=1 b=2 c=3

scala> add(b=2)
a=1 b=2 c=3

scala> add(1,2,3)
a=1 b=2 c=3

scala> add(1)
          ^
       error: not enough arguments for method add: (a: Int, b: Int, c: Int)Unit.
       Unspecified value parameter b.
```

#### 可变长参数方法

```scala
scala> def add(a:Int*)={
     | for(i <- a)
     | println(a)}
add: (a: Int*)Unit

scala> add(1)
ArraySeq(1)

scala> add(1,2,3,4)
ArraySeq(1, 2, 3, 4)
ArraySeq(1, 2, 3, 4)
ArraySeq(1, 2, 3, 4)
ArraySeq(1, 2, 3, 4)
```

### 函数

```scala
scala> (x:Int,y:Int) => x+y
res0: (Int, Int) => Int = $$Lambda$775/901751227@6b321262

scala> res0(1,2)
res1: Int = 3

scala> val fun = (x:Int,y:Int) => x+y
fun: (Int, Int) => Int = $$Lambda$789/1703254852@d9f5fce

scala> fun(3,4)
res2: Int = 7

scala> val fun = ((x:Int,y:Int)=>x+y)
fun: (Int, Int) => Int = $$Lambda$790/2050791921@16b7e04a

scala> val fun = (_:Int)+(_:Int)
fun: (Int, Int) => Int = $$Lambda$791/602529144@470c4229

scala> val fun:(Int,Int)=>Int = (_+_)
fun: (Int, Int) => Int = $$Lambda$805/126426355@6bfbab1c

scala> val fun:(Int,Int)=>Int=(x,y)=>x+y
fun: (Int, Int) => Int = $$Lambda$806/2014166743@31859960
```

#### 无参函数

```scala
scala> val fun1 = ()=>println("haha")
fun1: () => Unit = $$Lambda$807/1059781259@6b2efcae

scala> fun1
res4: () => Unit = $$Lambda$807/1059781259@6b2efcae

scala> fun1()
haha
```

#### 多参数函数

```scala
scala> val fun2 = (x:Int,y:Int)=>x*y
fun2: (Int, Int) => Int = $$Lambda$813/281110571@2cf97875

scala> fun2(1,5)
res6: Int = 5

scala>                                                                                                                             
```

### 方法和函数

#### 区别：

1、方法和函数的定义语法不同

2、方法一般定义在类、特质、或者object中

3、方法可以共享所在类、特质、或者object中的属性

4、可以调用函数，也可以存放到一个变量中，作为参数传递给其他的方法或者函数，也可以作为返回值

#### 联系：

1、可以把函数作为参数传递给一个方法

```scala
scala> def m(f:(Int,Int)=>Int) = f(5,1)
m: (f: (Int, Int) => Int)Int

scala> val f = (x:Int,y:Int)=>x-y
f: (Int, Int) => Int = $$Lambda$777/1157856790@2f2e4bde

scala> m(f)
res0: Int = 4
```

2、方法可以转换函数

```scala
scala> def m(f:(Int,Int)=>Int) = f(5,1)
m: (f: (Int, Int) => Int)Int

scala> def m2(x:Int,y:Int) = x-y
m2: (x: Int, y: Int)Int
//把方法传递给另一个方法时，该方法会自动转换为函数
scala> m(m2)
res2: Int = 4
//使用空格下划线的方法也可以把一个方法转换成一个函数
scala> m2 _
res3: (Int, Int) => Int = $$Lambda$822/1958731110@6fc7e828

scala> m(m2 _)
res4: Int = 4
```

### 集合

不可变集合：不可以修改，但是可以模拟修改或删除等

可变集合：可修改，可以更新或扩充

集合三大类：

set sque map

#### 定长数组

##### 数组的定义

```scala
scala> val arr = Array(1,2,3)
arr: Array[Int] = Array(1, 2, 3)

scala> val arr1 = Array[Int](4,5,6)
arr1: Array[Int] = Array(4, 5, 6)

scala> val arr2 = new Array[Int](10)
arr2: Array[Int] = Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

scala> val arr2 = new Array[Int](10,20,30)
                                    ^
       error: too many arguments (3) for constructor Array: (_length: Int)Array[Int]
//这种方式定义数组如果不指定数据类型，则定义的数组无法访问，无法放入数据。
scala> val arr3 = new Array(10)
arr3: Array[Nothing] = Array(null, null, null, null, null, null, null, null, null, null)

scala> arr3(0)
java.lang.NullPointerException
  at .$print$lzycompute(<synthetic>:8)
  ... 26 elided
```



##### 数组的访问和常用方法

```scala
scala> val arr1 = Array[Int](4,5,6)
arr1: Array[Int] = Array(4, 5, 6)

scala> arr1.length
res6: Int = 3

scala> arr1(0)
res7: Int = 4

scala> arr1(0) = 7

scala> arr1
res9: Array[Int] = Array(7, 5, 6)

scala> arr1.sum
res10: Int = 18

scala> arr1.max
res12: Int = 7

scala> arr1.min
res13: Int = 5

scala> arr1.sorted
res14: Array[Int] = Array(5, 6, 7)

scala> arr1.sorted.reverse
res18: Array[Int] = Array(7, 6, 5)
```

#### 变长数组

##### 变长数组的创建

```scala
scala> import scala.collection.mutable.ArrayBuffer
ArrayBuffer   ArrayBufferView

scala> import scala.collection.mutable.ArrayBuffer
import scala.collection.mutable.ArrayBuffer

scala> var arr1 = ArrayBuffer("a","b")
arr1: scala.collection.mutable.ArrayBuffer[String] = ArrayBuffer(a, b)

scala> var arr2 = new ArrayBuffer[Int](10)  //创建变长数组后面的10是没有意义的，可以不写
arr2: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer()

scala> arr2.length
res0: Int = 0

scala> var arr2 = new ArrayBuffer[Int]()
arr2: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer()
```

##### 数组的操作

```scala
scala> var arr2 = ArrayBuffer[Int]() //定义数组时数组类型不能少
arr2: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer()

scala> arr2.append(1)
res32: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1)
scala> val arr3 = Array(2,3)
arr3: Array[Int] = Array(2, 3)

scala> arr2.appendAll(arr3)
res33: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1, 2, 3)

scala> val arr4 = Array(4,5)
arr4: Array[Int] = Array(4, 5)

scala> arr2.addAll(arr4)  //感觉addAll和appendAll的参数只要是集合都可以
res34: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4, 5)

scala> arr2+=6
res35: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1, 2, 3, 4, 5, 6)

scala> arr2.insert(2,100)

scala> arr2
res37: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1, 2, 100, 3, 4, 5, 6)

scala> arr2 -= 1  //如果数组中有多个1  它会找到第一个1 删除
res38: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(2, 100, 3, 4, 5, 6)

scala> arr2.trimEnd(2) //删除最后面2个

scala> arr2
res42: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(2, 100, 3, 4)

scala> arr2.remove(2,2) 第一个参数是索引的位置，第二个参数是要删除的元素个数

scala> arr2
res44: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(2, 100)
```

##### 练习：数组中的正负数分开

```scala
scala> var a1 = Array(1,2,-6,-8,4,5,-2,33)
a1: Array[Int] = Array(1, 2, -6, -8, 4, 5, -2, 33)

scala> var a2 = new ArrayBuffer[Int]()
a2: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer()

scala> var a3 = new ArrayBuffer[Int]()
a3: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer()
//注意for循环中的（）不能丢
scala> for (e<-a1){
     | if (e>0) a2.append(e)
     | else a3.append(e)
     | }

scala> a2
res46: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1, 2, 4, 5, 33)

scala> a3
res47: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(-6, -8, -2)

scala> a2.addAll(a3)
res48: scala.collection.mutable.ArrayBuffer[Int] = ArrayBuffer(1, 2, 4, 5, 33, -6, -8, -2)
```

##### 数组的变换

```scala
scala>  val a = Array(1,2,3,4,5)
a: Array[Int] = Array(1, 2, 3, 4, 5)

scala> for (e<-a)yield e*10
res4: Array[Int] = Array(10, 20, 30, 40, 50)

scala> a.map(_*10)
res5: Array[Int] = Array(10, 20, 30, 40, 50)

scala> a.map(x=>x*10)
res6: Array[Int] = Array(10, 20, 30, 40, 50)

scala> a.filter(_%2 == 0)
res7: Array[Int] = Array(2, 4)

scala> a.filter(x=>x%2== 0)
res8: Array[Int] = Array(2, 4)
```

#### List

##### 不可变list创建以及操作

```scala
scala> val list1 = List(1,2,3)
list1: List[Int] = List(1, 2, 3)

scala> println(list1.getClass.getName)
scala.collection.immutable.$colon$colon

scala> 0::list1   //在list1头部插入  但list1本身没有变化
res10: List[Int] = List(0, 1, 2, 3)

scala> list1
res11: List[Int] = List(1, 2, 3)

//以下三种操作效果一样
scala> list1.::(0)
res14: List[Int] = List(0, 1, 2, 3)

scala> 0 +: list1
res15: List[Int] = List(0, 1, 2, 3)

scala> list1.+:(0)
res16: List[Int] = List(0, 1, 2, 3)
//在尾部插入
scala> list1 :+ 4
res17: List[Int] = List(1, 2, 3, 4)

scala> val list2 = List(4,5,6)
list2: List[Int] = List(4, 5, 6)

scala> list1 ++: list2
res18: List[Int] = List(1, 2, 3, 4, 5, 6)
```

##### 可变list创建以及操作

```scala
scala> import scala.collection.mutable.ListBuffer
import scala.collection.mutable.ListBuffer

scala> var list3 = ListBuffer(1,2,3)
list3: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3)

scala> list3 += 4
res19: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4)

scala> list3
res20: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4)

scala> list3.append(5)
res21: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4, 5)

scala> list3
res22: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4, 5)

scala> var list4 = new ListBuffer[Int]()
list4: scala.collection.mutable.ListBuffer[Int] = ListBuffer()

scala> list4.append(9)
res23: scala.collection.mutable.ListBuffer[Int] = ListBuffer(9)

scala> list3 ++ list4
res24: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4, 5, 9)

scala> list3
res25: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4, 5)

scala> list4
res26: scala.collection.mutable.ListBuffer[Int] = ListBuffer(9)

scala> list3 :+ 8
res27: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4, 5, 8)

scala> list3
res28: scala.collection.mutable.ListBuffer[Int] = ListBuffer(1, 2, 3, 4, 5)
```

##### list的转换

```scala
scala> list3.map(_*10)
res29: scala.collection.mutable.ListBuffer[Int] = ListBuffer(10, 20, 30, 40, 50)

scala> list3.map(e=>e*10)
res30: scala.collection.mutable.ListBuffer[Int] = ListBuffer(10, 20, 30, 40, 50)

scala> list3.map(println("hello");_*10)
                                 ^
       error: ')' expected but ';' found.
                                      ^
       error: ';' expected but ')' found.
//注意以下两种方式生成结果的不同
scala> list3.map{println("hello");_*10}
hello
res31: scala.collection.mutable.ListBuffer[Int] = ListBuffer(10, 20, 30, 40, 50)

scala> list3.map{e=>println("hello");e*10}
hello
hello
hello
hello
hello
res32: scala.collection.mutable.ListBuffer[Int] = ListBuffer(10, 20, 30, 40, 50)
```

#### map

##### 创建map

```scala
//创建不可变map，以下两种方法都可以
scala> val score = Map("zhangsan"->90,"lisi"->80)
score: scala.collection.immutable.Map[String,Int] = Map(zhangsan -> 90, lisi -> 80)

scala> val score = Map(("zhangsan",90),("lisi",80))
score: scala.collection.immutable.Map[String,Int] = Map(zhangsan -> 90, lisi -> 80)
//以下为创建可变map
scala> import scala.collection.mutable.Map
import scala.collection.mutable.Map

scala> val score = Map(("zhangsan",90),("lisi",80))
score: scala.collection.mutable.Map[String,Int] = HashMap(zhangsan -> 90, lisi -> 80)
//也可以不导入包，直接创建
scala> val score = scala.collection.mutable.Map("zhangsan"->95,"lisi"->100)
score: scala.collection.mutable.Map[String,Int] = HashMap(zhangsan -> 95, lisi -> 100)
```

##### 基本操作

```scala
scala> score("zhangsan")
res0: Int = 95
//这种方法取值如果没有这个key会报错
scala> score("zhang")
java.util.NoSuchElementException: key not found: zhang
  at scala.collection.MapOps.default(Map.scala:244)
  at scala.collection.MapOps.default$(Map.scala:243)
  at scala.collection.AbstractMap.default(Map.scala:375)
  at scala.collection.mutable.HashMap.apply(HashMap.scala:355)
  ... 28 elided
//可通过判断方式取值
scala> if(score.contains("zhang")) score("zhang") else -1
res2: Int = -1
//最常用的是这种方法
scala> score.getOrElse("zhang",-2)
res3: Int = -2

scala> score.getOrElse("zhangsan",-2)
res4: Int = 95

scala> score.isEmpty
res5: Boolean = false

scala> score.keys
res6: Iterable[String] = Set(zhangsan, lisi)
//注意该方法
scala> score.values
res7: Iterable[Int] = View(<not computed>)

scala> val v = score.values
v: Iterable[Int] = View(<not computed>)
//可以对上面的结果在进行操作
scala> v map(_+1)
res10: Iterable[Int] = View(<not computed>)
//想要取出里面的值可以用以下方法
scala> res10.to(List)
res11: List[Int] = List(96, 101)

scala> res10.to(Vector)
res12: scala.collection.immutable.Vector[Int] = Vector(96, 101)

scala> res10.to(Array)
res13: Array[Int] = Array(96, 101)
```

##### 其他

```scala
scala> score
res14: scala.collection.mutable.Map[String,Int] = HashMap(zhangsan -> 95, lisi -> 100)

scala> score("zhangsan")=60

scala> score
res16: scala.collection.mutable.Map[String,Int] = HashMap(zhangsan -> 60, lisi -> 100)
//当key值没有的时候不会报错，会新增加成员
scala> score("zhang")=90

scala> score
res18: scala.collection.mutable.Map[String,Int] = HashMap(zhangsan -> 60, lisi -> 100, zhang -> 90)

scala> score += ("zhaowu"->99)
res19: score.type = HashMap(zhangsan -> 60, lisi -> 100, zhang -> 90, zhaowu -> 99)
//这种方式新增成员报错，因为他把zhao 和 99都当作key了
scala> score += ("zhao",99)
                 ^
       error: type mismatch;
        found   : String("zhao")
        required: (String, Int)
                        ^
       error: type mismatch;
        found   : Int(99)
        required: (String, Int)

scala> score += (("zhao",99))
res21: score.type = HashMap(zhangsan -> 60, lisi -> 100, zhang -> 90, zhaowu -> 99, zhao -> 99)
//这种方式新版本已弃用
scala> score += (("zh1",99),("zh2",80))
             ^
       warning: method += in trait Growable is deprecated (since 2.13.0): Use `++=` (addAll) instead of varargs `+=`
res22: score.type = HashMap(lisi -> 100, zh1 -> 99, zh2 -> 80, zhao -> 99, zhangsan -> 60, zhang -> 90, zhaowu -> 99)

//可以用这种方式添加多个成员
scala> val a = Map(("zh3",99),("zh4",80))
a: scala.collection.mutable.Map[String,Int] = HashMap(zh3 -> 99, zh4 -> 80)

scala> score.addAll(a)
res26: score.type = HashMap(lisi -> 100, zh1 -> 99, zh3 -> 99, zh2 -> 80, zhao -> 99, zh4 -> 80, zhangsan -> 60, zhang -> 90, zhaowu -> 99)
//成员的删除
scala> score -= "zh1"
res27: score.type = HashMap(lisi -> 100, zh3 -> 99, zh2 -> 80, zhao -> 99, zh4 -> 80, zhangsan -> 60, zhang -> 90, zhaowu -> 99)

//成员遍历
scala> for ((k,v)<- score) println (k+":"+v)
lisi:100
zh3:99
zh2:80
zhao:99
zh4:80
zhangsan:60
zhang:90
zhaowu:99
```

#### 元组

##### 元组的创建

```scala
scala> val t1 = (1,2,3,4)
t1: (Int, Int, Int, Int) = (1,2,3,4)
//元组内的元素可以不同类型
scala> val t2 = ("java","scala",1)
t2: (String, String, Int) = (java,scala,1)
//元组成员访问从1开始
scala> t2._1
res30: String = java

scala> t2._2
res31: String = scala

scala> t2._3
res32: Int = 1
//元组的值不能改变
scala> t2._3 = 2
             ^
       error: reassignment to val

scala> var t3 = ("java","scala",1)
t3: (String, String, Int) = (java,scala,1)

scala> t3._3
res33: Int = 1

scala> t3._3 = 2
             ^
       error: reassignment to val
//这种创建元组的好处是可以用abc变量来取对应的值
scala> val t4,(a,b,c)=("qianfeng","edu",1)
t4: (String, String, Int) = (qianfeng,edu,1)
a: String = qianfeng
b: String = edu
c: Int = 1

scala> a
res34: String = qianfeng

scala> b
res35: String = edu

scala> t4
res36: (String, String, Int) = (qianfeng,edu,1)


scala> val t5 = new Tuple
Tuple1    Tuple11   Tuple13   Tuple15   Tuple17   Tuple19   Tuple20   Tuple22   Tuple4   Tuple6   Tuple8
Tuple10   Tuple12   Tuple14   Tuple16   Tuple18   Tuple2    Tuple21   Tuple3    Tuple5   Tuple7   Tuple9
//Tuple3代表可以创建3个元素的元组，最长支持22个
scala> val t5 = new Tuple3("qianfeng","dashuju",1)
t5: (String, String, Int) = (qianfeng,dashuju,1)
```

##### 元组的遍历

```scala
scala> val t5 = new Tuple3("qianfeng","dashuju",1)
t5: (String, String, Int) = (qianfeng,dashuju,1)
//以下两种方式都可以遍历元组的成员
scala> t5.productIterator.foreach(i=>println(i))
qianfeng
dashuju
1

scala> t5.productIterator.foreach(println(_))
qianfeng
dashuju
1
```

##### 拉链操作

```scala
scala> val a1 = Array("Java","scala","python")
a1: Array[String] = Array(Java, scala, python)

scala> val a2 = Array(1,2,3)
a2: Array[Int] = Array(1, 2, 3)

scala> a1.zip(a2)
res39: Array[(String, Int)] = Array((Java,1), (scala,2), (python,3))

scala> val a3 = Array(4,5,6,7)
a3: Array[Int] = Array(4, 5, 6, 7)

scala> a1.zip(a3)
res40: Array[(String, Int)] = Array((Java,4), (scala,5), (python,6))
//使用这种方式需要提供默认值来和多余的元素匹配
scala> a1.zipAll(a3)
                ^
       error: not enough arguments for method zipAll: (that: Iterable[B], thisElem: A1, thatElem: B)Array[(A1, B)].
       Unspecified value parameters thisElem, thatElem.

scala> val x = "a"
x: String = a

scala> val y = 0
y: Int = 0

scala> a1.zipAll(a3,x,y)
res42: Array[(String, Int)] = Array((Java,4), (scala,5), (python,6), (a,7))
//拉链操作的逆操作
scala> val res = a1.zipAll(a3,x,y)
res: Array[(String, Int)] = Array((Java,4), (scala,5), (python,6), (a,7))

scala> res.unzip
res43: (Array[String], Array[Int]) = (Array(Java, scala, python, a),Array(4, 5, 6, 7))
```

#### set

##### 特点

set中的元素是不允许重复的

set中的元素是无序随机的

##### 创建set

```scala
//创建不可变set
scala> val set1 = Set(1,2,3)
set1: scala.collection.immutable.Set[Int] = Set(1, 2, 3)
//不可变set的操作不会改变set本身
scala> set1 + 4
res58: scala.collection.immutable.Set[Int] = Set(1, 2, 3, 4)

scala> set1
res59: scala.collection.immutable.Set[Int] = Set(1, 2, 3)

scala> set1 - 3
res60: scala.collection.immutable.Set[Int] = Set(1, 2)

scala> set1
res61: scala.collection.immutable.Set[Int] = Set(1, 2, 3)
//导包创建可变set
scala> import scala.collection.mutable.Set
import scala.collection.mutable.Set

scala> val set2 = Set(1,2,3)
set2: scala.collection.mutable.Set[Int] = HashSet(1, 2, 3)

scala> set2 += 4
res62: set2.type = HashSet(1, 2, 3, 4)

scala> set2
res63: scala.collection.mutable.Set[Int] = HashSet(1, 2, 3, 4)
//注意这种操作方法只能操作不可变set
scala> set2 - 3
            ^
       warning: method - in trait SetOps is deprecated (since 2.13.0): Consider requiring an immutable Set or fall back to Set.diff
res64: scala.collection.mutable.Set[Int] = HashSet(1, 2, 4)

scala> set2
res65: scala.collection.mutable.Set[Int] = HashSet(1, 2, 3, 4)
//追加重复元素  set不变
scala> set2 += 2
res68: set2.type = HashSet(1, 2, 4)
```

##### 基本操作

```scala
//返回set的第一个元素
scala> set2.head
res69: Int = 1
//返回set除第一个元素外的其他元素
scala> set2.tail
res70: scala.collection.mutable.Set[Int] = HashSet(2, 4)

scala> set2.isEmpty
res72: Boolean = false

scala> set2.max
res73: Int = 4
//两个set 的连接
scala> val set3 = Set(3,4,5,6)
set3: scala.collection.mutable.Set[Int] = HashSet(3, 4, 5, 6)

scala> set2
res74: scala.collection.mutable.Set[Int] = HashSet(1, 2, 4)
//生成新的set且去除重复值  源set不变
scala> set2 ++ set3
res75: scala.collection.mutable.Set[Int] = HashSet(1, 2, 3, 4, 5, 6)
//取出两个set的公共元素
scala> set2.intersect(set3)
res77: scala.collection.mutable.Set[Int] = HashSet(4)
```

#### 集合函数

```scala
scala> val list1 = List(2,3,4,5,6,7)
list1: List[Int] = List(2, 3, 4, 5, 6, 7)

scala> list1.sum
res78: Int = 27

scala> list1.max
res79: Int = 7

scala> list1.min
res80: Int = 2

scala> list1.filter(e=>e%2==0)
res81: List[Int] = List(2, 4, 6)
//flatten 对集合的集合进行脱壳处理
scala> val list2 = List(5,6,7)
list2: List[Int] = List(5, 6, 7)

scala> val list3 = List(list1,list2)
list3: List[List[Int]] = List(List(2, 3, 4, 5, 6, 7), List(5, 6, 7))

scala> list3.flatten
res82: List[Int] = List(2, 3, 4, 5, 6, 7, 5, 6, 7)

//flatten map
scala> val list4 = List('a','b','c')
list4: List[Char] = List(a, b, c)

scala> val list5 = list4.map(ch=>List(ch,ch.toUpper))
list5: List[List[Char]] = List(List(a, A), List(b, B), List(c, C))

scala> list5.flatten
res85: List[Char] = List(a, A, b, B, c, C)
//以下方法相当于上面的两步实现结果
scala> val list6 = list4.flatMap(ch=>List(ch,ch.toUpper))
list6: List[Char] = List(a, A, b, B, c, C)

//forall和foreach
scala> list1
res86: List[Int] = List(2, 3, 4, 5, 6, 7)

scala> list1.forall(e=>e>0)
res87: Boolean = true

scala> list1.foreach(println)
2
3
4
5
6
7

//reduceLeft reduceRight foldLeft foldRight用法
scala> list1
res90: List[Int] = List(2, 3, 4, 5, 6, 7)

scala> list1.reduceLeft(_+_)
res91: Int = 27

scala> list1.reduceRight(_+_)
res92: Int = 27

scala> list1.reduceRight(_-_)
res93: Int = -3

scala> list1.reduceLeft(_-_)
res94: Int = -23

scala> list1.foldLeft(0)(_+_)
res95: Int = 27

scala> list1.foldLeft(10)(_+_)
res96: Int = 37
```

