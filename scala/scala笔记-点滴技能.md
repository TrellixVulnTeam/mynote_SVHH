scala笔记-点滴技能

### 单词计数

```Scalascala
object Test extends App {
  val lines = List("qin xuan", "qin he sui", "qin shi ping", "wang yin ping")

  val words = lines.flatMap(x => x.split(" "))
  println(words)
  val tuples = words.map((_, 1))
  println(tuples)
  val grouped = tuples.groupBy(_._1)
  println(grouped)

  val sumed = grouped.mapValues(_.length)
  println(sumed.toList.sortBy(_._2).reverse)
}
```Scala

### for循环条件判断

```Scala
//打印偶数
object Test extends App {
  for (i <- 1 to 20) {
    if (i % 2 == 0) println(i)
  }
}


object Test extends App {
  for (i <- 1 to 20 if i % 2 == 0) {
    println(i)
  }
}

以上两种方法是等价的
```Scala

### stripPrefix和stripSuffix方法

```Scala
object Test extends App{
  val a = "xxxxxx65656565yyyyyy"
  val b = a.stripPrefix("xxxxxx").stripSuffix("yyyyyy")
  println(b)
}

//结果：65656565
```Scala

### replaceAll方法

```Scala
object Test extends App{
  val a = "xxxxxx65656565yyyyyy"
  val b = a.replaceAll("xxxxxx","aaaa")
  println(b)
}
//结果：aaaa65656565yyyyyy
```Scala

### 正则提取

```Scala
import scala.util.matching.Regex

object Test extends App{
  val a = "xxxxxx65656565yyyyyy"
  val pattern = new Regex("[a-zA-z]+")
  println(pattern.findAllIn(a).toList)
}
//结果：List(xxxxxx, yyyyyy)
```Scala

### 数组

1. 若长度固定则使用Array，若长度可能有变化则使用ArrayBuffer

2. 提供初始值时不要使用new

3. 用()来访问元素

4. 用for (elem<-arr)来遍历元素

   ```Scala
   object Test extends App{
     val arr = Array(1,2,3)
     //遍历数组
     for(i<-arr){println(i)}
     //倒序遍历
     for (i<-(0 until (arr.length)).reverse) {println(arr(i))}
   }
   ```Scala

   

```Scala
object Test extends App{
  val arr = Array(1,2,3,4,5,6)
  //用yield的时候条件要写到for里面
  //对数组进行yield要加to才能看到结果
 println((for(n<-arr if n>3) yield n*10).toList)

  println(for (i <- 1 to 20 if  i%2==0 ) yield i)
}
//结果：
List(40, 50, 60)
Vector(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
```Scala

### 用map的时候要注意，比如遇见嵌套的Array就需要使用case来处理

```Scala
object Test extends App{
  val arr = Array(Array("ID:1111","TEL:1233","NAME:ASDF"),Array("ID:1221","TEL:1211","NAME:DFAS"))
  //只取出ID这一项
  val arr2 = arr.map{case Array(x,y,z)=>Array(x)}
  println(arr2.getClass)
  for (i<- arr2) println(i(0))
  val arr3 = Array(Array(1,2,3),Array(4,5,6))
  println(arr3(1)(1))
}

class [[Ljava.lang.String;
ID:1111
ID:1221
5
```Scala

### intersect找出两个集合的交集

```Scala
object Test extends App{
 val a = Array(1,2,3,4,5)
  val b = Array(3,4,6)
  val c = a.intersect(b)
  val d = c.mkString(",")
  println(d)
}
```Scala

### 生成数组

```Scala
1.Array.ofDim[Double](3,4) //生成3*4的二维数组,初始值为0.0
2.Array.ofDim[Double](3) //生成length=3的数组，初始值为0.0
3.Array.emptyDoubleArray() //生成一个泛型为double的空数组
```Scala

### 变长数组

