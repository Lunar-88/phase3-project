
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True)
    address = Column(String, nullable=False)
    property_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default="Available")

    transactions = relationship("Transaction", back_populates="property")

    def __repr__(self):
        return f"<Property(id={self.id}, address='{self.address}', type={self.property_type}, price={self.price}, status={self.status})>"


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    role = Column(String, nullable=False)  # Buyer, Seller, Tenant, Landlord

    transactions = relationship("Transaction", back_populates="client")

    def __repr__(self):
        return f"<Client(id={self.id}, name='{self.name}', role={self.role})>"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey("properties.id"))
    client_id = Column(Integer, ForeignKey("clients.id"))
    transaction_type = Column(String, nullable=False)  # Sale or Rental
    date = Column(Date)
    amount = Column(Float)

    property = relationship("Property", back_populates="transactions")
    client = relationship("Client", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, type={self.transaction_type}, amount={self.amount})>"
