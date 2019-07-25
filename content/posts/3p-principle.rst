3P Principle: Purpose, Productivity, Performance
################################################

:date: 2019-07-28
:slug: 3p-principle
:tags: principle, programming, language
:image: images/3p-principle.png
:summary: Definition and description of the 3P Principle

.. image:: {static}/images/3p-principle.png
   :alt: diagram of the 3P principle

As programmers, we want programming languages which are efficient, effective and general purpose.
**Is there any language that satisfies these 3 properties ? And can we ever create such language ?**
In this article, I define the 3P Principle and explain its importance in software projects.

Definitions
-----------

**The 3P Principle states that a programming language cannot satisfies these properties at the same time:**

- **(General) Purpose**: a programming language that can be applied to a wide range of problems.
   -  e.g. web programming, computer security, theorem proving, data analysis …

- **Productivity**: a programming language that lets programmers deliver effective program under time constraints.
   -  e.g. dynamic typing, introspection, meta-programming, REPL development …

- **Performance**: a programming language which is fast and efficient to execute on a computer.
   -  e.g. static typing, compilation, manual memory management, unboxed types …

Trade-offs
----------

Let’s focus on the Performance Vs. Productivity trade-off:
   For a language to be **Performant**, it must provide a set of features close to the logic of a computer.

   For a language to be **Productive**, it must provide a set of features close to the logic of a programmer.

   Since the logic of a computer is different from the logic of a programmer, the task of optimizing the Performance and Productivity of a programming language at the same time is not possible.

Historically, some languages like C or Assembly have always been closer to the hardware than other languages like LISPs or Python. On the other hand, LISPs and Python provide many convenient features to their programmers such as dynamic typing and meta-programming.

As simple as it is, this trade-off is not all or nothing. Modern languages like Rust, Haskell or Clojure attempt to balance these two properties.

**The question is: can we succeed in creating a language that satisfies these 3 properties ?**

   To optimize both the Performance and the Productivity of a programming language, the Purpose of a language must the limited to a specific set of tasks.

   By limiting the domain of a programming language, its range of application becomes more essential both for the programmer to use and for the computer to execute.

If we need to consider every possible use cases, I think the problem will remain too hard for humans to solve. We can’t think about every situation in which a programming language can be used.

What can we do instead is to limit our focus, and try to find a good solution on a smaller problem.

Again, the most important requirement we can trade is the general applicability of a programming language. SQL for instance has one and only goal: managing database information with relational algebra. Other Domain Specific Languages (DSL) are created to deal with narrow tasks such as web template, matrix manipulation or logic programming.

**By reducing the scope of a language, the core developers have the opportunity to improve both the performance and the productivity of their language.**

Importance
----------

If ignored, the 3P principle can harm the success chance of a software project.

When I was working as a web developer, my mission was to deliver application features as fast as I can. But as the user base grown, my tasks shifted toward improving the performance of the application.

`Facebook <https://code.fb.com/web/hiphop-for-php-move-fast/>`__ and `Twitter <https://www.infoq.com/articles/twitter-java-use>`__ have attempted to improve the scalability of their website several time, without sacrificing their ability to develop new features. Unfortunately, most programming languages don’t help their programmers in that regard.

**The optimal solution is often to rewrite the application with a different (and often incompatible) language.**

Recently, I’ve been working on a data analysis project to process large datasets. Compared to web programming, a data analysis must be both fast to develop and fast to execute to gather experimental results as soon as possible. Again, few programming languages can address this use case.

Either the programming language is too slow to execute (e.g. Python, R) or too slow to develop (Java, C++). Other languages like Julia try to balance this trade-off, but they are not as general purpose as the languages I listed.

I don’t have a definitive answer to solve this problem, but there is few things that I can suggest:

-  **Create and explore specific purpose programming languages** (e.g. query languages, data pipelines ...).
-  **Embrace the idea of** `Polyglot Programming <https://deanwampler.github.io/polyglotprogramming/>`__ to combine the strength of multiple languages (e.g. TensorFlow relies on C++ for its backend (performance) and Python for its frontend (productivity)).
-  **Remember that** `premature optimization is the root of all evil <http://wiki.c2.com/?PrematureOptimization>`__. It is often more important to explore the edge cases of a problem before committing to optimize specific use case.
-  **Remember that the requirements of a project will change over time**. The ability to adapt to new requirements remains important through the course of a project.
