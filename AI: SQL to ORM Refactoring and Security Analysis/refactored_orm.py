from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Setup declarative base and model definition
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), nullable=False)

    def __repr__(self):
        return (
            f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"
        )


def get_session():
    """Establish and return an ORM Session."""
    # Using SQLite for a runnable standalone example; replace with MySQL URL for prod
    # "mysql+mysqlconnector://root:yourpassword@localhost/example_db"
    engine = create_engine("sqlite:///example.db", echo=False)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


# 3. Refactored CRUD Functions using SQLAlchemy ORM Sessions
def create_user(session, username, email):
    """Create a new user safely using SQLAlchemy ORM."""
    if not username or not email:
        print("Username and email are required.")
        return
    try:
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        print(f"User '{username}' created successfully.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating user: {e}")


def get_user_by_username(session, username):
    """Fetch a single user by username."""
    try:
        return (
            session.query(User).filter(User.username == username).first()
        )
    except SQLAlchemyError as e:
        print(f"Error fetching user: {e}")
        return None


def update_user_email(session, username, new_email):
    """Update a user's email."""
    try:
        user = (
            session.query(User).filter(User.username == username).first()
        )
        if user:
            user.email = new_email
            session.commit()
            print(f"Email updated for '{username}'.")
        else:
            print(f"User '{username}' not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error updating email: {e}")


def delete_user(session, username):
    """Delete a user by username."""
    try:
        user = (
            session.query(User).filter(User.username == username).first()
        )
        if user:
            session.delete(user)
            session.commit()
            print(f"User '{username}' deleted.")
        else:
            print(f"User '{username}' not found.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error deleting user: {e}")


def list_users(session):
    """Return all users."""
    try:
        return session.query(User).all()
    except SQLAlchemyError as e:
        print(f"Error listing users: {e}")
        return []


# 2. Demonstration of Table Creation, Insertion, and Querying via Session
if __name__ == "__main__":
    session = get_session()

    # Create user
    create_user(session, "alice", "alice@example.com")

    # Query for user
    alice = get_user_by_username(session, "alice")
    print("Fetched User:", alice)

    # List all users
    print("All Users:", list_users(session))

    session.close()
