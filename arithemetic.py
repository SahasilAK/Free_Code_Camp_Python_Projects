def arithmetic_arranger(problems, dosum=None):

    arranged_problems = ""

    # Test that number of problems is within range
    if len(problems) > 5:
        arranged_problems="Error: Too many problems."
        return arranged_problems

    top = []  # Will store values for top row
    bottom = []  # Will store values for bottom row
    if dosum: allsums = []  # Will store sum values if desired
    for problem in problems:
        pieces = problem.split()

        # Error checking
        if not pieces[0].isnumeric() or not pieces[2].isnumeric():
            arranged_problems = "Error: Numbers must only contain digits."
            return arranged_problems
        if len(pieces[0]) > 4 or len(pieces[2]) > 4:
            arranged_problems = "Error: Numbers cannot be more than four digits."
            return arranged_problems
        if pieces[1] != "+" and pieces[1] != "-":
            arranged_problems = "Error: Operator must be '+' or '-'."
            return arranged_problems

        if dosum is True: # Get sums if these are desired
            calc = 0
            if pieces[1] == "+":
                calc = int(pieces[0]) + int(pieces[2])
            elif pieces[1] == "-":
                calc = int(pieces[0]) - int(pieces[2])
            else:
                arranged_problems="Error: Operator must be '+' or '-'."
                return arranged_problems
            pieces.append(str(calc))

        top.append(pieces[0])  # Top values
        bottom.append((pieces[1], pieces[2]))  # Bottom values
        if dosum: allsums.append(pieces[3])  # Sum values

    # Determine length of each sum
    alltop_lengths = []
    allbottom_lengths = []
    actual_lengths = []

    for top_length in top:
        alltop_lengths.append(len(top_length))

    for bottom_length in bottom:
        allbottom_lengths.append(len(bottom_length[1]))

    for count in range(0, len(alltop_lengths)):  # We could also use allbottom_lengths here
        if alltop_lengths[count] >= allbottom_lengths[count]:
            actual_lengths.append(alltop_lengths[count])
        else:
            actual_lengths.append(allbottom_lengths[count])

        actual_length_int = (int(actual_lengths[count])) + 2  # Add operator plus one space
        actual_lengths[count] = actual_length_int

    # Build string

    # Top row of operands
    count = 0
    for top_string in alltop_lengths:
        space_length = actual_lengths[count] - top_string
        spacing = ""
        for spacecount in range(1, space_length+1):  # I suspect there is a better way of doing this
            spacing = spacing + " "
        arranged_problems = arranged_problems + spacing
        arranged_problems = arranged_problems + top[count]
        arranged_problems = arranged_problems + "    "
        count = count + 1
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n"

    # Second row of operators and operands
    count = 0
    for bottom_string in allbottom_lengths:
        arranged_problems = arranged_problems + bottom[count][0] + " "
        space_length = (actual_lengths[count] - 2) - bottom_string
        if space_length > 0:
            spacing = ""
            for spacecount in range(1, space_length+1):
                spacing = spacing + " "
            arranged_problems = arranged_problems + spacing
        arranged_problems = arranged_problems + bottom[count][1]
        arranged_problems = arranged_problems + "    "
        count = count + 1
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n"

    # Dashes row
    for dashes_length in actual_lengths:
        for dashcount in range (1, dashes_length+1):
            arranged_problems = arranged_problems + "-"
        arranged_problems = arranged_problems + "    "
    arranged_problems = arranged_problems.rstrip()
    arranged_problems = arranged_problems + "\n"

    # Sums row
    if dosum:
        count = 0
        for thissum in allsums:
            space_length = actual_lengths[count] - len(thissum)
            for spacecount in range (1, space_length+1):
                arranged_problems = arranged_problems + " "
            arranged_problems = arranged_problems + thissum
            arranged_problems = arranged_problems + "    "
            count = count + 1
        arranged_problems = arranged_problems.rstrip()
        arranged_problems = arranged_problems + "\n"

    return arranged_problems
