
contacts = {
    "Alice": "9876543210",
    "Bob": "9123456780",
    "Charlie": "9001122334"
}
contacts["Diana"] = "9988776655"
contacts["Bob"] = "9111111111"
existing_contact = contacts.get("Alice", "Contact not found")
missing_contact = contacts.get("Eve", "Contact not found")
print("Safe Lookup Results:")
print("Alice:", existing_contact)
print("Eve:", missing_contact)
print("\nContact List:")
for name, phone in contacts.items():
    print(f"Contact: {name} | Phone: {phone}")