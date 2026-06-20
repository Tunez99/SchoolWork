#!/bin/bash


# Define the interface we wish to clean
# In this case it's the wifi one
INTERFACE="en0"


# Define a simple array for networks we want to keep.
KEEP_NETWORKS=(
    "ENTER NETWORK YOU WANT TO KEEP"
    "THIS IS ANOTHER NETWORK TO KEEP"
)

# We need to find all networks so run this command and store the out put in a list
ALL_NETWORKS=$(networksetup -listpreferredwirelessnetworks $INTERFACE | tail -n +2)


# Informational outputs.
echo "Preferred networks before cleanup:"
echo "$ALL_NETWORKS"
echo ""


# Loop through all the prefered networks
echo "$ALL_NETWORKS" | while IFS= read -r NET; do
    
    # Trim the network name so bash can accept it.
    NET="${NET#"${NET%%[![:space:]]*}"}"
    
    # Init a boolean outcome
    KEEP=false

    # Loop through the white list provided.
    for K in "${KEEP_NETWORKS[@]}"; do
    # Only if the network is approved, change the boolean to keep.

        if [ "$NET" == "$K" ]; then
            KEEP=true
            break
        fi
    done
    # if at this point the network is False, run the command to remover it
    if [ "$KEEP" == false ]; then
        echo "Removing $NET ..."
        networksetup -removepreferredwirelessnetwork "$INTERFACE" "$NET"
    fi
done

# Finally output for the networks left.
echo ""
echo "Cleanup complete. Remaining networks:"
networksetup -listpreferredwirelessnetworks $INTERFACE | tail -n +2