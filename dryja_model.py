# Danielle Dryja
# Dryja Adaptive Model

print("Welcome to the Dryja Adaptive Model")

phases = []

num_phases = int(input("How many phases would you like to enter? "))

for i in range(num_phases):
    print(f"\nPhase {i + 1}")

    phase_name = input("Enter phase name: ")
    description = input("Enter short description: ")

    phases.append((phase_name, description))

print("\n--- Dryja Adaptive Model Summary ---")

for i, phase in enumerate(phases, start=1):
    print(f"\nPhase {i}: {phase[0]}")
    print(f"Description: {phase[1]}")

print("\nModel completed successfully.")