class c:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
        self.id = self.generate_id()
    def generate_id(self):
        # Generate an ID based on the worker's attributes
        id = self.surname + self.name[0] + str(self.seniority)
        if self.age < 18:
            return id.lower()
        else:
            return id.upper()
def main():
    worker1 = c("Anna","May",17,7)
    worker2 = c("George","Brown",21,4)
    print(f"Worker 1 ID: {worker1.id}")
    print(f"Worker 2 ID: {worker2.id}")
if __name__ == "__main__":
    main() 