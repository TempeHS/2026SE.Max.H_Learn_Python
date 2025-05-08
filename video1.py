class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house} "
    
    #getter
    def house(self):
        return self.house
    
    #setter
    def house(self, house):
        if house not in
        self.house = house


def main():
    student = get_student()
    student.house = "no way jose"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("house: ")
    return Student(name, house)


if __name__ == "__main__":
    main()