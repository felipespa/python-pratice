class Student:
    school = "Online School"

    def __init__(self, first_name: str, last_name: str, major: str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.major = major

    def full_name_with_major(self):
        return f"{self.first_name} {self.last_name}, your major is {self.major}"

    def full_name_major_school(self):
        return f"{self.first_name} {self.last_name}, your major is {self.major} on a {self.school}"

    @classmethod
    def set_online_school(cls, new_school: str) -> None:
        cls.school = new_school


class CollegeStudent(Student):
    def __init__(
        self, first_name: str, last_name: str, major: str, has_monograph: bool
    ) -> None:
        super().__init__(first_name, last_name, major)
        self.has_monograph = has_monograph
