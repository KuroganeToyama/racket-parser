# Check if func is defined on exactly 2 lines
def two_lines_rule(file, func):
    target = f"(define ({func}"

    func_start = 0
    func_end = 0
    line_count = 0

    with open(file, "r") as f:
        for line in f:
            line_count += 1

            if line.startswith(target):
                func_start = line_count 
                open_brackets = line.count('(')
                close_brackets = line.count(')')

                try:
                    while open_brackets != close_brackets:
                        line = next(f)
                        line_count += 1
                        open_brackets += line.count('(')
                        close_brackets += line.count(')')

                        if open_brackets == close_brackets:
                            func_end = line_count
                except StopIteration:
                    pass      

                if (func_end - func_start + 1) == 2:
                    return "Function is exactly 2 lines long"
                else:
                    return "Function is not 2 lines long"
                
            else:
                continue

    return "Whoops, target function not found"

# Check if func uses exactly 1 foldr
def foldr_count(file, func):
    target = f"(define ({func}"

    with open(file, "r") as f:
        for line in f:
            if line.startswith(target):
                foldr_counter = line.count("foldr")
                open_brackets = line.count('(')
                close_brackets = line.count(')')

                try:
                    while open_brackets != close_brackets:
                        line = next(f)
                        foldr_counter += line.count("foldr")
                        open_brackets += line.count('(')
                        close_brackets += line.count(')')

                        if open_brackets == close_brackets:
                            return foldr_counter
                except StopIteration:
                    pass      
            else:
                continue

    return "Whoops, function not found"

# Check if func uses banned ALFs (abstract list functions)
def banned_alfs(file, func):
    banned = ["map", "foldl", "filter", "build-list"]
    target = f"(define ({func}"

    with open(file, "r") as f:
        for line in f:
            if line.startswith(target):
                for func in banned:
                    if func in line:
                        return f"Use banned function {func}"
                open_brackets = line.count('(')
                close_brackets = line.count(')')

                try:
                    while open_brackets != close_brackets:
                        line = next(f)
                        for func in banned:
                            if func in line:
                                return f"Use banned function {func}"
                        open_brackets += line.count('(')
                        close_brackets += line.count(')')

                        if open_brackets == close_brackets:
                            return "Good job!"
                except StopIteration:
                    pass      
            else:
                continue

    return "Whoops, function not found"

# Check if func uses lambda as helpers (a possible sign of using the Y-Combinator)
def lambda_check(file, func):
    lambda_pattern = "((lambda"
    target = f"(define ({func}"

    with open(file, "r") as f:
        for line in f:
            if line.startswith(target):
                if lambda_pattern in line:
                    return "Possbily using Y-Combinator"
                open_brackets = line.count('(')
                close_brackets = line.count(')')

                try:
                    while open_brackets != close_brackets:
                        line = next(f)
                        if lambda_pattern in line:
                            return "Possibly using Y-Combinator"
                        open_brackets += line.count('(')
                        close_brackets += line.count(')')

                        if open_brackets == close_brackets:
                            return "Good job"
                except StopIteration:
                    pass      
            else:
                continue

    return "Whoops, function not found"