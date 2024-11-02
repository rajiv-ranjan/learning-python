# Useful References

## Oct-05-2024

### Suggestions for coding practice

* https://exercism.org/
* https://adventofcode.com/ 
* https://www.codewars.com/

### Books

* Start with `Python tutorial` as part of there official documentation
* Must have
  * [Python Distilled](https://www.amazon.in/Python-Distilled-David-M-Beazley-ebook/dp/B094CMKN2J)
* Intermediate level
  * [Robust-Python](https://www.amazon.in/Robust-Python-Patrick-Viafore-ebook/dp/B09982C9FX/)
  * [Fluent-Python](https://www.amazon.in/Fluent-Python-Luciano-Ramalho/dp/1491946008)

### Additional problem to solve for next day

* Covert figures to words
  * handles indian ways like lakhs, crores for less that 100 crores
  * handle western way in million and billion for less than 1 trillion
* Convert roman to number and vice versa

## Oct-06-2024

### Tools

* Debugging tool: [Python Tutor Website](https://pythontutor.com/)

### Books

* [3blue1brown](https://www.3blue1brown.com/) for basic calculus, linear algebra

## Oct-26-2024 - Oct-27-2024

### Tools and Libraries

* Package management for Python: [UV](https://docs.astral.sh/uv/)
* [cocalc](https://cocalc.com/)

* important libs in python
  * itertools are very important
  * accumulate
  * collections

  * polars is a better tool now than pandas

* [graphViz](https://graphviz.org/) can be used to declare the diagram and it creates it. extension is `.dot` file. Python too has a library to create .dot files ie.e [pygraphviz](https://pypi.org/project/pygraphviz/).

### Books

* book on pandas?

## Questions

* where is the association between vs code and virtual env stored?

* matplotlib - is base
* seaborn - statistics
* bokeh - web
* pltly - dashboard
* vega altair - declarative
* mermaid, plantUML - library for diagram

* learn by example scikitlearn https://scikit-learn.org/stable/modules/linear_model.html#
* decision tree can be exported as graphviz: https://scikit-learn.org/stable/auto_examples/tree/plot_iris_dtc.html#sphx-glr-auto-examples-tree-plot-iris-dtc-py

## Nov-02-2024

### Tools

* [pylint](https://pylint.readthedocs.io/en/stable/) can be used in conjunction with other useful tools:
  * [ruff](https://github.com/astral-sh/ruff): really fast, with builtin auto-fix and a large number of checks taken from popular linters, but implemented in rust
  * [flake8](https://github.com/PyCQA/flake8): a framework to implement your own checks in python using ast directly
  * [mypy](https://github.com/python/mypy): typing checks
  * [pyright](https://github.com/microsoft/pyright): typing checks
  * [pylance](https://www.google.com): typing checks
  * [pyre](https://github.com/facebook/pyre-check): typing checks
  * [bandit](https://github.com/PyCQA/bandit): security oriented checks
  * [black](https://github.com/psf/black): auto-formatting
  * [isort](https://pycqa.github.io/isort/): auto-formatting
  * [autoflake](https://github.com/myint/autoflake): automated removal of unused imports or variables
  * [pyupgrade](https://github.com/asottile/pyupgrade): automated upgrade to newer python syntax
  * [pydocstringformatter](https://github.com/DanielNoord/pydocstringformatter): automated pep257
  * pylint ships with below tool OOTB:
    * [symilar](https://pylint.readthedocs.io/en/latest/symilar.html): duplicate code finder that is also integrated in pylint
    * [pyreverse](https://pylint.readthedocs.io/en/latest/pyreverse.html): standalone tool that generates package and class diagrams.
