---
layout: post
title: "What is "user-friendly"?"
---


When I mention a tool being "unfriendly to users," I am often met with disdain. Is this what they call "treating others the way they treat themselves"? I remember when people complained about Linux or TeX being unfriendly back then, and I probably had a similar attitude. Now when I point out TeX's flaws and propose new solutions, I often see an American student roll their eyes and say, "Newbies complain about tools being hard to use because they don't know how. LaTeX is 'wYsiWyg,' so it's not like Word."

Little do they know, the "newbie" in front of them had already mastered TeX's configuration, read TeXbook twice, completed all the "double bend" exercises, and could write macros in TeX's language. Yet they were labeled as "newbies," an intriguing issue. So, putting aside personal feelings, let's discuss the reasons behind this "disdain" phenomenon and what constitutes "user-friendly."

First, let's analyze this phenomenon from a psychological perspective. The apparent reason why some people overlook the fact that something is "unfriendly to users" and label complainers as "newbies" is "superiority complex." If everyone could do something, how could I showcase my extraordinary intelligence? So, I choose the most difficult, cryptic, and sophisticated things to master, and once I've done so, I am hailed as a "master," looking down upon others. I must admit, I had similar thoughts in the past. Since my undergraduate days, I've pondered what sets computer science students apart from non-computer science students. It took me many years to find the answer (which I'll share later). However, I made a mistake that many people share: equating "difficulty" with "intelligence" or "professionalism." But the truth is, someone using a difficult tool does not necessarily possess extraordinary intelligence or greater professionalism.

Unfortunately, I found that very few people in the world understand this logic. In universities and companies, people proudly proclaim their mastery of difficult tools. This isn't limited to computer systems; it also applies to mathematics and abstract subjects. I often hear people boast, "I'm going to use XX logic to design a formal system..." However, these people only know the surface of this logic. They can use it, but they don't realize that all the confusing and cryptic rules can be derived using simpler and more straightforward methods.: Lovecraft said: "Any idiot can face a problem more complex. It takes a touch of genius - and a lot of courage to move in the opposite direction." I deeply understand the meaning of this quote. To simplify something to make it more "user-friendly," you indeed need a great deal of courage. You must intentionally ignore some details of this thing. However, since the people around you don't understand this principle, they will consider you incompetent or foolish. Even if you succeed, it may be difficult to convince them to try the simplified version of this thing.

Now let's talk about what "user-friendly" means. How do we define "user-friendly"? How can we precisely judge whether something is user-friendly? I think this is a concept that is still quite hazy, but the design philosophy of programming languages, especially type theory, can explain it fairly well. We can view machine and human as one system:

1. This system consists of multiple modules, including machine modules and human modules.

2. The interfaces between machine modules use usual programming interfaces.

3. The interface for human-machine interaction is the interface between machine modules and human modules. I. Each interface must provide a certain level of abstraction to prevent the user from obtaining unwarranted details. This user could be a machine module or a human module.

II. Abstraction makes the system extendable. Since if the interface remains unchanged, the modifications to the modules will not require any changes to the user.

Within a machine's various modules, abstraction manifests as the types (or interfaces) of functions or methods, a program's module definitions, operating system system calls, etc. However, their essence is the same: they tell the user "what you can do with me." Many programmers are aware of these machine interfaces' abstractness, keeping the user as far as possible from implementation details. However, they often overlook the interface between man and machine. Perhaps they didn't overlook it, but they approached the problem with vastly different design principles. They didn't truly consider people as part of the system, didn't provide a well-abstracted interface for them like they did for other machine modules. They seemed to think people should be able to do more things, so they exposed the complex internal structure of the program (including their own) to people. As a result, people are always confused about "what can I do with this program?" When the program is modified, people often need to change their operations, so the system's extensibility for people is lacking. Generally, programmers consider the extensibility of machine interfaces but neglect the interface's extensibility between man and machine.

For instance, many Unix programs have configuration files, set environment variables, and command-line arguments. Each user must know the name, location, and format of each configuration file, the names and meanings of environment variables, and the meanings of command-line arguments. One program is manageable, but if there are many programs, each in different locations with different named configuration files, and each with a different format, these configurations will confuse people. Often, a program says it can't find a configuration file, look in the manual, the manual says the configuration file's location is determined by the FOO environment variable. After changing the environment variable, it's found that the problem isn't solved. No choice, go to the forum and ask, finally figuring out that the configuration file works only when there isn't a file named ".bar" in the same directory. After finally remembering this rule, the program upgrades, and the rule is changed again, so the user continues to ponder, continues to go to the forum, and so on. Is this called "tinkering"? When will they be able to do their own work?

The configuration of TeX systems is even more complicated. Tens of thousands of small files, few people understand the structure and usage of kpathsea, and it takes a long time to figure it out. But it's only solving a very insignificant problem. TeX's language also has significant issues, making extension difficult. This will be discussed later. A good interface should not be like this. It should provide users with simple settings. Users should set all program parameters in the same way, as they are just a mapping (map) from variables to values. As for where the system stores these settings and how to find them, the specific format, users should not be aware of. This is the same logic as a high-level language's runtime system's memory management. A program requests to create an object, the system receives the instruction and allocates a memory block, initializes it, then returns the object's reference to the program. The program does not know where the object exists in memory, nor should it. The program should not use the object's address for operations.

Therefore, the "unfriendly to users" phenomenon behind it is actually due to the irrational design of the programs, not a user problem. This phenomenon exists in Windows, Mac, iPhone, and Android. For example, almost all iPhone users have been brainwashed into the mistaken belief that "iPhone only needs one button." One button is not enough. Similarly, software like Photoshop, Illustrator, and Flash hide user-required functions and settings, often resulting in irrational categorization, making it difficult for them to find these functions.

As for how to be more user-friendly, it's a complex issue that can't be summarized in a few sentences. Here are some points I've thought about:

1. Unity: Always keep in mind that people are a part of a unified system, not some strange deity. In essence, people can be imagined as a program module.
2. Abstraction: Maximally conceal the implementation of the program, and minimize exposing unnecessary information to other program modules and to people. "Do not impose what you do not want on others.": Provide sufficient and necessary mechanisms for people to complete their tasks.

4: Mechanisms should ideally have minimal redundancy and overlap, maintaining orthogonality.

5: Mechanisms should be composable, striving for only one way to perform the same task.

6: Not all desired functions are necessary, people often deceive themselves, clarify which functions are truly needed.

7: Human input/output includes five senses, although computers typically interact with people only through vision and hearing. 1. Intuition: People think with intuition and models. Information given to people, whether symbolic or graphic, should be easily establish an intuitive model in the human mind, allowing people to efficiently operate them.

2. Context: The capacity of human brain's "cache" is very small. Can you recall the names of seven people at once? Therefore, only operations relevant to the currently focused object should be provided at any given moment, rather than all possible operations for selection. Context menus and keyboard operation tips based on context seem like good ideas.