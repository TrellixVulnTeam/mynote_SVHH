scala笔记-类和对象

### 类的属性和定义

```scala
class PersonS {
  //val 修饰的属性，系统会自动生成get方法
  val id:String = "1234"
  //自己定义的get方法
  def getId():String={
    println("haha")
    this.id
  }
  // var 修饰的属性，系统会自动生成get和set方法
  var name:String = ""
  // private var 修饰的属性，系统会自动生成private val 修饰的 get和set方法
  private var gender:Int = 0
  //private[this]修饰的属性，系统不会生成get和set方法
  //只有当前对象可以访问该属性
  private [this] var age:Int = 0

//  def compare(obj:PersonS):Int = {
//    this.age - obj.age
//  }
}

object  test{
  def main(args: Array[String]): Unit = {
    var per:PersonS = new PersonS()
    //使用系统默认的get set方法
    println(per.id)
    per.name = "zhangsan"
    println(per.name)
    //使用自己定义的get方法
    println(per.getId())
  }
}

```

### 构造函数

```scala
//如果构造函数参数声明为val，Scala只为它生成一个getter方法。
class Book (val title:String){

}

object  Main{
  def main(args: Array[String]): Unit = {
    class Book(val title:String)
    val book = new Book("scala")

    println(book)
    println(book.title)
    //book.title = "new title"  //Error

  }
}




//如果构造函数参数声明为var，Scala将生成访问器和mutator方法。
class Book (var title:String){

}

object  Main{
  def main(args: Array[String]): Unit = {
    class Book(var title:String)
    val book = new Book("Beginning scala")
    book.title = "new title"
    println(book)
    println(book.title)
  }
}


//将 private 关键字添加到 val 或 var 字段，以防止getter和setter方法生成。在这种情况下，字段只能从类的成员内访问
class Book (private var title:String){
  def printTitle: Unit ={
    println(title)
  }
}

object  Main{
  def main(args: Array[String]): Unit = {
    val book:Book = new Book("python")
    //println(book.title)   报错
    println(book.printTitle)
  }
}

//当在构造函数参数上未指定val和var时，Scala不生成getter或setter。正如你在这里可以看到的，你不能访问书的字段标题。
class Book (title:String){

}

object  Main{
  def main(args: Array[String]): Unit = {
    val book:Book = new Book("python")
    book.title  //报错
  }
}

//辅助构造函数
我们可以为类定义一个或多个辅助构造函数，以提供创建对象的不同方法。
辅助构造函数通过创建名为this的方法来定义。
class Book (var title:String, var ISBN:Int){
  def this(title:String){
    this(title,2222)
  }
  def this(){
    this("CSS")
    this.ISBN = 1111
  }
}


object Main{
  def main(args: Array[String]): Unit = {
    val book1 = new Book()
    val book2 = new Book("clojure")
    val book3 = new Book("scala",333)
//    println(book2.ISBN)
    println(book1.title)
    println(book1.ISBN)
  }
}
```

###  单例对象

```scala
//单例对象不能带参数，因为不能创建他的实例化
object Logger {
  def log(message:String): Unit ={
    println(s"INFO:$message")
  }

}

class Test{
  def method={
    Logger.log("hello")
  }
}

object LoggerTest{
  def main(args: Array[String]): Unit = {
    Logger.log("haha")
    val obj:Test = new Test
    obj.method
  }
}
```

### 伴生对象

```scala
//类和对象名相同，两者互为伴生对象伴生类，可互相访问彼此的私有属性或者方法
class AccountInfo {

  var id = AccountInfo.newUiqueNumber
}

object  AccountInfo{
  private var lastNumber = 0
  private def newUiqueNumber: Int ={
    lastNumber += 1
    lastNumber
  }
}

object companionTest{
  def main(args: Array[String]): Unit = {
  //后面的括号加不加好像都可以
    var obj:AccountInfo = new AccountInfo()
    println(obj.id)
  }
}
```

### 应用程序对象

```scala
//类和对象名相同，两者互为伴生对象伴生类，可互相访问彼此的私有属性或者方法
class AccountInfo {

  var id = AccountInfo.newUiqueNumber
}

object  AccountInfo{
  private var lastNumber = 0
  private def newUiqueNumber: Int ={
    lastNumber += 1
    lastNumber
  }
}

//应用程序对象
//执行结果和上面的伴生对象一样
object companionTest extends App{
  var obj = new AccountInfo()
  println(obj.id)
}
```

### apply和unapply方法

