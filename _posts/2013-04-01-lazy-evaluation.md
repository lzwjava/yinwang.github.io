---
layout: post
title: "Lazy Evaluation"
---


You may have seen in some of the previous articles that Haskell actually has quite severe problems, but these problems have not received sufficient attention. The problems I see with Haskell are:

- Complex syntax based on indentation, making it inefficient for any editor to edit Haskell programs and increasing the difficulty of parsing. For this opinion, please refer to my article "Speaking of Syntax" and my English article "Layout Syntax Considered Harmful".

- The "pure functional" semantics and monads are not good things. For this, please refer to the article "Misconceptions about Functional Languages".

- The Hindley-Milner type system used in Haskell actually contains a fundamental error. For this, please refer to "The Fundamental Error of the Hindley-Milner Type System". I. Haskell's type classes are not fundamentally different from overloading in general-purpose languages like Java. The apparent differences are due to the Hindley-Milner system and overloading being combined. Type classes cannot do more than overloading in other languages.

II. However, I will add a straw man to this issue: Haskell's lazy evaluation method significantly reduces its running efficiency and contradicts the goal of parallel computing.

III. Lazy evaluation allows us to have two possibilities for a variable's value: 1) the variable has already been evaluated, so its value can be directly taken 2) the variable has not been evaluated yet, meaning it is a thunk, and we must initiate its evaluation.

IV. This brings about type system confusion. Any type, be it Int, Bool, List, ... or custom data types, has an additional component: thunk. It represents "calculation yet to be evaluated." Haskell programmers usually call it "bottom," written as _|_. It means: deadlock. Since any thunk can 1) return a value of a predefined type, or 2) cause a deadlock.

V. This is somewhat similar to null pointers in C++ and Java, as null can be used as any other type but lacks the features of that type, leading to unexpected issues. The problems _|_ brings to Haskell are not as severe, but unpredictable, hard to analyze, and debug. For Haskell, there is a possibility of occurrences such as: you write a small function, thinking it should not take much time. However, because it accesses the value of a certain variable, it unintentionally triggers a lengthy piece of code, making you wait indefinitely for a return. Finding the issue becomes difficult as this function neither directly nor indirectly calls the time-consuming code; instead, the code is initiated by the thunk of the variable. This makes analyzing the program's efficiency challenging: calculations "lazily" waiting in the wings may unexpectedly explode. This is what is referred to as "burning incense only when necessary." This uncertainty didn't bring about an increase in overall computation costs. However, "laziness" brought about enormous costs on the other hand, which is the cost of "asking questions." Whenever Haskell encounters a variable, it asks it a question: "Have you been evaluated yet?" Even if this variable has already been evaluated and retrieved a hundred thousand times, Haskell still asks this question: "Have you been evaluated yet?" Asking a variable this question may not be a problem, but Haskell asks almost every variable this question repeatedly. This accumulates into a huge cost. This kind of problem is similar to the "interpretation overhead" I talked about in another blog post, and it's a "runtime" problem, so it can't be optimized away by the compiler.

It's ironic that this "pure functional language," Haskell, requires all the thunks for lazy evaluation to have "side effects," so they must be kept in memory rather than in registers. If you understand what I wrote in my blog post "Misconceptions About Functional Programming," you'll find that even C programs have fewer side effects than Haskell. As a result, the processor's registers are not effectively utilized, leading to a significant increase in memory access. I can confidently tell you this because I once designed a register allocation algorithm, so during a meeting I asked the GHC implementers, "Would you be interested in a new register allocation algorithm I could add to GHC for you?" They replied, "We don't need it, because Haskell is full of thunks, and there's hardly any opportunity to use registers."

Therefore, asking too many questions prevents effective use of registers, making Haskell less efficient.

Now let's look at why lazy evaluation conflicts with the goal of parallel computing. This is quite clear, as the reason lies in the definition of "lazy evaluation." Lazy evaluation says: "Calculate me when you need me." Parallel computing says: "When you're needed, it's best if you've already been computed by some processor." So you can see, parallel computing requires you to be "diligent" and prepare in advance, while lazy evaluation is inherently "lazy" and unlikely to do so beforehand. Since this conflict arises from the definition of "lazy evaluation," it is an irreconcilable contradiction.

Thus, lazy evaluation reduces efficiency both in serial processing and in parallel processing, making it an irrelevant language feature. Though lazy evaluation itself cannot bring us direct benefits, the theories behind it can inspire other designs. If you really want to understand the principles of lazy evaluation, you can first take a look at my explanation of it. See how you can implement the essence of Haskell semantics in less than 40 lines of code:

<https://github.com/yinwang0/lightsabers/blob/master/interp-lazy.rkt>