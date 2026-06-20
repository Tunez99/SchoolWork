package factorysim.model;

/**
 * Class to represent a storage entity
 * Storage "slot" can maintain 1 item 
 * Has a capacity and tracks current amount in the storage
 * 
 * Implements Output Source for sink to use 
 * This is generalised for both inputs and outputs, can be used for overall storage too
 */
public class Storage implements OutputSource{

    private final String item;        // Item name
    public int amount;         // Current amount
    private final int capacity;       // Capacity of storage

    /**
     * Initiate a storage entity
     * @param capacity Max amount of numbers it can hold
     * @param item The type of item it can hold
     */
    public Storage(int capacity, String item){
        this.capacity = capacity;       // Set capacity
        this.item = item;               // Set item type
    }
    

    // GET FUNCTIONS ======================================

    /**
     * Returns item type
     * @return item type
     */
    @Override
    public String itemType(){ 
        return item; }
    
    /**
     * Returns current amount in storage
     * @return amount in storage
     */
    public int getAmount(){ 
        return amount; 
    }

    /**
     * Returns the capcaity of storage
     * @return the size of the storage
     */
    public int getCapacity(){ 
        return capacity; 
    }

    // GET FUNCTIONS END ===================================
    
    /**
     * Checks if the storage is empty
     * @return Boolean representing empty state
     */
    public boolean isEmpty(){ 
        return amount == 0;
    }

    /**
     * Checks if the storage is full
     * @return Boolean representing full state
     */
    public boolean isFull(){
        return amount == capacity;
    }

    /**
     * Sets the amount to 0
     */
    public void setToEmpty(){
        amount = 0;
    }
    
    /**
     * Sets the amount to the capacity
     */
    public void setToFull(){
        amount = capacity;
    }
    
    /**
     * Checks if the amount is more that 0
     */
    @Override
    public boolean canPull(){ 
        return amount > 0; 
    }

    /** 
     * Pulls 1 item from the storage
     */
    @Override
    public void pullItem(){ 
        decreaseAmount(1);; 
    }

    /**
     * Increases the amount -> DOES NOT HANDLE DOMAIN
     * @param x Amount the storage will increase by
     */
    public void increaseAmount(int x){
            amount += x;
    }

    /**
     * Decreases the amount in the storage -> DOES NOT HANDLE DOMAIN
     * @param x Amount the storage will decrease by
     */
    public void decreaseAmount(int x){
            amount -= x;
    }

}
