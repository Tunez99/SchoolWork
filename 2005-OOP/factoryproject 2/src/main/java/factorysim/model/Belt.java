package factorysim.model;


/**
 * Controller for belt transfer operations
 * 
 * Represents a converyor belt that can transfer items from 
 * an input source to an output source.
 * 
 * <p> Belt can only maintain 1 item type at a time. Will reject items
 * of a different type. 
 * Tracks number of items it transfers.<p>
 */
public class Belt extends Utilities implements Tockable, StatResettable {
    
    private int totalItems = 0;         // Counter for tracking stats

    private int inputPointer = 0;       // Counter to track inputs
    private int outputPointer = 0;      // Counter to track outputs

    private final String beltName;            // Stores belt name
    private final String itemType;            // Stores the item it moves - used for validation
    
    /**
     * Constructurs a new belt with given name and item.
     * @param beltName Name of the belt
     * @param itemType the type of item the belt is permitted to transfer
     */
    public Belt(String beltName, String itemType){
        this.beltName = beltName;       // Initiate name
        this.itemType = itemType;       // Initiate belt type
    }

    // GET FUNCTIONS ======================================
    /**
     * Returns the item this belt transfers
     * @return belts item type
     */
    public String getItemType(){
        return itemType;
    }
    /**
     * Returns the belts name
     * @return belts name
     */
    public String getBeltName(){
        return beltName;
    }
    /**
     * Returns the tracked items
     * @return total items transfered 
     */
    public int getTotalItems(){
        return totalItems;
    }
    // GET FUNCTIONS END ===================================
    
    /**
     * Checks if a given item matches the belts specific item type
     * @param newItem The item you want to check matches belt
     * @throws BeltValidationException
     */
    public void validateItem(String newItem) throws BeltValidationException{
        if (!this.itemType.equals(newItem)){                        // Port requests item checked against belts item type
            throw new BeltValidationException("Message");
        }
    }

    /**
     * Controller for belt transfer logic
     * Operates on tock phase cycle
     */
    @Override
    public void tock() {

        while(inputHasItems() && outputHasSpace()){                 // Validate movement can happen

            Storage in = InputStorage.get(inputPointer);            // Get input we looking at
            Storage out = OutputStorage.get(outputPointer);         // Get output we looking at
        
            if(in.amount <= 0){                                             // If input is empty, 
                inputPointer = (inputPointer + 1) % InputStorage.size();    // skip iteration and move to next input
                continue;
            }

            if(out.amount >= out.getCapacity()){                                 // If output is full,
                outputPointer = (outputPointer + 1) % OutputStorage.size(); // Skip iteration and move to next output
                continue;
            }

            if(in.amount > 0 && out.amount <= out.getCapacity()){        // If valid transfer
                in.decreaseAmount(1);                            // Move 1 item out of input
                out.increaseAmount(1);                           // Move 1 item into output
                

                inputPointer = (inputPointer + 1) % InputStorage.size();    // Progres pointer
                outputPointer = (outputPointer + 1) % OutputStorage.size(); // Progress pointer
                
                totalItems++;                                       // Add 1 to moved items
            }
        }
    }
    /**
     * Reset tracked statistics for belt objects
     * - total items over a period.
     */
    @Override
    public void resetStatistics() {
        totalItems = 0;     // Only statistic for belts total items processed, reset
    }
}
