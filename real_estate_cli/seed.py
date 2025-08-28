
# seed.py
from datetime import date
from database import init_db, Session
from models import Property, Client, Transaction

def seed_data():
    session = Session()

    # --- Clear existing data ---
    session.query(Transaction).delete()
    session.query(Property).delete()
    session.query(Client).delete()

    # --- Add clients ---
    client1 = Client(name="Alice Johnson", email="alice@example.com", phone="1234567890", role="Buyer")
    client2 = Client(name="Bob Smith", email="bob@example.com", phone="0987654321", role="Seller")
    client3 = Client(name="Charlie Brown", email="charlie@example.com", phone="5551234567", role="Buyer")

    session.add_all([client1, client2, client3])

    # --- Add properties ---
    prop1 = Property(address="123 Main St", property_type="Apartment", price=120000, status="Available")
    prop2 = Property(address="45 Oak Ave", property_type="House", price=250000, status="Available")
    prop3 = Property(address="78 Pine Rd", property_type="Condo", price=180000, status="Available")

    session.add_all([prop1, prop2, prop3])
    session.commit()

    # --- Add transactions ---
    txn1 = Transaction(property_id=prop1.id, client_id=client1.id,
                       transaction_type="Purchase", date=date.today(), amount=120000)
    txn2 = Transaction(property_id=prop2.id, client_id=client2.id,
                       transaction_type="Listing", date=date.today(), amount=250000)

    session.add_all([txn1, txn2])

    # Update property status after transaction
    prop1.status = "Sold"
    prop2.status = "Available"  # still listed

    session.commit()
    session.close()
    print("✅ Database initialized and seeded with sample data!")

if __name__ == "__main__":
    init_db()
    seed_data()
