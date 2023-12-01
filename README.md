# Basic Racket Parser
Once again, a small project during my tenure as an Instructional Support Assistant (ISA).
<br><br>
The marking engine isn't exactly perfect and some assignment questions would have restrictions that just so happened to break the marking engine (i.e. the engine cannot check for those restrictions).
<br><br>
Luckily, my senpai (Japanese for senior, I prefer senpai over senior), Mark Gasior, has shown me how easy it is to parse Racket code.
<br><br>
It has to do with the fact that every single statement in Racket must be wrapped in a pair of brackets. For example, 
`(define (my-func x) (+ x 1))`.
<br><br>
As such, the algorithm to parse the code becomes a matter of counting the number of open and close brackets.
<br><br>
My senpai Mark initially wrote a C++ script for a one-off situation on an assignment (he's a big fan with C++ and quite the opposite with Python).
<br><br>
Unfortunately, the same situation repeated a whole lot, and I don't like re-compiling the C++ script every single time, so I did the same thing in Python, as well as generalized the script to work with arbitrary files, functions, and restrictions.
<br><br>
That said, many thanks to my senpai Mark Gasior!

# Usage
`python rkt_parser.py rkt_parser_args.txt`
<br><br>
`rkt_parser_args.txt` contains the arguments to be fed to `rkt_parser.py`. The arguments are the assignment directory name, the target submission file, the target function, and the name of the output CSV, respectively on each line.
<br><br>
Furthermore, you can define functions in `rkt_parser_restrictions.py` to implement custom restrictions. This would only require minor changes in `rkt_parser.py` to display what you want to see in the output CSV.

# Note
I'm aware that the functions share the same overall structure, so I'm working on how to abstract them even further. But like I mentioned in an earlier project, you gotta make it do the job before you start caring about other stuff. 