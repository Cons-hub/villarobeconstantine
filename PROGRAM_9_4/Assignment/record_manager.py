class RecordManager:
    def __init__(self):
        self.records = []

    def add_record(self, person):
        for record in self.records:
            if record.person_id == person.person_id:
                raise ValueError("ID already exists.")

        self.records.append(person)

    def view_records(self):
        if not self.records:
            print("\nNo records available.")
            return

        print("\n========== ALL RECORDS ==========")

        for record in self.records:
            print("\n-------------------------------")
            record.display_info()

        print("-------------------------------")

    def search_record(self, person_id):
        for record in self.records:
            if record.person_id == person_id:
                return record

        return None

    def update_record(
        self,
        person_id,
        name,
        age,
        address,
        contact_number,
        email
    ):
        record = self.search_record(person_id)

        if record is None:
            return False

        record.name = name
        record.age = age
        record.address = address
        record.contact_number = contact_number
        record.email = email

        return True

    def delete_record(self, person_id):
        record = self.search_record(person_id)

        if record is None:
            return False

        self.records.remove(record)
        return True