```Scala
import scala.collection.mutable.ArrayBuffer
val b = ArrayBuffer[Int]()
//或者val b = new ArrayBuffer[Int]()
//一个空的数组缓冲，准备存放数组

b += 1
//ArrayBuffer(1),用 += 在尾端添加元素

b += (1, 2, 3, 5)
// ArrayBuffer(1, 1, 2, 3, 5)
//在尾端添加多个元素，以括号包起来

b ++= Array(8, 13, 21)
//ArrayBuffer(1,1,2,3,5,8,13,21)
// 可以用 ++= 操作符追加任何集合
//但是不能 b++= 1 【错误】1不是集合类型

b.trimEnd(5)
//移除最后5个元素
//ArrayBuffer(1,1,2)
```Scala

### 数组转成映射（array转Map）

假设一个场景，一个array中全是字符串，我们需要拿出最长的那个字符串，那么我们可以把这个array转成Map，
 映射表中为（str -> str.length）这种形式。
 那么我们可以先用case转化array为元祖，再用toMap转化成映射。

```Scala
val a = Array("1222","733232","2435345", "9568678")
 val b = a.map{case x => (x,x.length) } 
val c = b.toMap
val d = c.maxBy(_._2)
val e = d._1
```Scala

### 数组合并

```Scala
object Demo01 extends App {
  val arr1 = Array( 1, 2, 3 )
  val arr2 = Array( 4, 5, 6 )
  val arr3 = Array( 7, 8, 9 )
  val arr = Array.concat( arr1, arr2, arr3 )

}
```Scala

### 构建可变映射

```Scala
val res = scala.collection.mutable.Map("a" -> 1, "b" -> 2)
res: scala.collection.mutable.Map[String,Int] = Map(b -> 2, a -> 1)

注：上述代码构建了一个可变的Map[String, Int]，其值可以被改变。Scala可以推导出Map对偶的类型，但是如果为Map()，则会生成一个可变的Map[Nothing, Nothing]
```Scala

### 构建空映射

```Scala
scala> val res = new scala.collection.mutable.HashMap[String, Int]
res: scala.collection.mutable.HashMap[String,Int] = Map()
```Scala

### 添加多个键/值对

```Scala
scala> val map = scala.collection.mutable.Map("a" -> "a", "b" -> "b")
map: scala.collection.mutable.Map[String,String] = Map(b -> b, a -> a)
 
scala> map += ("c" -> "c", "d" -> "d")
res4: map.type = Map(b -> b, d -> d, a -> a, c -> c)
```Scala

### 移除某个键和对应的值

```Scala
scala> val map = scala.collection.mutable.Map("a" -> "a", "b" -> "b")
map: scala.collection.mutable.Map[String,String] = Map(b -> b, a -> a)
 
scala> map -= "b"
res5: map.type = Map(a -> a)
```Scala



### 对不可变map可以进行添加操作，但源map不变，可用新变量接收操作后的map

```Scala
object Test extends App{
val map = Map(("a",1),("b",2))
  val newMap = map + ("c"->3,"d"->4)
  println(map)
  println(newMap)
}
//结果：
Map(a -> 1, b -> 2)
Map(a -> 1, b -> 2, c -> 3, d -> 4)
```Scala

### 迭代映射

如果你想迭代映射，可使用如下结构，即for((k, v) <- 映射) 处理k和v，如

```Scala
object Test extends App {
  val map = Map(("a", 1), ("b", 2))
  for ((k, v) <- map) println(k, v)
  for (k <- map.keySet) println(k)
  for (v <- map.values) println(v)
  val newMap = for((k,v)<-map) yield (v,k)
  println(newMap)
}
//结果
(a,1)
(b,2)
a
b
1
2
Map(1 -> a, 2 -> b)
```Scala

注：如果你想迭代key，则可使用for(k <- map.keySet) ...，如果你想迭代value，则可使用for(v <- map.values) ...，如果你想反转一个映射，则可使用for((k, v) <- 映射) yield (v, k)。