```scala
class User (val name:String,val password:String) {

}

object User{
  def apply (name:String,password:String) = new User(name,password)

  def unapply(arg: User): Option[(String, String)] = {
    if (arg == null) None
    else{
      Some(arg.name,arg.password)
    }
  }
}
//传统的创建对象方法
//object userTest{
//  def main(args: Array[String]): Unit = {
//    val obj = new User("zhangsan","123456")
//    println(obj.isInstanceOf[User])
//  }
//}
//以下创建对象的方法其实是调用了上面的apply方法
object userTest{
  def main(args: Array[String]): Unit = {
    val obj = User("zhangsan","123456")
    println(obj.isInstanceOf[User])
    //unapply 方法提取对象的参数
    obj match {
      case User(name,password) => println(name+":"+password)
      case _ => println("None")
    }
  }
}
```

### 类的继承

```scala
class Point (val xc:Int,val yc:Int) {
  var x:Int = xc
  var y:Int = yc

  def move(dx:Int,dy:Int) = {
    x = x + dx
    y = y + dy
    println("X的坐标：" + x.toString)
    println("Y的坐标：" + y.toString)
  }
}
//继承了父类的所有属性和方法
//重写父类的非抽象方法，要用override
//重写父类的抽象方法，override可选择
//用final修饰的类不可以被继承
class Location (override val xc:Int,override val yc:Int,val zc:Int) extends Point(xc,yc){
  var z:Int = zc

  def move(dx:Int,dy:Int,dz:Int) = {
    x = x + dx
    y = y + dy
    z = z + dz
    println("X的坐标：" + x.toString)
    println("Y的坐标：" + y.toString)
    println("Z的坐标：" + z.toString)
  }
}


object TestClass{
  def main(args: Array[String]): Unit = {
    val obj1 = new Point(2,3)
    val obj = new Location(5,6,7)
    obj.move(1,2,3)
    //判断对象是不是属于给定的类
    println(obj.isInstanceOf[Location])
    //类型转换
    println(obj.asInstanceOf[Point])
    //获取类的信息
    println(classOf[Location])
  }
}
```

### 抽象类

```scala
abstract class Wangyp {
  //抽象字段，没有初始化值
  var name:String
  //抽象方法：没有方法体的方法
  def id:Int
  //抽象类可以有具体方法
  def simle = {
    println("wangyp is simling")
  }
}

class Qinhesui extends Wangyp {
   override var name:String = "Jerry"
   override def id:Int = {
    name.hashCode
  }

  override def simle: Unit = super.simle
}

object PersonTest{
  def main(args: Array[String]): Unit = {
    val obj = new Qinhesui
    println(obj.name)
    println(obj.id)
    obj.simle

  }
}
```

### 特质

```scala
//定义一个带有抽象方法的特质
 trait Iterator[A]{
  def hasNext:Boolean
  def next:A

}
//定义一个带有实现的特质
trait  ConsoleLogger{
  def log(msg:String) = {
    println(msg)
  }
}
//定义一个类，实现我们的特质  混入多个特质用with
class IntIterator(to:Int) extends Iterator[Int] with ConsoleLogger {
  private var current = 0

  override def hasNext: Boolean = current < to

  override def next: Int = {
    if(hasNext){
      log("has next")
      val t = current
      current += 1
      t
    } else 0
  }
}

object TraitTest {
  def main(args: Array[String]): Unit = {
    val iterator = new IntIterator(10)
    println(iterator.next)

  }
}

```

### 特质的应用

```scala
trait Logger{
  def log(msg:String)
}
//子特质实现父特质里的抽象方法
trait ConsoleLogger extends Logger{
  override def log(msg: String): Unit = println(msg)
}

//给日志加上时间戳
trait TimestampLogger extends ConsoleLogger{
  override def log(msg: String): Unit = super.log(s"${java.time.Instant.now()}$msg")
}
//如果日志过长，对日志截断显示
trait ShortterLoger extends ConsoleLogger{
  val maxLength = 15
  override def log(msg: String): Unit = super.log(
    if(msg.length<= maxLength) msg
    else s"${msg.substring(0,maxLength-3)}..."
  )
}

class Account {
  protected var balance:Double = 0.0
}

class SavingAccount extends Account with ConsoleLogger {
  def withdraw(amount:Double)={
    if(amount > balance) log("Insufficent funds")
    else balance = balance - amount
  }
}
//特质可以为类提供可以堆叠的改变，特质的应用是从混入的最后一个特质依次往前应用
object TraitTest2 {
  def main(args: Array[String]): Unit = {
    var acc1 = new SavingAccount with TimestampLogger
    acc1.withdraw((100.0))
    var acc2 = new SavingAccount with ConsoleLogger with TimestampLogger with ShortterLoger
    acc2.withdraw((100.0))
  }

}

```

