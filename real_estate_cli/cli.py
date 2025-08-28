
# cli.py
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Property, Client, Transaction
from sqlalchemy.exc import IntegrityError

# Setup DB connection
engine = create_engine("sqlite:///real_estate.db")
Session = sessionmaker(bind=engine)
session = Session()


def list_properties():
    properties = session.query(Property).all()
    if not properties:
        print("No properties found.")
    else:
        for p in properties:
            print(f"[{p.id}] {p.address} | {p.property_type} | ${p.price} | {p.status}")


def add_property():
    address = input("Enter property address: ")
    p_type = input("Enter property type (House/Apartment/etc.): ")
    price = float(input("Enter property price: "))
    status = input("Enter status (Available/Sold/Rented): ")

    new_property = Property(address=address, property_type=p_type, price=price, status=status)
    session.add(new_property)
    session.commit()
    print("✅ Property added successfully!")


def list_clients():
    clients = session.query(Client).all()
    if not clients:
        print("No clients found.")
    else:
        for c in clients:
            print(f"[{c.id}] {c.name} | {c.email} | {c.phone} | {c.role}")


def add_client():
    session = Session()
    name = input("Enter client name: ")
    email = input("Enter client email: ")
    phone = input("Enter client phone: ")
    role = input("Enter role (Buyer/Seller): ")

    new_client = Client(name=name, email=email, phone=phone, role=role)
    session.add(new_client)
    try:
        session.commit()
        print("✅ Client added successfully!")
    except IntegrityError:
        session.rollback()
        print("⚠️ A client with this email or phone already exists. Please use different details.")
    finally:
        session.close()


def record_transaction():
    property_id = int(input("Enter property ID: "))
    client_id = int(input("Enter client ID: "))
    t_type = input("Enter transaction type (Purchase/Rent): ")
    amount = float(input("Enter transaction amount: "))

    new_txn = Transaction(property_id=property_id, client_id=client_id, transaction_type=t_type, amount=amount)
    session.add(new_txn)

    # Update property status if sold or rented
    property_obj = session.query(Property).get(property_id)
    if property_obj and t_type.lower() == "purchase":
        property_obj.status = "Sold"
    elif property_obj and t_type.lower() == "rent":
        property_obj.status = "Rented"

    session.commit()
    print("✅ Transaction recorded successfully!")


def main():
    while True:
        print("\n🏠 Real Estate CLI Menu")
        print("1. List all properties")
        print("2. Add new property")
        print("3. List all clients")
        print("4. Add new client")
        print("5. Record transaction")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            list_properties()
        elif choice == "2":
            add_property()
        elif choice == "3":
            list_clients()
        elif choice == "4":
            add_client()
        elif choice == "5":
            record_transaction()
        elif choice == "0":
            print("Goodbye 👋")
            session.close()
            sys.exit()
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
