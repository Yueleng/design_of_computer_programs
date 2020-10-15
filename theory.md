# Theory and Practice

## Theory

pattern and grammar which describe language.
We learnt interpretors over those languages and also compilers which can do the same thing
only faster.

## Practice

* Regular expressions are useful for all sorts of things. And they are concise language for getting work done.

* We learnt that intepretors and compilers can be valueble tools. They can be more expressive and more natural to describe a problem in terms of native language that makes sense for the problem rather than in terms of Python code that doesn't necessarily make sense.

* We learnt functions are more composable than other things in python. For example, in Python we have expressions and we have statements. They can only be composed by the Python programmer whereas functions can be composed dynamically. We can take two functions and put them together. f(g(x)). We can't do that with expressions and statements. We can do with values of expressions, but we can't do with expressions themselves.

* Functions provide a composability that we don't get elsewhere.

* Functions also provide control over time, so we can divide up the work that we want to do some now and so some later. Expressions and statements don't do that because they just get done at 1 time when they are executed. Functions allow us to package up computation that we want to do later.

# Lesson 3 Q&A

* Q: What is the difference between finding state machines as a representation of uderlying engine for regular expressions and our implementation of regular expression?

  * A: There is one-to-one correspondence between a regular expression and finite state machine.

* Q: When you have a really long regular expression, is there any way of dumping out the final set of these low level machine instructions so they can be called later?
  
  * A: One is that within the regular expression module, the re module in Python, there is a compile statement that takes a string in and returns a compiled version of that regular expression. So if you're running your program once, you can compile that regular expression once at the very top of your program then use the compiled expression each time. If you are doing that explicitly, you are all set.

  * If you don't, the regular expression module does most of the work for you. Because what it does is it keeps a little cache. It does something like memoize and keeps the last few reguar expression that's done and says, I've seen this string before. I'll just fetch that compiled object. It does that automatically.

  * Now another thing to think about is between runs of your program. What if you've compiled everthing, and then you don't want to have the startup time of compiling it over again? There is another module called pickle. It takes an object that exists within the running Python interpretor and writes it out to disk in a form that can be read back in.

* Q: Design process in coming up with these lectures and how mistakes figure in there.

  * A: There are all kinds of mistakes, and errors are there.

* Q: How do you decide which of these paradigms to use when approaching a new problem?

  * A: I try to think of things as how can I get as close to the problems as possible? I want to program at the level of the problems. Start analyze the problem and say waht are the pieces of problem, what are the objects I'm going to manipulate them, what are the ways I'm going to manipulate them, and try to do most of the anaylsis at that level. And then, once that anaylsis is done, then I can say, well, what do I have in my programming language? In this way, there is more direct connection between the problem and the solution. Rather than a multistep of going from the problem to the language implementation.