### 特质的应用-瘦接口变成胖接口

```scala
trait LoggerQin{
  def log(msg:String)
  def info(msg:String)={
    log("INFO:"+msg)
  }
  def servere(msg:String)={
    log("SEVERE:"+msg)
  }
  def warn(msg:String) = {
    log("WARN:"+msg)
  }
}

class AccountQin{
  protected  var balance:Double = 0

}

class SavingAccountQin extends AccountQin with LoggerQin{
  override def log(msg: String): Unit = println(msg)
  def withdraw(amount:Double) = {
    if(amount > balance) servere("Insufficent funds") else {
      balance = balance - amount
      info ("you withdraw......")
    }
  }
}
object TraitTest3 {
  def main(args: Array[String]): Unit = {
    val acc = new SavingAccountQin
    acc.withdraw(100.0)
  }
}

```

### 样例类

```scala
object CaseclassDemo {
  def main(args: Array[String]): Unit = {
    //定义样例类
    //默认带有apply 方法，所以下面创建对象时不用new
    //构造函数的参数默认是public val修饰的
    case class Message(send:String,recipient:String,body:String)
    //创建一个样例类对象
    val message1 = Message("Jerry","Tom","Hello")
    println(message1.send)
    //message1.send = "kate" //报错，因为构造函数的参数默认是val修饰的，也可以在上面对send修改为var send  但不推荐
  //样例类的比较 基于值或结构比较，而不是基于引用比较
    val message2 = Message("Jerry","Tom","Hello")
    if (message1 == message2) println("same") else println("different")
    //样例类的copy
    val message3 = message1.copy()
    println(message3.send,message3.recipient,message3.body)
    println(message1 == message3)
    //不完全拷贝，对部分参数赋值
    val message4 = message1.copy(send="hanmeimei")
    println(message4.send,message4.recipient,message4.body)
  }

}

```

### 模式匹配

```scala
//字面值匹配
object PatternDemo {
  def main(args: Array[String]): Unit = {
    //常量字面值的匹配
    val site = "qianfeng.com"
    site match {
      case "qianfeng.com" => println("success") //如果有多个模式匹配 只要当前的匹配成功就结束匹配，不需要break语句
      case _=> println("fail")
    }
  }
}

//常量变量的匹配
object PatternDemo {
  def main(args: Array[String]): Unit = {
    //常量变量的匹配
    val site = "qianfeng.com"
    //此处一定要大写
    val QIANFENG = "qianfeng.com"
    site match {
      case QIANFENG => println("success")
      case _=> println("fail")
    }
  }
}

//变量模式的匹配
object PatternDemo {
  def main(args: Array[String]): Unit = {
    //变量的匹配
    val site = "qianfeng.com"
    val qianfeng = "qian.com"
    site match {
      case qianfeng => println(qianfeng + "success") //从这可以看出qianfeng的值为site的值，不管怎么匹配都是成功的
      case _=> println("fail")
    }
  }
}


//通配符模式匹配
object PatternDemo {
  def main(args: Array[String]): Unit = {
    //通配符模式
  val list = List(1,2,3)
    list match {
      case List(_,_,3) => println("success")
      case _ => println("fail")
    }
  }
}
//样例类模式匹配
object PatternDemo {
  def main(args: Array[String]): Unit = {
    //做信息的甄别
    abstract class Notification{

    }
    //定义不同信息的样例类
    case class Email(sender:String,title:String,body:String) extends Notification
    case class SMS(caller:String,message:String) extends Notification
    case class VoiceRecording(contactName:String,link:String) extends Notification

  //做信息的识别
  def showNotification(notification: Notification):String = {
    notification match {
      case Email(sender,title,_) => "you get a email message from" +sender
      case SMS(caller,message) => "you get a SMS message from"+caller
      case VoiceRecording(contactName,link) => "you get a voicerecording message from" +contactName
      case _ =>"you got an message "
    }
  }
    //创建一条信息
    val email = Email("zhangsan","important","sosososo")
    println(showNotification(email))
  }
}


//类型匹配
import scala.util.Random

object PatternDemo {
  def main(args: Array[String]): Unit = {
    //类型匹配
    val arr = Array("sss",1,2,3,'c')
    //随机取数组中的一个元素
    val obj = arr(Random.nextInt(4))
    println(obj)
    obj match {
      case x:Int => println(x)
      case s:String => println(s.toUpperCase)
      case d:Double => println(Int.MaxValue)
      case _ => println("fail")
    }
  }
}

```

