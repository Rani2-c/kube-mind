import os
import time

print("="*60)
print(" KUBEMIND: MEMORY-AUGMENTED INCIDENT RESPONSE AGENT ")
print("="*60)

def handle_incident(error_log):
    print(f"\n[Analyzing System Error Log]: '{error_log}'")
    print("Checking Hindsight long-term memory banks for past occurrences...")
    time.sleep(1)
    
    # Simulating the Hindsight recall logic gate structure cleanly
    memory_file = "hindsight_bank.txt"
    has_memory = False
    past_fix = ""
    
    if os.path.exists(memory_file):
        with open(memory_file, "r") as f:
            for line in f:
                if error_log in line:
                    has_memory = True
                    past_fix = line.split("|")[1].strip()
                    break
    
    if has_memory:
        print("\n🎉 [MEMORY HIT] Found a matching past incident in Hindsight memory banks!")
        print(f"-> RESOLUTION FROM PAST INTERACTIONS: {past_fix}")
    else:
        print("\n❌ [MEMORY MISS] No historical resolution found in memory system.")
        print("-> FALLBACK SYSTEM: Querying base system database...")
        time.sleep(0.5)
        print("-> SUGGESTED SYSTEM FIX: Try restarting the server node container instance.")
        
        # Take manual team validation input from the engineer
        user_input = input("\nEngineers! Type the manual emergency fix applied to save it to memory: ")
        if user_input:
            # Simulating the Hindsight retain behavior to save the context state
            with open(memory_file, "a") as f:
                f.write(f"{error_log} | {user_input}\n")
            print("✓ [MEMORY RETAINED] Resolution successfully saved to Hindsight Memory layer!")

# --- MULTI-INTERACTION TEST SCENARIO FOR EVALUATION ---
sample_error = "CRITICAL: Database connection timed out on port 5432"

# Clean up any past runs to show a fresh demo execution flow
if os.path.exists("hindsight_bank.txt"):
    os.remove("hindsight_bank.txt")

print("\n--- RUNNING INTERACTION #1 (First time seeing the error) ---")
handle_incident(sample_error)

print("\n" + "-"*55)
print("--- RUNNING INTERACTION #2 (Running the same error to prove memory) ---")
print("-"*55)
handle_incident(sample_error)
