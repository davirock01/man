"""
Fix user passwords in database
"""
from app.core.config import settings
from app.core.security import get_password_hash
from sqlalchemy import create_engine, text

# Password for all test users
PASSWORD = "testpass123"
hashed = get_password_hash(PASSWORD)

print(f"Hashed password: {hashed}")

# Connect to database
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)

with engine.connect() as conn:
    # Update all test users with the correct hashed password
    result = conn.execute(
        text("UPDATE usuarios SET hash_password = :hash WHERE email LIKE '%@test.com'"),
        {"hash": hashed}
    )
    conn.commit()
    
    print(f"Updated {result.rowcount} users")
    
    # Verify
    users = conn.execute(text("SELECT email, rol FROM usuarios WHERE email LIKE '%@test.com'"))
    print("\nUsers in database:")
    for row in users:
        print(f"  - {row[0]} ({row[1]})")

print("\nDone! All test users now have password: testpass123")

