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

**Abstraction** Modeling the relevant attributes and interactions of entities as classes to define an abstract representation of a system.
<br>**Encapsulation** Hiding the internal state and functionality of an object and only allowing access through a public set of functions.
<br>**Inheritance** Ability to create new abstractions based on existing abstractions.
<br>**Polymorphism** Ability to implement inherited properties or methods in different ways across multiple abstractions.

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