### 偏函数

```scala
//使用中规中矩方法定义偏函数
object PartialFunctionDemo {
  //创建一个普通函数
  val div1 = (x:Int) => 100/x

  //定义一个偏函数
  val div2 = new PartialFunction[Int,Int] {
    override def isDefinedAt(x: Int): Boolean = x!=0

    override def apply(x: Int): Int = 100/x
  }

  def main(args: Array[String]): Unit = {
    //div1(0)
    println(div2.isDefinedAt(1))
    div2(1)
    println(div2.isDefinedAt(0))
    div2(0)
  }
}



object PartialFunctionDemo {
//使用case定义偏函数
  val div3:PartialFunction[Int,Int] = {
    case d:Int if(d!=0) => 100/d
  }

  def main(args: Array[String]): Unit = {
    //div1(0)
    println(div3.isDefinedAt(1))
    div3(1)
    println(div3.isDefinedAt(0))
    //div3(0)
  }
}



object PartialFunctionDemo {
//使用case定义偏函数
//[Int,String] 表示传入的参数和返回值的类型
val res:PartialFunction[Int,String] ={
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}

  def main(args: Array[String]): Unit = {
    println(res.isDefinedAt(1))
    println(res.isDefinedAt(2))
    println(res.isDefinedAt(3))
    println(res(1))
  }
}


//使用orElse对多个偏函数进行组合
object PartialFunctionDemo {
  val r1:PartialFunction[Int,String] = {case 1 => "one"}
  val r2:PartialFunction[Int,String] = {case 2 => "two"}
  val r3:PartialFunction[Int,String] = {case _ => "other"}

  val res2 = r1 orElse r2 orElse r3  //相当于上面的res
  def main(args: Array[String]): Unit = {
    println(res2.isDefinedAt(1))
    println(res2.isDefinedAt(2))
    println(res2.isDefinedAt(3))
    println(res2(1))
  }
}


//使用andthen对多个偏函数进行流水线作业
object PartialFunctionDemo {
  val r4:PartialFunction[Int,String] = {case cs if(cs == 1) =>"one"}
  //cs eq "one" 可以写成cs == "one"
  val r5:PartialFunction[String,String] = {case cs if (cs eq "one") => "the number is 1"}
  //下面的:[Int=>String]有没有都可以
  val res3:[Int=>String]  = r4 andThen(r5)
  def main(args: Array[String]): Unit = {
    println(res3(1))
  }
}

```

### 密封类

用seald修饰的类或特质

约束：不能在类定义文件之外定义他的子类

作用1：可以避免滥用集成

作用2：用在模式匹配中

```scala
sealed abstract class Furniture
case class Couch() extends Furniture
case class Chair() extends Furniture

object SealedDemo   {

  def findPlaceToSit(furniture: Furniture):String =
    furniture match {
      case a:Couch => "lie on the couch"
      case b:Chair =>"sit on the chair"
    }
    val chair = Chair()

    def main(args: Array[String]): Unit = {
      println(findPlaceToSit(chair))
    }
  }
```

### 字符串插值器

```scala
object StringDemo {
  def main(args: Array[String]): Unit = {
    //s 字符串插值器
    val name = "jerry"
    val res = s"Hello,$name"
    //对${}中的表达式进行运算
    val res1 = s"1+1=${1+1}"
    println(res)
    println(res1)
    //f 插值器
    val height =1.9d
    val name1 = "tom"
    val res2 = f"$name1 is $height%2.2f meters tall"
    println(res2)
    //raw插值器，类似于s插值器，但不对其中的内容做转换
    val str = s"a\nb"
    println(str)
    val str2 = raw"a\nb"
    println(str2)
  }
}

```

### 文件操作

```scala
import scala.io.Source

object FileDemo extends App {
  //读取文件行
  val source = Source.fromFile("src/filetest.txt")
  //获取文件行迭代器
  val lines = source.getLines()
  for (line<-lines) println(line)
  //关闭源
  source.close()
}

//获取每个字符
import scala.io.Source

object FileDemo extends App {
  //读取文件的字符
  val source = Source.fromFile("src/filetest.txt")
  //获取字符迭代器
  val iter = source.buffered
  var sum = 0
  while (iter.hasNext){
    if(iter.head=='a') {
      sum = sum + 1
    }
    println(iter.next())
  }
  println("sum:" + sum)
  //关闭源
  source.close()
  //
}


//写入文件
import java.io.PrintWriter

object FileDemo extends App {
  //写文件
  val out = new PrintWriter("fileresult.csv")
  for(i<- 1 to 100) out.println(i)
  out.close()

}

```

