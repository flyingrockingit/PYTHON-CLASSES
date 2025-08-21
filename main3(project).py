total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes you attended: "))

attendance = (attended_classes / total_classes) * 100

print(f"\nYour attendance is: {attendance:.2f}%")

if attendance >= 75:
    print("✅ You are eligible to sit for the exam.")
else:
    print("❌ You are NOT eligible to sit for the exam.")