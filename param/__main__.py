from .Arg import Arg
import sys

ex = Arg(
    params={
        "name" : {
            "flag" : "--name",
            "type" : str,
            "default" : "Human",
        },
    },
    command=sys.argv
)

@ex.run("greet") 
def greet() :
    print(f"Hello {ex.val('name')}")