### 正则表达式

```scala
import scala.util.matching.Regex

object RegDemo extends App{
  //构造正则表达式
  val pattern1 = "[0-9]+".r
  val pattern2 = new Regex("[0-9]+")
  //如果正则表达式中含有斜杠，引号，可以用"""..."""
  val pattern3 = """\s+[0-9]+\s"""

  val matchStr = "99botoles,100bottles"
  //返回一个迭代器
  val a = pattern1.findAllIn(matchStr)
  for (item <- a) println(item)
  //返回首个匹配项
  val first = pattern1.findFirstIn(matchStr)
  println(first)
  //检查字符串的开始部分是不是能匹配
  val ifStartMatch = pattern1.findPrefixOf(matchStr)
  println(ifStartMatch)

  //替换
  //使用传入的字符串替换首个匹配项
  val res1 = pattern1.replaceFirstIn(matchStr,"xxx")
  println(res1)
  //使用传入的字符串替换所有的匹配项
  val res2 = pattern1.replaceAllIn(matchStr,"yyy")
  println(res2)
}

```

### 高阶函数

参数是函数

返回值是函数

参数和返回值都是函数

```scala
object HFunDemo extends App {
  //传入参数是函数
  val arr = Array(1,2,3,4,5)
  val fun = (x:Int)=>x*2
  val res = arr.map(fun)
  //传入匿名函数
  val res1 = arr.map((x:Int)=>x*2)
  val res2 = arr.map(_*2)
  //要打印数组可以用toBuffer方法
  println(res.toBuffer)


  //返回值是函数
  def urlBuilder(ssl:Boolean,domainName:String):(String,String)=>String={
    val schema = if(ssl) "https://" else "http://"
    (endpoint:String,query:String)=>s"$schema$domainName/$endpoint?$query"
  }
  val domainName = "www.1000phone.com"
  def getUrl:(String,String)=>String = urlBuilder(true,domainName)
  val endpoint = "users"
  val query = "id=1"
  val res3 = getUrl(endpoint,query)
  println(res3)
}

```

### 闭包

闭包是一个函数，函数的返回值依赖于函数外部的一个或者多个变量

```scala
object FunDemo1 extends App {
  val multiply = (x:Int) =>x*5


  var factor = 5
  val multiply2 = (x:Int) =>{
    x*factor}
  println(multiply2(10))
  //可以重新给factor赋值，函数的执行结果受外面参数的影响，这种情况就叫闭包
  factor = 10
  println(multiply2(10))
  //函数内对因子做更改
  val multiply3 = (x:Int)=>{
    factor = factor + 10
    x*factor
  }
  //函数尚未执行，因子不变
  println(factor)
  println(multiply3(10))
  //函数执行后，因子变化（+10）
  println(factor)
}

```

### 柯里化

柯里化是把接收多个参数的函数变成接收一个单一参数的函数，返回一个接收余下参数的新函数

```scala
object CurryDemo  extends App {
  //创建一个普通的函数
  def add(x:Int,y:Int) = {x+y}
  println(add(1,2))
  //柯里化后的方法
  def curryAdd(x:Int)(y:Int) = x+y
  println(curryAdd(1)(2))

   //模拟柯里化的实现过程
  def first(x:Int):Int=>Int = (y:Int)=>x+y
  val second = first(1)
  val res = second(2)
  println(res)

  val one = curryAdd(1)_
  println(one(2))
  val two = curryAdd(2)_
  println(two(2))

}

```

### 方法的嵌套和多态

```scala
object Demo{
  def factorial(x:Int):Int = {
    def fact(x:Int,accumulator:Int):Int = {
      if(x<=1) accumulator
      else fact(x-1,x*accumulator)
    }
    fact(x,1)
  }
  def main(args: Array[String]): Unit = {
  println(factorial(3))
  }

  //方法的多态：方法可以通过类型实现参数化,类似泛型

  def listOfDuplicates[A](x:A,length:Int):List[A] = {
    if(length<1) Nil
    else {
//      println(listOfDuplicates(x,length-1))
      x::listOfDuplicates(x,length-1)
    }
  }

  println(listOfDuplicates[Int](3,5))
}
```

