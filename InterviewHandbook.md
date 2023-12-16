# Interview Handbook
We hope it helps us to prepare for the **ASP.Net Core Developer** interview in a short time :)

### Table of Contents
**[OOP Concepts](#oop-concepts)**<br>
**[Git Essentials](#git-essentials)**<br>
**[Concurrency and Parallelism In Depth](#concurrency-and-parallelism-in-depth)**<br>
**[Testing in Dotnet](#testing-in-dotnet)**<br>
**[Design Patterns](#design-patterns)**<br>
**[Design Principals](#design-principals)**<br>
**[Clean Code](#clean-code)**<br>
**[Refactoring](#refactoring)**<br>
**[Relational Databeses](#relational-databeses)**<br>
**[NoSql](#nosql)**<br>
**[Caching](#caching)**<br>
**[Logging](#logging)**<br>
**[Identity](#identity)**<br>
**[IOC](#ioc)**<br>
**[Observability and Monitoring](#observability-and-monitoring)**<br>
**[system Design and Architecture](#system-design-and-architecture)**<br>
**[Cloud](#cloud)**<br>




## OOP Concepts
### Summary
Object-oriented programming (OOP) is a programming style that helps solve problems by thinking in terms of real-world objects. Each object has some behaviors and attributes. These concepts help organize code, improve code readability, reusability, maintainability, and security. 
### The four basic principles of object-oriented programming are:
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/oops-concept.jpg?raw=true).

**Abstraction** Abstraction in OOP is the concept of hiding the complex implementation details of a class and only exposing the necessary features and functionality to the outside world. It allows for the creation of simplified and easy-to-use interfaces for interacting with objects.<br>

<br>**Encapsulation** Encapsulation in OOP involves bundling the data and methods that operate on the data into a single unit, while restricting direct access to some of the object's members. This ensures that the members are accessed and modified in a controlled manner, promoting a consistent interface independent of the internal implementation. Encapsulation helps in maintaining code integrity, security, and organization by preventing unauthorized access to an object's internal state.<br>

<br>**Inheritance** Ability to create new abstractions (Class, Abstract Class and Interface) based on existing abstractions (Class, Abstract Class and Interface).<br>inheritance is used in OOP to create a hierarchy of classes that share a set of attributes and methods, and it provides a powerful mechanism for code reuse and better code structure.<br>

<br>**Polymorphism** Polymorphism in oop allows objects to take on different forms or behave differently based on the context in which they are used. It also enables derived classes to override specific functionality based on a common interface. There are two types of polymorphism: compile-time (static polymorphism), which uses method overloading, and runtime (dynamic polymorphism), which uses method overriding to implement. <br>


Object oriented programming generally support **4 types of relationships**, which include **inheritance**, **association**, **composition**, and **aggregation**.
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/relations-in-oop.png?raw=true).

<br>**1. Inheritance**: (is-a)
<br>Inheritance is “IS-A” type of relationship. “IS-A” relationship is a totally based on Inheritance, which can be of two types Class Inheritance or Interface Inheritance. Inheritance is a parent-child relationship where we create a new class by using existing class code. It is just like saying that “A is type of B”. For example is “Apple is a fruit”, “Ferrari is a car”.

<br>**2. Composition**: (part-of _ Is composed of another object and when BMW dies so Engine dies)
<br>Composition is a "part-of" relationship. Simply composition means mean use of instance variables that are references to other objects. In composition relationship both entities are interdependent of each other for example “engine is part of car”, “heart is part of body”.
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/composition.jpg?raw=true).

<br>Example of Inheritance and Composition

```csharp
    public class BMW : Car // Inheritance (BMW is a Car)
    {
        public Engine Engine { get; set; } // Sample usage of composition in C#
        public BMW()
        {
            Engine = new Engine("V-8", 300, 1200); // death dependency
        }
    }
    public class Engine
    {
        public string Name { get; set; }
        public int MaxSpeed { get; set; }
        public int Power { get; set; }

        public Engine(string name, int maxSpeed, int power)
        {
            Name = name ?? throw new ArgumentNullException(nameof(name));
            MaxSpeed = maxSpeed;
            Power = power;
        }
    }
```

<br>**3. Association**: (has-a)

<br>Association is a “has-a” type relationship. Association establish the relationship between two classes using through their objects. Association relationship can be **one to one**, **one to many**, **many to one** and **many to many**. For example suppose we have two classes then these two classes are said to be “has-a” relationship if both of these entities share each other’s object for some work and at the same time they can exists without each others dependency or both have their **own life time**.


<br>Example
```csharp
class Employee
{
    public string EmployeeName { get; set; }
    public void ManagerInfo(Manager manager)
    {
        manager.Info(this);
    }
}
class Manager
{
    public string ManagerName { get; set; }
    public void Info(Employee employee)
    {
        Console.WriteLine($"Manager of Employee {employee.EmployeeName} is {this.ManagerName}");
    }
}
```

<br>**4. Aggregation** (has-a. It has an existing object of another type)
<br>Aggregation is based is on "has-a" relationship. Aggregation is a special form of association. **In association there is not any classes (entity) work as owner but in aggregation one entity work as owner**. In aggregation both entities meet for some work and then get separated. **Aggregation is a one way association**.

Example
Let us take an example of “Student” and “address”. Each student must have an address so relationship b/w Student **class and Address class will be “Has-A” type relationship but vice versa is not true(it is not necessary that each address contain by any student)**. So Student work as owner entity. This will be a aggregation relationship.

```csharp
public class Student
{
    // Aggregation is a one way dependency relation
    public string Name { get; set; }
    public Address Address;// Employee HAS-A Address  _ Address has a standalone lifetime
    public Student(string name, Address address)
    {
        Name = name ?? throw new ArgumentNullException(nameof(name));
        Address = address ?? throw new ArgumentNullException(nameof(address));
    }
}

public class Address
{
    public string Street { get; set; }
    public string State { get; set; }

    public Address(string street, string state)
    {
        Street = street ?? throw new ArgumentNullException(nameof(street));
        State = state ?? throw new ArgumentNullException(nameof(state));
    }
}
```


**Cohesion**
<br>Cohesion refers to the degree to which the elements of a module/class belong together, it is suggested that the related code should be close to each other, so we should strive for high cohesion and bind all related code together as close as possible. It has to do with the elements within the module/class.

**Coupling**
<br>Coupling refers to the degree to which the different modules/classes depend on each other, it is suggested that all modules should be independent as far as possible, that's why low coupling. It has to do with the elements among different modules/classes.
We can use interfaces to have weaker coupling between classes because there is no concrete implementation in interfaces.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/coupling-and-cohesion.png?raw=true).


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
A design pattern is a general repeatable solution to a commonly occurring problem in software design. According to GOF, there are 3 types of design patterns, which include 22 patterns:
### 1. Creational Design Patterns: 
<br>Focus on **object creation** (class instantiation). These patterns often use for **reducing complexity** of class instantiation and providing **flexibility** in creating objects while **decoupling** the system from specific classes or implementations. These patterns aim to ensure that the process of creating objects is **efficient, extensible, and easily maintainable**. They can be further divided into **class-creation patterns** and **object-creational patterns**. While class-creation patterns use **inheritance** effectively in the instantiation process, object-creation patterns use **delegation** to get the job done. 
<br> Creational patterns list: 1. **Singltone**  2. **Factory Method**  3. **Abstraction Factory**  4. **Prototype**  5. **Builder**
### 2. Structural Design Patterns: (composition and relationships)
<br> Structural patterns deal with **composition and relationships**. These patterns are intended for organizing larger class structures and compositions. The main goal of most of these patterns is to **increase the functionality of the class(es) involved, without changing much of its composition**. 
 These patterns **help define relationships between objects, ensuring flexibility, and ease of modification**.
<br> Structural patterns list: 1. **Adapter**  2. **Facade**  3. **Composition**  4. **Proxy**  5. **Decorator**  6. **Bridge**  7. **Flyweight**
### 3. Behavioral Design Patterns: (interaction and communication)
<br>Behavioral patterns focus on the **interaction and communication** between objects. These patterns define communication patterns and the delegation of responsibilities between objects.
<br> Behavioral patterns list: 1. **Strategy**  2. **Observer**  3. **Command**  4. **Template method**  5. **State**  6. **Vistor**  7. **Chain of responsibility**  8. **Iterator**  9. **Mediator**  10. **Memento**

#### After GOF, some other types of design patterns are defined, such as Architectural design patterns and Cloud design patterns:
### Architectural design patterns: 
<br>Architectural patterns focus on the **overall structure and organization** of a software system. These patterns provide guidelines and **high-level structures** for designing **large-scale applications**.
<br>Architectural patterns list: 1. **Model-View-Controller (MVC)**  2. **Model-View-ViewModel (MVVM)**  3. **Microservices Architecture**  4. **Event-Driven Architecture (EDA)** and etc.
### Cloud design patterns:
<br>These patterns provide **guidance and best practices for designing and implementing cloud-based systems**, and are widely used in the industry to ensure that cloud applications are reliable, scalable, and secure. They provide solutions for a wide range of problems, including **data management**, **messaging**, and **application resilience** (Design and Implemention). Cloud design patterns are essential for ensuring that cloud-based applications are **well-architected** and **can meet the demands of modern, distributed systems**. 

<br>Cloud patterns list: 1. **Ambassador pattern**  2. **Retry pattern**  3. **Circuit Breaker pattern**  4. **Anti-Corruption Layer**  5. **Bulkhead**  6. **Queue-based load leveling**  7. **Throttling**  8. **Saga**  9. **CQRS** and etc. 

### Resources:
1.    https://www.freecodecamp.org/news/the-basic-design-patterns-all-developers-need-to-know/
2.    https://arindam-das.medium.com/design-patterns-demystified-unlocking-the-power-of-creational-structural-behavioral-and-f50e3a5b6cd7#:~:text=Creational%20patterns%20focus%20on%20object%20creation%2C%20structural%20patterns%20deal%20with,guide%20the%20overall%20system%20structure.

## Design Principals
## Clean Code
## Refactoring
## Relational Databeses
## NoSql
## Caching
## Logging
## Identity
## IOC
## Observability and Monitoring
## system Design and Architecture
## Cloud


