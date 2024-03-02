# Interview Handbook
We hope it helps us to prepare for the **ASP.Net Core Developer** interview in a short time :)

### Table of Contents
**[OOP Concepts](#oop-concepts)**<br>
**[Git Essentials](#git-essentials)**<br>
**[Concurrency and Parallelism In Depth](#concurrency-and-parallelism-in-depth)**<br>
**[Design Patterns](#design-patterns)**<br>
**[Design Principals](#design-principals)**<br>
**[Clean Code](#clean-code)**<br>
**[Testing](#testing)**<br>
**[Refactoring](#refactoring)**<br>
**[Relational Databeses](#relational-databeses)**<br>
**[NoSql](#nosql)**<br>
**[Caching](#caching)**<br>
**[Logging](#logging)**<br>
**[Identity](#identity)**<br>
**[IOC](#ioc)**<br>
**[Message Broker](#message-broker)**<br>
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

<br>**3. Association**: (use-a)

<br>Association is a “use-a” type relationship. Association establish the relationship between two classes using through their objects. Association relationship can be **one to one**, **one to many**, **many to one** and **many to many**. For example suppose we have two classes then these two classes are said to be “use-a” relationship if both of these entities share each other’s object for some work and at the same time they can exists without each others dependency or both have their **own life time**.


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
Let us take an example of “Student” and “address”. Each student must have an address so relationship between Student **class and Address class will be “Has-A” type relationship but vice versa is not true(it is not necessary that each address contain by any student)**. So Student work as owner entity. This will be a aggregation relationship.

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

### Difference between Aggregation and Composition Relationship in OOP
In Object-Oriented Programming (OOP), both aggregation and composition are ways to represent relationships between classes, but they differ in the strength of the relationship and the lifecycle management of the objects involved.
#### Aggregation Relationship:
* Aggregation is a "has-a" relationship where one class is a part of another class but can exist independently.
* It represents a weaker relationship where objects can be shared among multiple classes.
* The aggregated class can exist without the container class.
**Example:** A university has departments. A department can exist independently of the university and can be part of multiple universities.
#### Composition Relationship:
* Composition is a stronger form of aggregation where one class is composed of another class and cannot exist without it.
* It signifies a whole-part relationship where the part cannot exist independently outside the whole.
* The composed class's lifecycle is tied to the container class, and when the container is destroyed, so are its parts.
**Example:** A car has an engine. The engine is an integral part of the car, and if the car is destroyed, the engine goes with it.


### Cohesion and Coupling: 

**Cohesion**
<br>Cohesion refers to the degree to which the elements of a module/class belong together, **it is suggested that the related code should be close to each other**, so we should strive for high cohesion and bind all related code together as close as possible. It has to do with the elements within the module/class.

**Coupling**
<br>Coupling refers to the degree to which the different modules/classes depend on each other, **it is suggested that all modules should be independent as far as possible**, that's why low coupling. It has to do with the elements among different modules/classes.
<br>We can use interfaces to have weaker coupling between classes because there is no concrete implementation in interfaces.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/coupling-and-cohesion.png?raw=true).



More details of coupling and cohesion in the link below that include types of coupling and cohesion, etc.
https://www.geeksforgeeks.org/software-engineering-coupling-and-cohesion/

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/coupling-and-cohesion-details.jpg?raw=true).


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

#### Clone Repository
Clones a repository onto your local machine. You can replace <repository_url> with either a remote URL or a path to a local repository.
```
git clone <repository_url>
```

#### Add Files
Stages files for the next commit. The first command stages a specific file, while the second stages all modified files in the current directory.
```
git add <file_name>
git add .
```

#### Commit Changes
Creates a new commit containing changes staged previously. Use a descriptive commit message to help others understand what has changed.
```
git commit -m "<commit_message>"
```

#### View Status
Displays the state of working tree and cached content. Shows which files are added, deleted, or modified compared to the last commit.
```
git status
```

#### Check Log
Shows the complete revision history of the project. Each line represents a single commit.
```
git log
```

### Manage Branches
#### List Branches 
Lists all branches locally. By default, this command shows only non-remote branches.
```
git branch
```

#### Switch Between Branches
Switches to a specified branch.
```
git checkout <branch_name>
```

#### Create New Branch
Creates a new branch and switches to it immediately.
```
git branch <new_branch_name>
git checkout -b <new_branch_name>
```

#### Merge Branches
Merges changes from the target branch into the currently checked out branch.
```
git merge <target_branch_name>
```

#### Delete Branch
Deletes a local branch.
```
git branch -d <branch_name>
```

### Remote Operations
#### Add Remote Repository
Establishes a connection between your local repository and a remote repository.
```
git remote add origin <repository_url>
```

#### Pull From Remote
Retrieves changes from the remote repository and merges them into the current branch.
```
git pull origin <branch_name>
```

#### Push to Remote
Uploads commits made in the current branch to the remote repository.
```
git push origin <branch_name>
```

#### Git Diff
Git's diff command compares the contents of files between commits, showing the differences visually or in patch form.
Comparisons can be done between any pair of commits, including the current head (HEAD), previous head (HEAD~1), and so forth. Specify the paths of interest after the double dash (--).
```
git diff <first_commit>..<second_commit> -- <path_to_file>
git diff HEAD~1 HEAD -- <path_to_file>
```
#### Git Diff (with staged)
With --staged option or without arguments, `git diff` displays differences between the working tree and the index (unstaged changes). 
```
git diff --staged
```
#### Git Diff (with cached)
With --cached option, it shows differences between the index and the latest committed version (staged changes).
```
git diff --cached
```

### Git Reset
Git's reset command modifies the history of your repository, moving the tip of the current branch back to a particular commit.

#### Hard Resets
Hard resets discard all changes since the specified commit. Be cautious when using hard resets because they cannot be undone easily.
```
git reset --hard <commit_hash>
```

#### Soft Resets
Soft resets move the tip of the current branch back to the specified commit but keep the changes in the working tree.
```
git reset --soft <commit_hash>
```
#### Mixed Resets
This command resets the index to the specified commit while keeping the changes in the working directory but not staged. It allows you to review the changes before committing them again. It is a mix of hard and soft resets.
```
git reset --mixed <commit_hash>
```
#### Partial Resets
Partial resets allow reverting selected files while keeping others intact.
```
git reset <path_to_file> -- <other_paths>...
```

#### The differences between git reset --hard, git reset --soft, and git reset --mixed in Git are as follows:
* **git reset --hard:** This command resets the index and working directory to the specified commit. **It discards all changes and history after that commit**. It is a destructive operation, meaning all changes are permanently lost.
* **git reset --soft:** This command resets the index to the specified commit while **keeping the changes in the working directory and it unstages the changes**, allowing you to recommit them if needed. It is a non-destructive operation.
* **git reset --mixed:** This command resets the index to the specified commit while **keeping the changes in the working directory but not staged**. It allows you to review the changes before committing them again. It is a mix of hard and soft resets.

### Git Blame
Git's blame command assigns responsibility for each line of code in a file to the author who last modified it.

#### Basic Usage
By default, git blame lists the most recent commit at the top and works backward through the history.
```
git blame <filename>
```

#### Show Author Information
With the -p flag, git blame also includes parent information, displaying the relationship between commits. The -l flag removes unnecessary whitespace and makes output easier to read.
```
git blame -p -l <filename>
```

#### Cherry pick
Selects a specific commit from one branch and applies it to another, helpful for incorporating individual changes.
This contrasts with other ways such as merge and rebase which normally apply many commits to another branch.
It's also possible to cherry-pick multiple commits but merge is the preferred way over cherry-picking.

1. Ensure Clean Working Directory:
Make sure there are no changes in both branches:
```
git status
```

2. Select the Source Branch:
Checkout the branch containing the commit you want to pick:
```
git checkout <source_branch>
```
3. Identify the Commit:
Use git log to find the commit you want to cherry-pick and copy its hash.
Move to Target Branch:
Checkout the branch where you want to apply the cherry-picked commit:
```
git checkout <target_branch>
```

4. Cherry-Pick the Commit:
Execute the cherry-pick command with the commit hash:
```
git cherry-pick <commit_hash>
```

5. Resolve Conflicts (if any):
If conflicts arise, resolve them manually.
Commit Changes:
After resolving conflicts, commit the changes.

#### Git Rebase
Reapplies commits on top of another base tip, useful for maintaining a clean commit history.
```
git checkout feature_branch
git rebase main
```
#### Git Stash
Temporarily shelves changes to work on something else, then reapply them later.
```
git stash
git checkout other_branch
git stash pop
```
#### Git Bisect
Helps find the commit that introduced a bug by performing a binary search through the commit history.
```
git bisect start
git bisect bad <commit_hash>
git bisect good <commit_hash>
```
#### Git Reflog
Shows a log of all Git references, useful for recovering lost commits or branches.
```
git reflog
```

## Concurrency and Parallelism In Depth
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
### SOLID
The SOLID principles were introduced by Robert C. Martin in his 2000 paper “Design Principles and Design Patterns.” These concepts were later built upon by Michael Feathers, who introduced us to the SOLID acronym.

The SOLID acronym stands for:

* Single Responsibility Principle (SRP)
* Open-Closed Principle (OCP)
* Liskov Substitution Principle (LSP)
* Interface Segregation Principle (ISP)
* Dependency Inversion Principle (DIP)



## Clean Code
## Testing
![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/types-of-testing.png?raw=true).

### Unit Testing Best Practices
1. Write simple, readable tests: Easy-to-understand tests enable quick identification of issues and reduce maintenance efforts
2. Write deterministic tests: Ensure that tests yield predictable outputs, regardless of the environment or input variations
3. Test one scenario per test case: Each test should focus on a single aspect of the code, preventing confusion and reducing false positives
4. Automate unit tests: Set up an automated process for unit testing to catch errors early and allow frequent execution
5. Write isolated tests: Utilize test doubles to isolate units from external dependencies, enhancing test stability and speed
6. Avoid test interdependence: Independent tests minimize the risk of cascading failures and increase test repeatability
7. Avoid active API calls: Reduce reliance on live services to decrease test setup times and improve test stability
8. Combine unit and integration testing: Implement a hybrid approach to gain the advantages of both testing paradigms
9. Ensure test coverage: Maximize test coverage to increase confidence in the codebase
10. Design tests for speed: Fast tests encourage frequent executions and promote agility in the development process
12. Test for security issues: Incorporate security checks into unit tests to proactively mitigate vulnerabilities
13. Review and maintain tests: Regularly audit and update tests to reflect changes in the codebase and ensure ongoing effectiveness
14. Adopt test-driven development (TDD): Write tests prior to implementing features, fostering cleaner designs and improved code quality
15. Collaboratively develop tests: Encourage collaboration among developers to foster shared ownership of tests and improve code reviews
16. Treat test failures seriously: Address test failures immediately to prevent defect propagation and maintain code health

Adhering to these best practices promotes robust unit testing, leading to increased code quality, reduced defect rates, and enhanced developer productivity.

### Integration Testing Best Practices:
1. Maintain Dedicated Test Suites:
    Keep separate and dedicated test suites for unit testing and integration testing to ensure efficient testing processes.
2. Keep Business Logic Separate:
    Avoid testing business logic along with integration testing to simplify the testing process and ensure faster execution of unit tests.
3. Craft Integration Testing Plan:
   Develop a comprehensive integration testing plan outlining the components, interfaces, and interactions to be tested.
4. Define Relevant Tests & Use Cases:
   Determine specific test cases and use cases based on software units, features, and requirements for efficient integration testing.
5. Run Testing Methods:
   Utilize various integration testing methods such as top-down, bottom-up, or sandwich approaches to ensure thorough testing coverage.
6. Scan & Detect Errors:
    Conduct detailed scans to identify errors in the combined functionalities of modules or components during integration testing.
7. Retest After Fixing Errors:
    Perform retesting iteratively until all issues or bugs are resolved to achieve optimal software quality and functionality.
8. Combine Manual and Automated Testing:
    Blend manual and automated testing methods to cover all aspects of integration and ensure effective validation.
9. Document and Track Issues:
   Document and track issues discovered during testing to address them promptly and improve the overall testing process over time.
10. Test Early and Often:
    Initiate integration testing early in the development process and continue testing throughout the project lifecycle to identify issues promptly.
11. Use Various Testing Methods:
    Employ a variety of testing methods to ensure thorough evaluation of integrated systems and components.
12. Make Continuous Improvements:
    Continuously evaluate and enhance the integration testing process based on metrics, feedback, and lessons learned from previous cycles.
13. Maintain the Testing Environment:
    Ensure the stability and consistency of the testing environment by keeping hardware and software updated and isolated from production systems.
14. Define Acceptance Criteria:
    Establish clear acceptance criteria based on functional requirements to validate that the integrated system meets stakeholder needs.
    By following these best practices in integration testing, teams can enhance the reliability, functionality, and performance of their software systems while e      nsuring seamless interactions between different components or modules.

### Types of Test Doubles in Software Testing with Examples:
1. Dummy:
Description: Objects passed around but not used, typically to fill parameter lists.
Example: Passing a dummy object as a placeholder parameter in a function call during testing.
2. Fake:
Description: Provides a working implementation but may take shortcuts not suitable for production.
Example: Using an in-memory test database as a fake to simulate database interactions in tests.
3. Stub:
Description: Provides canned answers to calls made during the test, responding only to programmed scenarios.
Example: Creating a stub object that returns predefined responses to specific method calls during testing.
4. Spy:
Description: Records information about its state and usage, combining aspects of stubs and mocks.
Example: Using a test spy to track how many times a specific method is called within a test scenario.
5. Mock:
Description: Pre-programmed with expectations for specific calls, verifying they are received as expected.
Example: Setting up a mock object to expect certain method calls and parameters during unit testing.

These types of test doubles play crucial roles in software testing by replacing real dependencies with controlled substitutes, enabling focused and reliable testing of code functionality without external dependencies

### Four-Phase Test in Software Testing:
1. Setup:
Description: In the setup phase, the system under test is prepared for the test.
Example: Creating an instance of a class or setting up necessary data before executing the test.
2. Exercise:
Description: The exercise phase involves executing the system under test to perform the intended operation.
Example: Invoking a method or function to trigger a specific behavior for testing.
3. Verify:
Description: During verification, the outcome of the exercise is compared against expected results.
Example: Checking if the result matches the expected output or behavior.
4. Teardown:
Description: In the teardown phase, the system under test is reset to its pre-setup state.
Example: Releasing memory, cleaning up resources, or resetting data structures used during the test.

### Types of Teardown in Software Testing:
1. Manual Teardown:
Description: Involves physically disassembling hardware or software components for inspection or analysis.
Example: A quality assurance engineer manually disassembles a prototype device to examine its internal components and identify any potential defects.
2. Transactional Teardown:
Description: Reverts database transactions or temporary modifications made during a test to restore the system to its pre-test state.
Example: During an online banking application test, transactions made during the test are rolled back to ensure the account balances return to their original values.
3. Sandbox Teardown:
Description: Restores the testing environment to its original state after executing tests within a controlled environment.
Example: A software developer runs unit tests in a sandbox environment, where each test case is isolated and the environment is reset after each test run.
4. No Teardown:
Description: Skips the teardown phase, leaving the system in its current state after test execution.
Example: In a simple UI testing scenario, where no cleanup is necessary as the actions performed during the test do not impact subsequent tests.
5. Truncate Table:
Description: Empties a database table by removing all rows, effectively resetting its contents.
Example: Before running regression tests on a customer database, the testing script truncates the "Orders" table to ensure a clean starting point for each test iteration.

## Refactoring
## Relational Databeses
## NoSql
## Caching
## Logging
## Identity
## IOC
## Message Broker

### When to use a message broker instead of other communication methods in programming:
When integrating heterogeneous applications and systems and enabling message communication between these systems to achieve desired business goals, choosing the right messaging platform is always a key decision in any organization. Legacy approach of Point to Point Integration between a set of systems and applications is neither scalable nor performance efficient and that’s why organizations tend to opt for more agile and efficient approaches including ESB based Integrations and inclusion of a message broker as a Message Oriented Middleware to achieve a loosely coupled or ideally a decoupled messaging in the applications and systems eco-system.

When we talk about Message Brokers, there are plenty of options available — proprietary as well as open-source which fulfil the required goal of achieving efficient, scalable and robust messaging for complex business scenarios involving huge number of information generating and information consuming applications. We already talked about ActiveMQ Message Broker in another tutorial which is a widely used open-source message broker which can be used to integrate various systems and applications supporting a rich set of protocols and data formats. ActiveMQ is a JMS provider which is based on JMS specifications.

In this tutorial, we will cover another widely known and popular open-source message broker– RabbitMQ and we will have a high level overview of RabbitMQ in which we cover RabbitMQ Introduction, RabbitMQ basic Concepts as a RabbitMQ Beginners Tutorial without going into the complexities associated.
Before we dig deeper and talk about RabbitMQ Message Broker, It is important to first talk a bit about Message Broker in general to set the context.

What is a Message Broker?
A message broker is an application which sits in the middle of the two or more systems or applications which need to communicate with each other uni-directional or bi-directional in the forms of messages. A message broker with its ability to store, route, filter messages originated from a message producing application can help a message consuming application or system to receive the messages as and when desired without a direct tightly coupled link between the source and destination parties.

In the below diagram, we have a simple example where we have multiple Producers and multiple consumers connected to a Message Broker in order to produce and consume messages respectively.

Different message brokers can have additional features and abilities for message mediation, transformation, filtering and routing but in general, all of these brokers primarily serve the purpose of a middle-man to deliver the messages to the consumers on behalf of producer.

RabbitMQ Introduction: What is RabbitMQ Message Broker
RabbitMQ is a widely used and a well known open-source Message Broker which is used as a queuing system to enable message communication in an asynchronous fashion between different applications and system.

RabbitMQ is based on AMQP (Advanced Message Queuing Protocol) with a support of various communication protocol including HTTP, STOMP, MQTT etc. making it a flexible choice to utilize it as a Message Oriented Middleware for integrating systems and applications of different nature in a seamless and efficient manner.

RabbitMQ Core Concepts
To understand how RabbitMQ as a message broker works, we need to first have a clarity on various concepts which are the basic building block of message brokers in general and RabbitMQ in particular.

Message
A message is a piece of information that contains useful content that needs to be shared between communicating parties. A message consists of following elements:

Message Header
Message header contains meta-data about the message and helps understanding various useful information about the actual message. E.g. data format or encoding format can be part of a message header.

Message Body
A message body contains the actual information or the core of a message. For example a message about an account can have details of the account holder in JSON or XML format in the body of a message.

Message Properties (Optional)
Additional properties can be associated with a message which can be used to filter the messages. For example, we can think of having AccountType property for a message about Accounts and consuming applications can filter messages based on this property to pick only relevant messages from the broker queues.

Message Producers
Message Producers are those systems or applications which produce messages and send it to the broker to make those messages available for potential consumers to pick from the broker queues and consume it as desired.

There can be any number of message producers which can connect to the broker as producers.

* RabbitMQ Exchange
Exchange is a routing manager in RabbitMQ message broker which routes the messages towards different queues which are produced by the producer.  Contrary to ActiveMQ or other JMS based message brokers, in RabbitMQ messages are not sent by producers directly to the queues; rather Exchanges are used to route the messages as per binding associations.

There are different RabbitMQ Exchange types which route the message differently towards the queues.

### Following are the Exchange Types in RabbitMQ:

* Direct Exchange
A direct Exchange in RabbitMQ routes messages to the queues based on the routing key and binding key association. A message received in a direct exchange with a routing key abc is routed to any queue with binding key abc (same as routing key).

* Topic Exchange
A Topic Exchange is used for multi-cast purposes where a message received on a Topic Exchange is routed to multiple queues based on a wildcard match between routing key of the message and the binding key pattern of the queues.

* Fanout Exchange
Fanout Exchange is used in order to broadcast a message to all the queues which are bound it it without checking any association between routing and binding keys. A copy of same message is sent to every queue by ignoring any routing keys.

* Header Exchange
Header Exchange in RabbitMQ is used to send messages to queues based on matching header fields. There can be a binding with either one header property (using Match-Any) or all header fields (Match-All) and accordingly messages are routed to the queues.

When using Header exchange, routing key is ignored as routing decisions are purely based on header attributes.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/rabbitmq.png?raw=true).

### How RabbitMQ Works?
In order to understand basic concepts of RabbitMQ further and to understand how RabbitMQ works, refer to below video on TutorialsPedia YouTube channel where I have explained the concepts in detail. Since this is RabbitMQ beginners tutorial, you should be able to grasp the concepts easily without going into the advanced topics or much details.

At a high level, below diagram depicts how RabbitMQ works as a Message Broker:

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/how-rabbitmq-works.png?raw=true).

* Microservices Communication:
In a microservices architecture where services are distributed and communicate through messages, a message broker like RabbitMQ can streamline communication between services, reducing the complexity of direct API calls and enabling scalable and reliable interactions

* Long-Running Tasks:
  When tasks triggered by messages, such as video processing or background tasks, require extended processing time, a message broker can efficiently manage these  
  long-running operations without blocking the main application flow

* Mobile Apps:
  Message brokers are beneficial for mobile apps where asynchronous communication is essential for handling events, notifications, and data updates efficiently across different devices and platforms

* Scalability:
As the volume of messages exchanged between components increases, a message broker becomes crucial for managing message delivery, ensuring reliability, and handling potential spikes in traffic effectively

* Decoupling Services:
Message brokers promote loose coupling between services by allowing them to communicate without direct knowledge of each other. This decoupling enhances system flexibility, resilience, and maintainability

In summary, consider using a message broker like RabbitMQ when dealing with distributed systems, asynchronous communication requirements, scalability challenges, long-running tasks, or the need for decoupling services to enhance the overall robustness and efficiency of your application architecture

Producing messages with RabbitMQ does not require the sender to wait for a response from consumers; instead, it places data into an exchange without knowing if or when consumers will retrieve them. This approach promotes decoupling and minimizes dependencies.
If you want to deliver data to multiple recipients, using messaging eliminates the need to create separate APIs for each recipient. Instead, you simply publish data to an exchange where consumers can subscribe to receive those messages. This design helps achieve scalable and available systems in distributed environments.
### Key features of RabbitMQ include:
* Support for various programming languages
* Open source
* Easy to use
* Multiple protocol support
* Written in Erlang
* Enables high scalability and availability in distributed and federated environments.
### Best practices for RabbitMQ usage:
Create one queue per consumer.
Publish messages to exchanges, not directly to queues.
Exchanges act like routers for messages.
Routing keys are attributes included in message headers.
Four primary types of exchanges plus additional customizable ones.
Messages in RabbitMQ follow FIFO order by default but prioritization can be applied through message and queue settings.
Time To Live (TTL).
Priorities.

### Protocols supported by RabbitMQ:
* AMQP (Advanced Message Queuing Protocol)
* STOMP (Simple (or Streaming) Text Orientated Messaging Protocol)
* MQTT (MQ Telemetry Transport)
* HTTP & WebSocket.

## Observability and Monitoring
## system Design and Architecture
## Cloud


