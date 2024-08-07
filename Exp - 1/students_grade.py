def main():
    marks  = int(input("Enter the marks of the student : "))
    grade = calc_grade(marks)
    if(grade != "inavlid"):
        print(f"The grade of the student is {grade}")
    else:
        print("Invalid marks entered")
    
def calc_grade(marks):
    if marks >= 95:
        return "A++"
    elif marks >= 90:
        return "A+"
    elif marks >= 85:
        return "A"
    elif marks >= 80:
        return "B++"
    elif marks >= 75:
        return "B+"
    elif marks >= 70:
        return "B"
    elif marks >= 65:
        return "C++"
    elif marks >= 60:
        return "C+"
    elif marks >= 0:
        return 'F'   
    else:
        return "inavlid"
if __name__ == "__main__":
    main()    