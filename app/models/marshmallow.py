from app import ma


class StudentSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email", "address", "phone")
