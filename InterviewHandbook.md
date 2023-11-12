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
**[Logging](#logging)**<br>
**[Observability and Monitoring](#observability-and-monitoring)**<br>
**[system Design and Architecture](#system-design-and-architecture)**<br>
**[AWS Cloud](#aws-cloud)**<br>




## OOP Concepts
### Summary
C# is an object-oriented programming language. The four basic principles of object-oriented programming are:

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
## Logging
## Observability and Monitoring
## system Design and Architecture
## AWS Cloud


