---
layout: post
title: "Language Design Mistake 2"
---

I. Programming Language Design Flaws (2) - Trying to Accommodate the World

In a previous article, I discussed a common design flaw in programming languages: the tendency to pursue brevity at the expense of other considerations, which led to a series of historical design errors. Today, I will talk about another design flaw, one that has caused numerous issues and continues to do so.

This design flaw is called "trying to accommodate the world." This flaw is responsible for various problems in languages like Python, Ruby, and JavaScript. I have written a static analyzer for Python, so I have a good understanding of its semantics. While designing this static analyzer, I found that Python's design makes static analysis exceptionally difficult. Python programs are hard to diagnose when they encounter issues, and Python's execution speed is slower than most programming languages, which is largely due to Python's own design issues. These design issues are largely rooted in the same design tendency: "trying to accommodate the world."

In Python, every "object" has a "dictionary" (dictionary). This dict contains the mapping relationship between the object's fields and their values, essentially functioning as a hash table. In most languages, you are required to declare these names and specify their types beforehand. However, Python does not work this way. In Python, you can define a person, and this person's fields may include "name," "head," "hands," "feet," and so on.

However, Python believes that programs should be able to create or delete these fields at any time. Therefore, you can add a new field to a specific person, such as a "third hand." You can also delete one of its fields, such as "head." Python thinks this is more in line with the way the world works, as some people may not have a head, while others may have an extra hand. I see, this is really convenient. Then you come across such a problem: you need to put a hat on every person in this world. While writing this code, you assume that everyone has a head, so you write a function called putOnHat which takes any person as input and puts a hat on their head. You then want to map this function to the collection of people in a country.

However, you didn't anticipate that due to Python's ability to describe the world, other coders would create all sorts of unexpected creatures. For instance, headless people, or those with three hands, six eyes, and so on. No matter how you write your putOnHat function, it always produces the unexpected. You're surprised to find that there are indeed headless people! The most tragic part is that after spending several months and a considerable amount of energy putting hats on millions of people, the program crashes due to an encounter with a headless person. Even though you know there's a bug, it's difficult to find these headless people because they came from various convoluted paths and took many turns. To reproduce this bug, you have to wait for several months, and it might not even occur.... This is what they call a Higgs-Bugson.

What can be done? So you came up with a solution: keep "normal people" in a separate list, and handle the other creatures differently. You'd like a way to prevent others from putting those creatures in this list. What you really want is Java's "type" system:

List<PersonWithOneHeadAndTwoHands> normalPeople;

Unfortunately, Python doesn't provide you with this mechanism because, according to Python's philosophy, it's not extensive enough to accommodate this world's vast and intricate variations. Having programmers manually write types for parameters and variables is considered "too much labor." This issue exists in JavaScript and Ruby as well.

Language designers should be aware that a programming language is not for "constructing the world," but only for simple simulation. The tendency to encompass the world has brought little benefit and hasn't saved programmers much energy, yet it has made the code completely ruleless. It's like living in a world without rules, institutions, or laws, where unexpected things happen constantly, and there are people running around with three hands and six eyes. This is an endless source of frustration and a waste of time and energy.