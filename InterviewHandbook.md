# Interview Handbook
We hope it helps us to prepare for the **ASP.Net Core Developer** interview in a short time :)

### Table of Contents
**[OOP Concepts](#oop-concepts)**<br>
**[Git Essentials](#git-essentials)**<br>
**[Concurrency and Parallelism In Depth](#concurrency-and-parallelism-in-depth)**<br>
**[Testing in Dotnet](#testing-in-dotnet)**<br>
**[Design Patterns](#design-patterns)**<br>
**[Design Principals](#design-principals)**<br>
**[Relational Databeses](#relational-databeses)**<br>
**[NoSql](#nosql)**<br>
**[Caching](#caching)**<br>
**[Logging](#logging)**<br>
**[Identity](#identity)**<br>
**[IOC](#ioc)**<br>
**[Observability and Monitoring](#observability-and-monitoring)**<br>
**[system Design and Architecture](#system-design-and-architecture)**<br>
**[AWS Cloud](#aws-cloud)**<br>




## OOP Concepts
### Summary
Object oriented programming generally support **4 types of relationships**, which include **inheritance**, **association**, **composition**, and **aggregation**.
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/RelationsInOOP.png?raw=true).

<br>**1. Inheritance**: (is-a)
Inheritance is “IS-A” type of relationship. “IS-A” relationship is a totally based on Inheritance, which can be of two types Class Inheritance or Interface Inheritance. Inheritance is a parent-child relationship where we create a new class by using existing class code. It is just like saying that “A is type of B”. For example is “Apple is a fruit”, “Ferrari is a car”.

<br>**2. Composition**: (part-of _ Is composed of another object and when BMW dies so Engine dies)
Composition is a "part-of" relationship. Simply composition means mean use of instance variables that are references to other objects. In composition relationship both entities are interdependent of each other for example “engine is part of car”, “heart is part of body”.
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/composition.jpg?raw=true).

<br>Example of Inheritance and Composition

```csharp
    public class BMW : Car // ******Inheritance (BMW is a Car)******
    {
        public Engine Engine { get; set; } // ******Composition (Engine part of BMW)******

        public void Info()
        {
             Console.WriteLine($"{Color} BMW {ModelName}, Engine:{Engine.Name}," +
                $" MaxSpeed: {Engine.MaxSpeed} km, Power: {Engine.Power} horsepower");
        }
    }
```

<br>**3. Association**: (has-a)

Association is a “has-a” type relationship. Association establish the relationship b/w two classes using through their objects. Association relationship can be one to one, One to many, many to one and many to many. For example suppose we have two classes then these two classes are said to be “has-a” relationship if both of these entities share each other’s object for some work and at the same time they can exists without each others dependency or both have their **own life time**.


<br>Example
```csharp
class Employee
{
    public string EmployeeName { get; set; }
    public void ManagerInfo(Manager manager) // *****Employee HAS-A Manager*****
    {
        manager.Info(this);
    }
}
class Manager
{
    public string ManagerName { get; set; }
    public void Info(Employee employee) // *****Manager HAS-A Employee*****
    {
        Console.WriteLine($"Manager of Employee {employee.EmployeeName} is {this.ManagerName}");
    }
}
```


<br>**4. Aggregation** (has-a. It has an existing object of another type)

Aggregation is based is on "has-a" relationship. Aggregation is a special form of association. **In association there is not any classes (entity) work as owner but in aggregation one entity work as owner**. In aggregation both entities meet for some work and then get separated. **Aggregation is a one way association**.

Example
Let us take an example of “Student” and “address”. Each student must have an address so relationship b/w Student **class and Address class will be “Has-A” type relationship but vice versa is not true(it is not necessary that each address contain by any student)**. So Student work as owner entity. This will be a aggregation relationship.

```csharp
public class Student
{
    public string Name { get; set; }
    public Address Address;// *****Employee HAS-A Address but Address hasn't a Student*****  
    public Student(string name, Address address)
    {
        Name = name ?? throw new ArgumentNullException(nameof(name));
        Address = address ?? throw new ArgumentNullException(nameof(address));
    }    
    public void GetStudentInfo()
    {
        Console.WriteLine($"Student Info => Name: {Name}\n Address => Street: {Address.Street}, City: {Address.City}, State: {Address.State}");
    }
}

public class Address
{
    public string Street { get; set; }
    public string City { get; set; }
    public string State { get; set; }
    public Address(string street, string city, string state)
    {
        Street = street ?? throw new ArgumentNullException(nameof(street));
        City = city ?? throw new ArgumentNullException(nameof(city));
        State = state ?? throw new ArgumentNullException(nameof(state));
    }
}
```


**Coupling**
Coupling in Java refers to the information or dependency of one class on another class. It occurs when classes are aware of each other or interact with each other. If a class contains detailed information about another class, then we say that there is strong coupling between them.

We can use interfaces to have weaker coupling between classes because there is no concrete implementation in interfaces.

**Cohesion**
Cohesion refers to the level of performing a single well-defined task by a component. A highly cohesive method performs a single well-defined task. While, the weakly cohesive method will split the task into different parts.

The java.io package is a highly cohesive package in Java because this package contains the classes and interfaces related to I/O(Input/Output). The java.util package is considered as a weakly cohesive package because there are unrelated classes and interfaces in it.


####The four basic principles of object-oriented programming are:
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/oops-concept.jpg?raw=true).

**Abstraction** Modeling the relevant attributes and interactions of entities as classes to define an abstract representation of a system. <br>
In the book "Object Thinking" by David West, The Author emphasizes that abstraction is the process of hiding the internal details of an application from the outer world.
 Abstraction is used to describe things in simple terms and create a boundary between the application and the client programs. 
 It involves showing only relevant data and hiding unnecessary details of an object from the user.
 The main purpose of abstraction is to reduce programming complexity and efforts. 
 The book also highlights that abstraction is implemented in OOPs through interfaces and abstract classes.
 They are used to create a base implementation or contract for the actual implementation classes. 
 The book emphasizes that abstraction is a key concept in OOP that enables the user to implement more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden complexity.<br>
 Abstraction in the real world :<br>
I’m a coffee addict. So, when I wake up in the morning, I go into my kitchen, switch on the coffee machine and make coffee. Sounds familiar?
Making coffee with a coffee machine is a good example of abstraction.
You need to know how to use your coffee machine to make coffee. You need to provide water and coffee beans, switch it on and select the kind of coffee you want to get.
The thing you don’t need to know is how the coffee machine is working internally to brew a fresh cup of delicious coffee. You don’t need to know the ideal temperature of the water or the amount of ground coffee you need to use.
Someone else worried about that and created a coffee machine that now acts as an abstraction and hides all these details. 
You just interact with a simple interface that doesn’t require any knowledge about the internal implementation.<br>
<br>**Encapsulation** Hiding the internal state and functionality of an object and only allowing access through a public set of functions.<br>
By definition, encapsulation describes bundling data and methods that work on that data within one unit, like a class in Java. We often often use this concept to hide an object’s internal representation or state from the outside. This is called information hiding.<br>
The general idea of this mechanism is simple. For example, you have an attribute that is not visible from the outside of an object. You bundle it with methods that provide read or write access. Encapsulation allows you to hide specific information and control access to the object’s internal state.<br>
<br>**Inheritance** Ability to create new abstractions based on existing abstractions.<br>
inheritance is used in OOP to create a hierarchy of classes that share a set of attributes and methods, and it provides a powerful mechanism for code reuse and better code structure.<br>

<br>**Polymorphism** Ability to implement inherited properties or methods in different ways across multiple abstractions.<br>
olymorphism means "many forms", and it occurs when we have many classes that are related to each other by inheritance. <br>
There are two types of polymorphism: https://www.c-sharpcorner.com/UploadFile/ff2f08/understanding-polymorphism-in-C-Sharp/ <br>

#### Question_1:  What are advantages of composition and aggregation over inheritance?
#### Answer: 
1. There is principle, which sounds like "favor object composition over class inheritance". Composition over inheritance in OOP is the principle that classes should achieve polymorphism and code reuse by composition, instead of through inheritance. And there are reasons for existence of this principle.
2. In most cases "HAS-A" relationship is more semantically correct than "IS-A" relationship between classes.
3. Composition is more flexible than inheritance. You can change implementation of class at run-time by changing included object, thus changing behavior of it, but you can't do this with inheritance, you can't change behavior of base class at run-time.
4. Inheritance breaks encapsulation. By inheriting from a class you're coupling child class with number of potential implementation details of the parent.
5. A design based on object composition usually will have less classes.
It is possible to implement "multiple inheritance" in languages which do not support it by composing multiple objects into one.
6. There is no conflict between methods/properties names, which might occur with inheritance.

#### Question_2:  What are downsides of composition and aggregation?
#### Answer: 
1. The behavior of the system may be harder to understand just by looking at the source code, since it's more dynamic and more interaction between classes happens in run-time, rather than compile time.
2. Composition approach might require more code and time effort.
3. A design based on object composition usually will have more objects.


### Resources:
https://developer-interview.com/p/oop-ood/what-are-advantages-of-composition-and-aggregation-over-inheritance-14

## Git Essentials
## Concurrency and Parallelism In Depth
## Testing in Dotnet
## Design Patterns
## Design Principals
## Relational Databeses
## NoSql
## Caching
## Logging
## Identity
## IOC
## Observability and Monitoring
## system Design and Architecture
## AWS Cloud


