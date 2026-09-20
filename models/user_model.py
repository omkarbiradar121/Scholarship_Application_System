from models import fetch_records, insert_record


def get_user_by_email(email):
    query = """
        SELECT id, name, email, password, role, student_id
        FROM users
        WHERE email = :email
    """

    rows = fetch_records(
        query,
        {"email": email}
    )

    if rows:
        return rows[0]

    return None


def create_student(name, email, password, student_id):
    query = """
        INSERT INTO users
        (name, email, password, role, student_id)
        VALUES
        (:name, :email, :password, 'Student', :student_id)
    """

    return insert_record(
        query,
        {
            "name": name,
            "email": email,
            "password": password,
            "student_id": student_id
        }
    )