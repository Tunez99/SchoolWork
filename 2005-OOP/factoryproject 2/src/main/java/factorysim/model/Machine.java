package factorysim.model;

/**
 * Controller for Machine transfer operations
 * 
 * Represents a machine that can transform items from 
 * an input source to an output source.
 * 
 * <p> Machine can only maintain 1 item conversion at a time. 
 * Tracks when the machine is not blocked -> cooldown or active.<p>
 */
public class Machine extends Utilities implements Tickable, StatResettable {
  
    private final String name;                // Name of the machine
    
    private final int cooldown;               // Cooldown of machine
    int cooldownTimer = 0;      // Tracks state -> If active > 0 it's actively in cooldown
    int itemsProcesses = 0;     // Number of processed items
    int utilisationTime = 0;    // Anytime the process is in cooldown or working. Not Blocked.

    /**
     * Constructor for a machine
     * Creates machine with given name and a cooldown
     * @param name The name of the machine
     * @param cooldown The cooldown time of the machine
     */
    public Machine(String name, int cooldown){
        this.name = name;                       // Give name to machine
        this.cooldown = cooldown;               // Give cooldown to machine
    }

    // GET FUNCTIONS ======================================
    /**
     * Returns the name of the machine 
     * @return name of the machine
     */
    public String getMachineName(){
        return name;
    }
    /**
     * Returns the cooldown of the machine
     * @return cooldown 
     */
    public int getCooldown(){
        return cooldown;
    }
    /**
     * Returns the total utilisation time
     * @return utilisation of machine
     */
    public int getUtilisationTime(){
        return utilisationTime;
    }
    // GET FUNCTIONS END ===================================
    
    /**
     * Controller logic for machine transfers.
     * Operates on tick cycle
     * 
     * Machine Specs:
     * Transfer if 
     *          - ALL inputs available -> fullness
     *          - ALL outputs are available -> Emptiness
     * ALL inputs get consumed and transformed into output capacity
     */
    @Override
    public void tick() {

        if(cooldownTimer > 0){                              // Check if machine is in cooldown
            cooldownTimer--;                                // Reduce cooldown timer by 1 time
            utilisationTime++;                              // Increase utilisation by 1 time
            return;                                         // Skip any transfer

        } else if(allInputsFull() && allOuputsEmpty()){     // If all inputs and outputs in correct state
            while(allInputsFull() && allOuputsEmpty()){     // While inputs and outputs continue correct state
                
                for(Storage in : InputStorage){             // For all inputs set empty
                    in.setToEmpty();
                }
                
                for(Storage out : OutputStorage){           // For all outputs fill to max
                    out.setToFull();
                }
            }
        cooldownTimer = cooldown;                           // Put machine into cooldown 
        utilisationTime++;                                  // Increase utilisation by 1 time
        } 
    }

    /**
     * Reset tracked statistic for machine
     * Items processed and utilisation time
     */
    @Override
    public void resetStatistics() {         
        itemsProcesses = 0;     
        utilisationTime = 0; 
    }
}


