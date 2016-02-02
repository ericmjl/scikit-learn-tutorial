# FAQ

**Q: What is this tutorial about?**

This tutorial is about how to use the scikit-learn API to do machine learning in Python. You will see, through hands-on examples, how to use machine learning algorithms to gain insights onto biological problems. Hands-on coding time will be built into the tutorial. At the end of it, you should be confident enough to use the scikit-learn API, and reason about & visualize your data with the tools taught here.

**Q: What is this tutorial not about?**

This tutorial will not explicitly cover:

1. How particular ML algorithms work.
1. The basics of Python.
1. How to setup your environment (this should have been done by [contacting the instructor][2] before class).
1. How to transform specific data sets to be `scikit-learn` compatible. It is welcome as a question, though.

**Q: What preparation should I have before coming to the workshop?**

In terms of background knowledge, you should be:

*1. Familiar with Python syntax, or at least capable of reading it.* 

Familiarity with other scripting language's syntax is acceptable as well. A few tests in Python are below:

>(1) Provide a plausible data structure for the variables `my_fav_things` and `item` in the list comprehension: `[item['name'] for item in my_fav_things]`.
    
> (2) Given the code block below, what is the value of `i`?

```python
    n = 5
    def power_overwhelming(b):
        return b ** 5

    i = power_overwhelming(n)
```

*2. Familiar with object-oriented programming (OOP).* 

A test to see if you get OOP is to see if you can implement a `Watch` object that has a method `current_time`, which does not accept any parameters, that tells the current time. Do it in your favourite language, need not be Python. 

*3. Able to read API documentation, and read error messages, to debug your code.*

---

In terms of computing environment, you should follow the instructions on the [README.md][1] file.


[1]: README.md
[2]: mailto:ericmajinglong@gmail.com