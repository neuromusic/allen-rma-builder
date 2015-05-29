# allen-rma-wrapper
generates RMA queries using a more pythonic syntax

documentation for the RMA can be found here:

- http://help.brain-map.org/display/api/RMA+Path+Syntax

allen also has a nice builder here:

- http://api.brain-map.org/examples/rma_builder/index.html

This project is pretty bare, but implements the basic functionality to build out an RMA query using more Pythonic syntax, using the double-underscore notation (borrowed from django) to  define filters, along with some (hopefully) sensible defaults.

``` python
    from allen_rma import Q
    print Q(model='Gene').criteria(organism='Homo Sapiens').string
```

will print out the string `model::Gene,rma::criteria,organism[name$il'Homo Sapiens']`
    
