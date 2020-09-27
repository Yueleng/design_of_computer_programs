# Theory and Practice

## Theory

pattern and grammar which describe language.
We learnt interpretors over those languages and also compilers which can do the same thing
only faster.

## Practice

Regular expressions are useful for all sorts of things.
And they are concise language for getting work done.

We learnt that intepretors and compilers can be valueble tools. They can be more expressive and more natural to describe a problem in terms of native language that makes sense for the problem rather than in terms of Python code that doesn't necessarily make sense.

We learnt functions are more composable than other things in python. For example, in Python we have expressions and we have statements. They can only be composed by the Python programmer whereas functions can be composed dynamically. We can take two functions and put them together. f(g(x)). We can't do that we expressions and statements. We can do with values of expressions, but we can't do with expressions themselves.

Functions provide a composability that we don't get elsewhere.

Functions also provide control over time, so we can divide up the work that we want to do some now and so some later. Expressions and statements don't do that because they just get done at 1 time when they are executed. Functions allow us to package up computation that we want to do later.