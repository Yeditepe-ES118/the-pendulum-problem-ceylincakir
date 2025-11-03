import math

def find_period(L0, L1):
    "This function calculates and displays pendulum periods between L0 AND L1 (in meters) incremented by 1. Returns (T0 and T1) for L0 and L1 respectively."
    g = 9.81  # gravitational acceleration (m/s^2)
    # Loop through L values
    for L in range(L0,L1+ 1):
        T = 2*math.pi*math.sqrt(L/g)
        print(f"When L = {L:.1f} m, T = {T:.1f} s")
        
        # Return T0 and T1
        T0 = 2 * math.pi * math.sqrt(L0 / g)
        T1 = 2 * math.pi * math.sqrt(L1 / g)
        return T0, T1
    
#Example test (only runs if file is excuted directly)
if __name__ == "__main__":
    T0,T1 = find_period (2,10)
        
    

