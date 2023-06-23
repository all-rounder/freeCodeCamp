def arithmetic_arranger(problems, answers=False):

    arranged_problems = ""
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    result = 0

    if len(problems) > 5:
        return "Error: Too many problems."

    for i in problems:
        # txt = re.split("\s", i)
        txt = i.split(" ")
        operand1, operator, operand2 = txt
        # if re.search("\D", operand1) or re.search("\D", operand2):
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator == "+":
            result = int(operand1) + int(operand2)
        elif operator == "-":
            result = int(operand1) - int(operand2)
        else:
            return "Error: Operator must be '+' or '-'."

        len1 = len(operand1)
        len2 = len(operand2)
        result = str(result)
        len4 = len(result)

        # if len1 > len2:
        #     length = len1 + 2
        #     line1 += " " * 2 + operand1 + " " * 4
        #     line2 += operator + " " * (length - len2 - 1) + operand2 + " " * 4
        #     line3 += "-" * length + " " * 4
        # else:
        #     length = len2 + 2
        #     line1 += " " * (length - len1) + operand1 + " " * 4
        #     line2 += operator + " " + operand2 + " " * 4
        #     line3 += "-" * length + " " * 4

        if len1 > len2:
            length = len1 + 2
        else:
            length = len2 + 2

        line1 += " " * (length - len1) + operand1 + " " * 4
        line2 += operator + " " * (length - len2 - 1) + operand2 + " " * 4
        line3 += "-" * length + " " * 4
        line4 += " " * (length - len4) + result + " " * 4

    arranged_problems = line1.rstrip() + "\n" + line2.rstrip() + "\n" + line3.rstrip()
    if answers:
        arranged_problems += "\n" + line4.rstrip()

    return arranged_problems


