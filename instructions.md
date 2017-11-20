# Project 3: original data analysis

As discussed in class, project #3 will be a free-form version of work along the lines of what you did in project #2.  The goal of the project will be to develop a complete analysis of a dataset that you find online, ask some interesting questions from it, and share your complete set of results in a well documented manner, using the practices we've been developing during the course.


## Team setup and logistics

**Due date:** the last commit should be no later than *Wednesday December 13th, at 11pm local (Pacific) Time*.

**Teams:** the project is to be completed with the same team of three that you used for hw 3, the dataset selection.

**Team names:** use the same team name as for hw3: your repo should be named `p3-XX-YY-ZZ`, where XX, YY and ZZ are the first two letters of each member's last name.

## Project deliverables

### Data

Depending on the size of your data, you may choose to include it in the repository or not (use your judgment - up to a few dozen megabytes it's not a problem, something in the Gigabyte range is too big to put into a repo). If the data isn't  included locally, your code should access it remotely and cache it adequately for subsequent executions.  If you don't include the data in the repository, consider the implications of doing so for long-term reproducibility: is the source you are using a reliable one? Will it be there in 10 years?


### Functional structure of your code and testing

You should identify steps amenable to be put into standalone functions and write a proper function for those, with a complete docstring describing their inputs, as I've shown in some of our examples (the Numpy project offers [detailed examples of high-quality docstrings](http://www.sphinx-doc.org/en/stable/ext/example_numpy.html)). 

You may choose to put a few analysis functions into a pure python file that you import separately, make the choice that you find cleanest/most fluid for your workflow.

Whether you do it in a notebook or python scripts, make sure to write at least a few test for utility functions that you write.

**Note:** this is a *requirement*. You must structure your code to include at least two functions, that you test and document properly (feel free to use more as your analysis dictates).


### Analysis notebooks and supporting code

Break down your analysis into as many notebooks as is reasonable for convenient reading and execution. There is no hard and fast rule for this, just as there isn't for how many paragraphs or figures a good scientific paper should have. You should consider readability, execution time, total notebook length, etc, as criteria in your decisions.  [This essay](http://blog.wolfram.com/2017/11/14/what-is-a-computational-essay) by Stephen Wolfram, the creator of Mathematica (part of the inspiration for the Jupyter Notebook) has some good thoughts on what makes a well written computational narrative.

Consider how to "chain" your analyses with intermediate results being stored so they don't need to be recomputed from scratch each time. Also, be mindful of saving key figures you may want to reuse in your report to disk, so the main narrative notebook can reuse them for display and discussion.  Look back at the instructions for project 2 if you need a refresher.


### Main narrative notebook

Write a `main.ipynb` notebook that summarizes and discusses your results. It can contain figures referenced from disk or simple summary information (for example if you want to display part of a dataframe) from variables read from disk, but *no significant computations at all*. Think of this as your "paper".

Discuss the assumptions you can make about the data to justify your analysis.  You have no control over the original data acquisition and measurement, and for many of you this project will likely fall under the broad purview of *Exploratory Data Analysis*.  If you propose any statistical hypothesis/model in your analysis, discuss your justifications, considering how the data was acquired.

Your final report, when completed, may well diverge your initial plan as submitted in hw3. Discuss any changes you made from this plan and why you chose to pursue new questions or modify your original ones.

**Author Contributions section:** your `main.ipynb` notebook should contain, at the end, a brief section titled *Author Contributions*. This section should indicate, for each team member, what they did in the project. It doesn't have to be a long, detailed story, a few sentences per person should suffice.  All team members must agree to the language in this section.  (By the way, this is standard practice in many scientific journals).  While in principle the project grade is the same for all team members, we reserve the right to lower the grade of anyone who doesn't contribute to the team effort.


### Reproducibility support

* Environment: like in Projects #1 and #2, provide an `environment.yml` file that creates an environment with all necessary dependencies to run your analysis.

* `Makefile`: you will also create a `Makefile` with `env` and `all` targets, similar to that of Project #1. The `env` target should make the environment with all necessary libraries, `all` should run all notebooks.

* Don't forget to control your random seeds for anything that has a stochastic component.


### Good repository practices

* `README.md`: see instructions therein.

* `LICENSE`: you should explicitly state which licensing conditions apply to your work (see [Github's help](https://help.github.com/articles/adding-a-license-to-a-repository/)). I strongly suggest looking at Victoria Stodden's [ENABLING REPRODUCIBLE RESEARCH:
LICENSING SCIENTIFIC INNOVATION](https://web.stanford.edu/~vcs/papers/ijclp-STODDEN-2009.pdf). For a short summary, her [slides](https://web.stanford.edu/~vcs/talks/VictoriaStoddenCommuniaJune2009-2.pdf) can be useful. She suggests a "Reproducible research standard" that licenses code, data and text/media materials in comparable terms that maximize resharing potential while providing due credit guarantees for the original authors.

* `.gitignore`: provide a git ignore file that prevents the automatic inclusion of unwanted files.  This also helps you avoid noisy `git status` output that lists things you know you won't actually want to put under git's control.
