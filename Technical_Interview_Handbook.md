# Technical Interview Handbook
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
**[Relational_Databases](#relational-databases)**<br>
**[Garbage_Collection](#garbage-collection)**<br>
**[NoSql](#nosql)**<br>
**[Caching](#caching)**<br>
**[Logging](#logging)**<br>
**[Identity](#identity)**<br>
**[IOC](#ioc)**<br>
**[Message Broker](#message-broker)**<br>
**[Observability and Monitoring](#observability-and-monitoring)**<br>
**[System Design and Architecture](#system-design-and-architecture)**<br>
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

### Here are some popular Git workflows
1. **Trunk-Based Workflow:** This workflow is considered a best practice for modern continuous software development and DevOps practices. It involves committing changes directly to the main branch, simplifying the development process and increasing stability
2. **Feature Branch Workflow:** In this workflow, developers create a branch for each feature they are working on, make changes, submit a merge request, and then merge it back into the main branch. It helps keep the main branch clean and avoids conflicts with unfinished features
3. **GitHub Flow:** GitHub Flow is a simpler workflow that breaks down large sets of changes into smaller chunks that can be addressed more frequently. It is more conducive to iterative development and easier to manage compared to complex branching models like Gitflow
4. **Gitflow Workflow:** Gitflow is a legacy Git branching model that involves feature branches and multiple primary branches. It has fallen in popularity in favor of trunk-based workflows due to its complexity and challenges with CI/CD integration

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
#### Git Squash
In Git, squashing commits involves combining multiple commits into a single commit to simplify the commit history and make it more organized. This process is useful for cleaning up the branch history and creating more meaningful commits. There are several ways to squash commits in Git:

**1. Interactive Rebase Method:**
Use the command **git rebase -i HEAD~<number_of_commits>** to enter interactive mode.
In the interactive editor, change "pick" to "squash" for the commits you want to squash.
Save the file, enter a new commit message, and complete the process

**2. Merge Command with --squash Flag:**
Create and switch to a new branch where you want to merge the commits.
Use **git merge --squash <Branch>** to merge the branch with the --squash option.
Resolve any merge conflicts and commit the changes

Squashing commits helps in easier code reviewing, reducing clutter in the repository, simplifying rollback of changes, and facilitating merging branches with fewer conflicts. It is recommended to squash related commits before submitting a pull request for better code understanding and maintenance

### resources:
1. https://nvie.com/posts/a-successful-git-branching-model/

## Concurrency and Parallelism In Depth

### Idioms:

**Multithreading** and **Asynchronous Programming** are two different programming paradigms used to achieve **concurrency** and **parallelism** in computer systems.

#### Parallel Programming: 
This is all about multiple tasks **running on multiple cores simultaneously** (parallel programming involves breaking down a computational task into smaller parts that can be executed simultaneously)

#### Concurrency:
- Concurrency is a concept where several tasks appear to run simultaneously, **but not necessarily in parallel**.
- It’s about dealing with multiple tasks at once, which can be achieved in various ways, including parallelism (using multiple processors), interleaved processing (time-slicing on a single processor), or even distributed processing across multiple machines.
- It’s about managing access to shared resources, ensuring that data remains consistent, and tasks are executed in an orderly manner.

#### Multithreading: 
- This is all about a single process split into multiple threads. 
- Multithreading is a form of concurrency where multiple threads, it's important to note that multithreading is not necessarily limited to physical threads and can involve logical threads as well.
- Unlike asynchronous programming, which may or may not use threads, multithreading always involves multiple threads
- Managing multithreaded applications can be complex due to issues like race conditions, deadlocks, and the need for synchronization mechanisms. 

#### Asynchronous Programming: 
- Asynchronous programming is a form of concurrency where **tasks start and then move on without waiting for the previous task to finish** (This is all about a single thread initiating multiple tasks without waiting for each to complete). This can be achieved using callbacks, promises, futures, events, etc.
- It’s especially popular in I/O-bound operations (like reading files, making network requests) where tasks don’t need to wait for the operation to complete and can proceed with other operations, improving responsiveness.
- Asynchronicity doesn’t necessarily imply parallel execution. The tasks may still be executed in a single thread (like in JavaScript’s Node.js), but the system can handle other tasks while waiting for some tasks to complete.

#### Critical Section
A critical section in programming is a specific part of code where shared resources are accessed, requiring exclusive execution to prevent data conflicts. It ensures that only one thread or process can access these resources at a time, maintaining data integrity and avoiding race conditions. By using synchronization mechanisms like mutexes or semaphores, critical sections enforce mutual exclusion, essential for preventing issues like data corruption and deadlock in concurrent programming. Properly managing critical sections is crucial for effective resource sharing and synchronization in multi-threaded environments.

#### Critical Section Pillars
*  There are more than one thread in the application
*  Shared data must exist
*  There is a need to modify the shared data

#### Racing Condition
A race condition occurs when **two or more threads** can access **shared data** and they try to change it at the **same time**. 

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/race-conditions.png?raw=true" alt="Race Conditions" width=600; height=300>

#### Heisenbug
A heisenbug is a software bug that changes its behavior or disappears when you try to observe or debug it.
Problems occurring in production systems can therefore disappear when runnig in debug mode, when additional logging is added, or when attaching a debugger, often referred to as a heisenbug.
Preventing race conditions through thoughtful software design is more effective than trying to resolve them later.

#### DeadLock
Deadlock describes a condition in which two or more threads are blocked (hung) forever because they are waiting for each other.

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/deadlock.png?raw=true" alt="Deadlock" width=350; height=220>

#### Physical Thread (Logical Processor or Logical Core)
Physical thread relates to the actual hardware threads available on a processor, where each physical core can execute multiple tasks simultaneously, often achieved through technologies like hyper-threading.

#### Logical Thread (Virtual Thread or Software Thread)
Logical thread involves the software perspective, where threads are virtual constructs that allow a single core to handle multiple tasks concurrently. While physical threads are tied to the hardware capabilities of the processor, logical threads are more flexible and can be managed at a higher level by the operating system or programming environment

#### I/O Bound and CPU Bound
**CPU-bound tasks** The term CPU-bound describes a scenario where the execution of a task or program is highly dependent on the CPU.
**I/O-bound tasks**, spend time waiting for input/output operations to complete, such as reading from databases or interacting with files. 

#### Context Switching 
Execution of multiple threads on a single CPU core causes thread or context switching that is managed by the **schedular**. <br>
Because  the thread scheduling algorithm can swap between threads at any time, you don't know the order in which threads will attemp to access the shared data.
* The period during which a thread is allocated time to execute a specific task before a context switch occurs is known as the **quantum time or time slice**. This interval defines how long a thread can run before the operating system switches to another thread, managing resource allocation and ensuring fair execution among concurrent processes. Efficient management of quantum time is crucial for optimizing system performance and balancing task execution in multitasking environments.
* **Thread and process priority** determine the order of **task execution and resource allocation**. Higher-priority threads and processes are given precedence during context switching, ensuring critical tasks are handled promptly. **Managing priorities helps prevent issues like CPU starvation**, where low-priority tasks may wait indefinitely for resources due to higher-priority tasks constantly using the CPU. Techniques like aging can help balance priorities over time to avoid such scenarios and optimize system performance.
* During each context switch, **the system saves the state of the currently running process or thread**, including registers and other essential data, to a data structure like a process control block (PCB). This saved state allows the process to be paused and later resumed from the same point when it regains CPU time. Subsequently, **the system loads the saved state of the next process or thread that is scheduled to run, enabling seamless execution transitions between multiple tasks**
* To minimize overhead and costs, it is advisable to **reduce unnecessary context switches** due to their high impact.
* Mistakes in C# programming leading to unnecessary context switches:
    1. **Avoiding Exceptions:** Missing error handling can cause extra context switches, impacting efficiency.
    2. **Naming Conventions:** Incorrect naming can confuse and trigger unnecessary context switches in C# code.
    3. **Inefficient Data Access:** Poor data retrieval practices like excessive I/O operations can lead to unnecessary context switches.
    4. **Multithreading Errors:** Improper thread management or excessive synchronization can increase context switching overhead in C#.
    5. **Garbage Collection Impact:** Creating and discarding many objects can trigger frequent garbage collection cycles, causing unnecessary context switches.  

#### CPU Starvation
CPU starvation occurs when a thread is consistently denied access to resources, hindering its progress and potentially leading to significant delays in task execution.
For instance, **inefficient thread management**, **improper synchronization mechanisms**, and **excessive thread creation without proper resource sharing strategies** can all lead to CPU starvation by causing delays in task execution and resource contention.

A popular mistake in C# programming that can lead to CPU starvation is inefficient usage of the Task.Run method, especially for I/O-bound operations. Incorrectly using Task.Run for I/O-bound tasks can result in inefficient resource utilization, potentially causing CPU starvation. It is crucial to use the async-await pattern for I/O-bound operations instead of Task.Run to prevent such issues

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/cpu-starvation.png?raw=true" alt="cpu-starvation.png" width=700; height=600>

#### Thread Safity
This means that different threads can access the same resources without exposing erroneous behavior or producing unpredictable results.

**Three Ways to Achieve Thread Safety**:
1. Design a class that is inherently thread-safe.
2. Implement thread safety when using a class designed without thread safety in mind.
3. Utilize a flag within a class to toggle between thread-safe and non-thread-safe behavior. 

**Thread-Safe Objects in .NET Core**:
1. **Immutable Objects**: Objects whose state cannot be changed after creation, ensuring thread safety by design.
2. **ConcurrentDictionary<TKey,TValue>**: A thread-safe collection of key/value pairs accessible by multiple threads concurrently.
3. **ConcurrentQueue<T>**: Thread-safe implementation of a first-in, first-out (FIFO) queue.
4. **ConcurrentStack<T>**: Thread-safe implementation of a last-in, first-out (LIFO) stack.
5. **BlockingCollection<T>**: Provides blocking and bounding capabilities for thread-safe collections.
6. **OrderablePartitioner<TSource>**: Represents a way to split an orderable data source into multiple partitions.

**Non-Thread-Safe Objects in .NET Core**:
1. **ArrayList and Hashtable**: These classes provide some thread safety through the Synchronized property but are not scalable and can lead to performance degradation.
2. **List<T> and Dictionary<TKey,TValue>**: Classes in the System.Collections.Generic namespace that do not provide inherent thread synchronization, requiring manual synchronization when used concurrently.

**Optional Thread-Safe or Non-Thread-Safe Objects in .NET Core**:
1. **Lazy<T>**: Provides support for lazy initialization.

#### Synchronization
Control the computations of multiple threads to access any shared resource (protect access to resources that are accessed concurrently)

#### User mode
User mode is a restricted operational state where software has limited access to system resources. 
It is where normal applications run, and any crashes typically affect only the faulty process, not the entire system.
* Extremely **fast and light**
* Does not switch to kernel mode
* Only **in-process**

#### Kernel mode
Kernel mode is a privileged operational state where software enjoys unrestricted access to hardware, memory, and other system resources.
It allows processes to execute critical operations like managing I/O hardware and memory. However, any crashes in kernel mode can bring down the entire system.
* It is a wrapper around OS **Kernel API**
* It is **slow** because of the switching between kernel and user mode.
* **Cross Process** or **Inter Process** (Kernel mode works at the OS level and is not limited to an internal process)
  
#### Hybrid mode
It uses both user mode and kernel mode. First it tries to run in user mode because user mode is faster and lighter than kernel mode. Whenever necessary, it switches to kernel mode to perform tasks that require cross-process access.
* Hybrid Mode is optimized and fast.
* Hybrid Mode synchronization primitives are **In-Preocess**.

#### Exclusive Locking
An exclusive lock allows only one thread to enter the lock block at a time, providing exclusive access to shared data.

#### Non-Exclusive Locking 
A non-exclusive lock permits multiple threads to enter the lock block and read or write simultaneously.

####  Thread Affinity
**Thread affinity in synchronization context means**, when a thread locks a critical section, it is the only one that allowed to access and unlock it. **Using an async method in a lock block can cause issues** like **context switches that disrupt proper lock release**.

#### We have the following ways for achieving synchronization:
* Blocking constructs - block thread execution and make it wait for another thread or task to complete, e.g. Thread.Sleep, Thread.Join, Task.Wait
* Locks - limits number of threads that can enter / access a “critical section” of code. In this category we have exclusive locks (allows only one thread) and non-exclusive locks (allows a limited number of threads)
* Signals - thread can pause and wait until a notification is received from another thread
* Nonblocking constructs - protects access to a common field

#### Synchronization Primitives

|#| Locking Name           | Locking Mode | In or Cross Process | Functionality Mode | Exclusive or Non-Exclusive | Thread Affinity | Timeout Support| Recursive & Nestead | Description |
|-- | ---------------------- | ----------- | ------------------- | ----------------- | ---------------------- | -------------- | ------- | ------- | ----------- |
|1| Monitor               | Hybrid Mode   | In Process          | Locking & Signaling | Exclusive  | YES        | YES      |      | Provides a mechanism that synchronizes access to objects |
|2| SemaphoreSlim         | Hybrid Mode   | In Process          | Locking | Non-Exclusive | NO | YES      |      | A lightweight alternative to Semaphore that limits the number of threads that can access a resource |
|3| SpinLock              | User Mode   | In Process          | Locking           | Exclusive              |            | YES      |      | A lock that uses spinning instead of context switching to protect a shared resource |
|4| Interlocked           | User Mode   | -   | Lock-Free            |  -  |   -   |  -   |   -   | Provides atomic operations for variables that are shared by multiple threads. |
|5| Mutex                 | Kernel Mode  | Cross Process         | Locking            | Exclusive     | YES        | YES      | YES     | Stands for “mutual exclusion” |
|6| Semaphore             | Kernel Mode  | Cross Process         | Locking            | Non-Exclusive              | NO         | YES      |  NO    | Allows setting a limit on the number of threads accessing a critical section |
|7| Barrier             | Hybrid Mode  | In Process         | Signaling            | Non-Exclusive   |  NO   | YES      |    | Enables multiple tasks to cooperatively work on an algorithm in parallel through multiple phases |
|8| Volatile | User Mode  |      -     | Lock-Free            |    -   |  -   |    -   |  -  | Enables multiple tasks to cooperatively work on an algorithm in parallel through multiple phases |
|9| CountDownEvent | Hybrid Mode  | In Process         | Signaling            | Exclusive   |      | YES      |   -   | Ensures direct memory access for reads and writes, bypassing caching and prevents compiler and jitter optimizations on the variable. |
|10| AutoResetEvent | Kernel Mode  | Cross Process (Only using EventWaitHandle) | Signaling            | Exclusive              |  -    | YES  | YES     | Represents a thread synchronization event that, when signaled, releases one single waiting thread, and the event resets automatically |
|11| ManualResetEvent  | Kernel Mode  | Cross Process         | Signaling            | Non-Exclusive  | - | YES |   YES   | Represents a thread synchronization event that, when signaled, must be reset manually |
|12| ManualResetEventSlim             | Hybrid Mode  | In Process         | Signaling            | Non-Exclusive   |     | YES      |    | This class is a lightweight alternative to ManualResetEvent |
|13| ReaderWriterLock 	|          	|  	    	| Locking 		|          |            |  YES		|          | Not Recomended (Use Slim Version Instead) _ Defines a lock that supports single writers and multiple readers.| 
|14| ReaderWriterLockSlim 	| Hybrid Mode 	| In Process 		| Locking 		|              |            |   Yes 	|      | A lock that protect a resource that is read by multiple threads and written to by one thread at a time |

#### Synchronization Libraries

#### Concurent Collections

#### Tips and Best Practice
* Avoid the need for synchronization, if possible. This is especially true for heavily used code. For example, an algorithm might be adjusted to tolerate a race condition rather than eliminate it. Unnecessary synchronization decreases performance and creates the possibility of deadlocks and race conditions. So **use locking mechanism if necessary** (1. More than one thread is required 2. Shared data exists. 3. Required to modify shared data)
* **Keep the lock block (Critical Section Area) as short and quick as possible**. Locking can **degrade concurrency** if locks are held for too long. This can also **increase the chance of deadlock**.
*  **Make static data thread safe by default**.
*  **Do not make instance data thread safe by default**. Adding locks to create thread-safe code **decreases performance**, **increases lock contention**, and **creates the possibility for deadlocks** to occur. In common application models, only one thread at a time executes user code, which minimizes the need for thread safety. For this reason, the .NET class libraries are not thread safe by default.
*  **Avoid providing static methods that alter static state**. In common server scenarios, static state is shared across requests, which means multiple threads can execute that code at the same time. This opens up the possibility of threading bugs. Consider using a design pattern that encapsulates data into instances that are not shared across requests. Furthermore, if static data are synchronized, calls between static methods that alter state can result in deadlocks or redundant synchronization, adversely affecting performance.

#### volatile keyword
In C#, the volatile keyword ensures that reads and writes to a variable go directly to memory, bypassing caching. This guarantees data freshness in a uniprocessor system. In a multiprocessor system, volatile reads and writes don't guarantee data staleness. It's crucial for multithreaded programming to maintain data consistency across threads by preventing caching of volatile variables.

The volatile keyword indicates that a field might be modified by multiple threads that are executing at the same time. The compiler, the runtime system, and even hardware may rearrange reads and writes to memory locations for performance reasons. Fields that are declared volatile are excluded from certain kinds of optimizations. There is no guarantee of a single total ordering of volatile writes as seen from all threads of execution. For more information, see the Volatile class.

**Note**
On a multiprocessor system, a volatile read operation does not guarantee to obtain the latest value written to that memory location by any processor. Similarly, a volatile write operation does not guarantee that the value written would be immediately visible to other processors.

#### The volatile keyword can be applied to fields of these types:
* Reference types.
* Pointer types (in an unsafe context). Note that although the pointer itself can be volatile, the object that it points to cannot. In other words, you cannot declare a "pointer to volatile."
* Simple types such as sbyte, byte, short, ushort, int, uint, char, float, and bool.
* An enum type with one of the following base types: byte, sbyte, short, ushort, int, or uint.
* Generic type parameters known to be reference types.
* IntPtr and UIntPtr.

Other types, including double and long, cannot be marked volatile because reads and writes to fields of those types cannot be guaranteed to be atomic. To protect multi-threaded access to those types of fields, use the Interlocked class members or protect access using the lock statement.

The volatile keyword can only be applied to fields of a class or struct. Local variables cannot be declared volatile.

**Example**
The following example shows how to declare a public field variable as volatile.
```csharp
class VolatileTest
{
    public volatile int sharedStorage;

    public void Test(int i)
    {
        sharedStorage = i;
    }
}
```

The following example demonstrates how an auxiliary or worker thread can be created and used to perform processing in parallel with that of the primary thread.

```csharp
public class Worker
{
    // This method is called when the thread is started.
    public void DoWork()
    {
        bool work = false;
        while (!_shouldStop)
        {
            work = !work; // simulate some work
        }
        Console.WriteLine("Worker thread: terminating gracefully.");
    }
    public void RequestStop()
    {
        _shouldStop = true;
    }
    // Keyword volatile is used as a hint to the compiler that this data
    // member is accessed by multiple threads.
    private volatile bool _shouldStop;
}

public class WorkerThreadExample
{
    public static void Main()
    {
        // Create the worker thread object. This does not start the thread.
        Worker workerObject = new Worker();
        Thread workerThread = new Thread(workerObject.DoWork);

        // Start the worker thread.
        workerThread.Start();
        Console.WriteLine("Main thread: starting worker thread...");

        // Loop until the worker thread activates.
        while (!workerThread.IsAlive)
            ;

        // Put the main thread to sleep for 500 milliseconds to
        // allow the worker thread to do some work.
        Thread.Sleep(500);

        // Request that the worker thread stop itself.
        workerObject.RequestStop();

        // Use the Thread.Join method to block the current thread
        // until the object's thread terminates.
        workerThread.Join();
        Console.WriteLine("Main thread: worker thread has terminated.");
    }
    // Sample output:
    // Main thread: starting worker thread...
    // Worker thread: terminating gracefully.
    // Main thread: worker thread has terminated.
}
```

#### References
1. https://learn.microsoft.com/en-us/dotnet/standard/threading/overview-of-synchronization-primitives

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
## Relational Databases
## Garbage Collection
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
## System Design and Architecture
### Domain-Driven Design (DDD)

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/ddd.jpg?raw=true" alt="DDD" width=700; height=700>

Writing software involves software architects and programmers. They understand software concepts, tools and implementation details. But they may be disconnected from the business and hence have an incomplete understanding of the problem they're trying to solve. **Domain-Driven Design (DDD) is an approach towards a shared understanding within the context of the domain**. 

**Large software projects are complex. DDD manages this complexity by decomposing the domain into smaller subdomains**. Then it establishes a consistent language within each subdomain so that everyone understands the problem (and the solution) without ambiguity. 

DDD is object-oriented design done right. Among its many benefits are better communication, common understanding, flexible design, improved patterns, meeting deadlines, and minimizing technical debt. However, **DDD requires domain experts, additional effort and hence best applied for complex applications**.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/ddd-concepts.png?raw=true)

#### There are two main phases in DDD

1. **Strategical design phase**
 Includes the strategic principles and methodologies for analysing and modeling domains as well as organised techniques for forming the development process.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/ddd-strategic-design-phase.png?raw=true)
  
2. **Tactical design phase**
Comes after the strategic phase and focuses on the refinement domain model to the point where it can be translated into working code.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/ddd-tactical-design-phase.png?raw=true)

#### Ubiquitous Language:
One of the most important aspects is clear communication and to handle the communication better, it promotes Ubiquitous language which is a language shared between the development teams and domain experts.
It is the language used in discussions, domain model, code of the application, classes and methods.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/ubiquitous-language.jpg?raw=true)

If the development team and business team don’t work together in improving this language, they will result in two different languages which will introduce language barriers that can cause inaccuracies and technical misinterpretation in the application.

for example, the term booking can be referred to a reservation of a seat or it could also mean punishment by a referee in a soccer match for foul play. so depending on the context the meaning is different and it is important to define the meaning and the term being used in large scaled applications with in the context.

The main goal is to close the gap between domain, problem, and detailed technical knowledge and to keep the well-known user programmer gap as small as possible in a way where domain experts and developers can collaborate effectively with minimal misunderstandings and arguments.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/ubiquitous-language2.png?raw=true)

#### E-Commerce Sample

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/ddd-problem-space.png?raw=true)

#### Three Types of Subdomains in DDD 
1. **Core Domain**: Represents the unique value and essence of the business, requiring advanced DDD techniques for competitive advantage.
2. **Supporting Domain**: Provides necessary support functions that complement the core domain, utilizing less complex DDD techniques for efficiency.
3. **Generic Domain**: Encompasses common functionalities applicable across industries, focusing on reusability and adaptability without the need for intensive DDD techniques.

![alt text](https://github.com/hosgha/Interview/blob/master/assets/images/bounded-context-subdomains.png?raw=true)


#### Bounded context
Sometimes applications can be bounded to multiple domains like delivery, shopping and packaging, or sometimes can be very vast domains like food or transport. So to understand what exact area in the domain, you can divide the domain into different zones which are called Bounded Contexts.

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/bounded-context2.png?raw=true" alt="Deadlock" width=600; height=400>

#### Context Map

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/context-map.png?raw=true" alt="ContextMap" width=800; height=650>

A Context Map is the integration of all the domain models in the systems. Each model might have been developed independent of each other. Over the time the proper integration needs to be done in order to make the system to work from end to end.

For example, an online-retail store company might have one system putting in orders, one for inventory, one for shipping (including tracking), one for payments, etc. Here combination of everything makes the stores business efficient and complete.

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/ddd-context-map.png?raw=true" alt="ConextMap" width=500; height=400>

**Integration Patterns** </br> 
Here is the list of DDD integration patterns in no particular order: **Customer/Supplier**, **Shared Kernel**, **Open Host Service**, **Published Language**, **Anticorruption Layer**, **Conformist** and **Separate Ways**.

The integration patterns can be aligned on two axes. The first is how good the involved teams communicate and adhere to the commitments they make. The second is how much control you have over the involved systems. When deciding on which pattern to use it is helpful to keep these in mind. The following introductions to the different patterns include a hint on where the pattern is located on the axes.

1. **Customer/Supplier** </br>
In the customer/supplier pattern, as the name implies, one context is the supplier of data or functions to the other. In planning sessions, the teams act according to their role, negotiate deliverables and schedule.
Because the supplier implements functionality the customer needs, the same rules apply as for an external customer to the business. The customer needs to be available for questions the supplier team may have.
On the other hand, the customer is king. Their needs do have to have priority for the supplier team. Otherwise, the customer team may be blocked and cannot continue to deliver value to the company.
Level of communication and commitment: Medium
Level of control over the involved systems: Medium

3. **Shared Kernel** </br>
When two contexts seem to have a common set of entities they may want to use a shared kernel. Both teams need to be willing to cooperate with and regard each other’s needs.
A shared kernel should include both model and data persistence. It should be automatically tested on each change with suites from both teams to ensure compatibility.
With the shared kernel duplication can be reduced and we can easily integrate contexts. However, big commitment is needed from the teams because they cannot change the kernel freely.
Level of communication and commitment: High
Level of control over the involved systems: High

3. **Open Host Service** </br>
When we need to integrate a bounded context with many others, it can be useful to build a common model for all integrations. This model is published as a set of services that the other contexts use.
It is only feasible to implement an open host service when we can find a common model, and the other contexts are willing to accept it. Of course, each consuming context can build an anti-corruption layer on his end, but this defeats the use of the open host service somewhat.
Level of communication and commitment: High
Level of control over the involved systems: Medium

5. **Published Language** </br>
Further development of the open host service may lead to (the use of) a published language that has it’s own bounded context. The language could be a model defined by some industry association or state for example.
As source context, we may translate into the published language and out of it if our model doesn’t match. We provide our services in the published language.
Level of communication and commitment: High
Level of control over the involved systems: Low

5. **Conformist** </br>
With the conformist integration pattern, we adapt our model fully to the model of the other context we would like to connect. There are two reasons why it may is a good idea to be a conformist.
The first is if the translation from and to the other model would be very complex. It could be complex because we have no control over the other context for example. Alternatively, it is a very different context that is naturally difficult to translate into our own.
The second reason is if the other context is based on a common standard or component. Most probably the model of this context is very mature in its area. Your model may didn’t get this far yet.
Level of communication and commitment: Low
Level of control over the involved systems: Low

7. **Anticorruption Layer** </br>
If we have no control over the context we would like to connect to, and its model doesn’t fit ourselves an anticorruption layer should be considered. This layer communicates with the other context in its language and translates from and to it.
The anticorruption layer can be especially useful when migrating a legacy system. It encapsulates the legacy system, and our new shiny solution communicates only with this layer in a clean language.
Level of communication and commitment: Low
Level of control over the involved systems: Low

7. **Separate Ways** </br>
Because integration always has an associated cost you may want to go separate ways instead. Maybe you rather duplicate some logic and data in your own context than build a complex integration layer.
The two contexts may still be connected through a middleware tire or on the GUI level. However, take care not to connect them on a model level accidentally.
Level of communication and commitment: Low
Level of control over the involved systems: Low

**Wrap Up / Final Thoughts** </br>
I think the benefit of context mapping is very obvious. It is beneficial for teams if they know their relationship to other parts of the software system they build.

Maybe the integrations between different contexts don’t always follow exactly one of the patterns. I think they can be altered or even combined at times.



#### Entity
An entity is a class with business logic, uniquely identified by an ID or attributes, maintaining consistent identity throughout its existence.

#### Value Object
Value Objects are **immutable** and **do not have a unique identity**, are **defined only by the values of their attributes**. Value Objects are employed when there is a need to encapsulate specific values required for a business application, ensuring immutability, simplifying business logic, ensuring data validity, and increasing modularity for better code quality and readability

For example:
Person: is an entity.
Address: is a value object; because 2 people can have same address.

**Rules of Value Object**: </br>
1. **Immutability**: Value Objects are immutable, meaning their values cannot change once the object is created. To modify a value, a new object must be created, promoting simplicity and thread safety
2. **No Identity**: Value Objects lack a unique identifier and are compared based on their values rather than an identity field. This distinguishes them from entities and emphasizes value-based comparisons
3. **Lifetime Shortening**: Value Objects require a parent entity to exist, as they cannot stand alone. This relationship ensures that value objects are always associated with an entity, leading to a composition-based structure and preventing separate tables in databases

#### Aggregate
A collection of objects that are bound together by a root entity, otherwise known as an aggregate root. The **aggregate root guarantees the consistency** of changes being made within the aggregate by forbidding external objects from holding references to its members. The idea of an aggregate is to guarantee consistency, being the root responsible for data integrity and forcing invariants.

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/ddd-aggregate.png?raw=true" alt="Deadlock" width=600; height=400>

**Aggregate Root**: </br>
1. An aggregate can only be accessed through its aggregate root.
2. The aggregate root is an entity and cannot be a value object.
3. The aggregate root has a global identity that is unique throughout the application. 
    
#### Invariant
A business invariant is a rule or constraint in a business domain that must always hold true.

<img src="https://github.com/hosgha/Interview/blob/master/assets/images/ddd-invariant.png?raw=true" alt="Deadlock" width=800; height=300>

#### Domain Event
A domain object that defines an event (something that happens) and is an event that domain experts care about.

#### Service
Services can be categorized into three types in domain driven design.

1. **Domain Services** </br>
Domain Services contain operations, actions, or business process and provides the functionality that the domain needs. It deals with all the domain related manipulation.
An example of domain services are catalog service for ecommerce domain which deals with all the catalog related information or account service in accounts domain which deals with all information related to accounts.

3. **Application Services** </br>
Application Services are the services used by the outside world which may have representations of data. Example of application service is a database CRUD operation.

4. **Infrastructure services** </br>
An Infrastructure Service is service that communicates directly with external resource . For example, accessing file system, registry, SMTP, database etc in the application.

#### References
1. https://martinfowler.com/bliki/DomainDrivenDesign.html 
2. https://medium.com/@mazraara/the-building-blocks-of-domain-driven-design-ddd-af745a53a9eb
3. https://ddd-practitioners.com/category/ddd/
4. https://devopedia.org/domain-driven-design
5. https://opus.ch/ddd-concepts-and-patterns-context-map/
    
## Cloud


