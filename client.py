import json
import sys

file = sys.argv[1]
# Read the JSON file
with open(file, "r") as json_file:
    data = json.load(json_file)

def reserve_circuit(dict ,circuit, current_time):
    dict[tuple(circuit)][2] = True
    dict[tuple(circuit)][3] = current_time
    return circuit


def should_release_circuit(dict , circuit, current_time, demand_end_time):
    return dict[circuit][2] and current_time >= demand_end_time


# Function to release a circuit and update the current time
def release_circuit(dict, circuit):
    dict[tuple(circuit)][2] = False
    dict[tuple(circuit)][3]= None
    dict[tuple(circuit)][4]= None
# Initialize a dictionary to store the capacity for each circuit
circuit_capacity = {}

# Process each possible circuit
for circuit in data["possible-circuits"]:
    total_capacity = 0.0

    # Process each link in the circuit
    for link in data["links"]:
        link_points = link["points"]

        # Check if the link's endpoints are in the current circuit
        if all(endpoint in circuit for endpoint in link_points):
            total_capacity += link["capacity"]

    # Store the capacity for the circuit
    circuit_capacity[tuple(circuit)] = [total_capacity , len(circuit) - 1,False,None,None]
    



def is_circuit_available(dict ,circuit, current_time, demand_end_time , required_cap):
    check1 = current_time + dict[circuit][1] <=  demand_end_time
    #print(check1)
    check2 = required_cap <= dict[circuit][0]
    return check1 and check2

print(circuit_capacity.items())
current_time = 1
event_number = 0 

for demand in data['simulation']['demands']:
        demand_start_time = demand['start-time']
        demand_end_time = demand['end-time']
        required_cap = demand['demand']

        # print(required_cap)
        print(demand)
       
        

        for  circuit , values in circuit_capacity.items():
            if not values[2] and is_circuit_available(circuit_capacity,circuit, current_time, demand_end_time ,required_cap ):
                print("available circuit found")
                print(f'curr time is {current_time}')
                reserve_circuit(circuit_capacity,circuit, current_time)
                first_endpoint, last_endpoint = circuit[0], circuit[-1]
                print(f"{event_number + 1}st claim booking:  {first_endpoint} <-> {last_endpoint} st:{current_time + demand_end_time} - successful")
                break
            else:
               first_endpoint, last_endpoint = circuit[0], circuit[-1]
               print(f"{event_number + 1}st demand reservation:  {first_endpoint} <-> {last_endpoint} st:{current_time + demand_end_time} - unsuccessful")

        for  circuit , values in circuit_capacity.items():
            if should_release_circuit(circuit_capacity , circuit, current_time, demand_end_time):
                print(f'curr time is {current_time}')
                release_circuit(circuit_capacity , circuit)
                first_endpoint, last_endpoint = circuit[0], circuit[-1]
                print(f"{event_number + 1}st claim release: {first_endpoint} <-> {last_endpoint} st:{current_time + demand_end_time}")
                event_number = event_number+1

        current_time += demand_end_time
        event_number = event_number+1

