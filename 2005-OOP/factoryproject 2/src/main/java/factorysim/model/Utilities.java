package factorysim.model;

import java.util.ArrayList;
import java.util.List;

/**
 * Class for utility functions used for all entities -> Holds I/O
 * Also contains utilities like state checks of entities
 * Never becomes object so no construtor for it.
 * Extended by classes for funtion usage.
 */
public class Utilities {
    
    List<Storage> InputStorage = new ArrayList<>();     // Inputs belt/machine has access to
    List<Storage> OutputStorage = new ArrayList<>();    // Outputs belt/machine has access to

    /**
     * Adds a storage to the input storage list
     * @param s A storage object 
     */
    public void addInputSource(Storage s){
        InputStorage.add(s);
    }
    /**
     * Adds a storage to output storage list
     * @param s A storage object
     */
    public void addOutputSource(Storage s){
        OutputStorage.add(s);
    }

    /**
     * Checks ALL inputs to make sure theyre all full
     * @return true if all inputs are full
     */
    public boolean allInputsFull(){
       for(int i = 0; i<InputStorage.size(); i++){
            if(!InputStorage.get(i).isFull()){      // If any input not full, return false
                return false;
            }
        }
        return true;
    }

    /**
     * Checks ALL outputs are empty
     * @return true is all outputs are empty
     */
    public boolean allOuputsEmpty(){
        for(int i = 0; i<OutputStorage.size(); i++){
            if(!OutputStorage.get(i).isEmpty()){    // If any output is not empty return false
                return false;
            }
        }
        return true;
    }

    
    /**
     * Checks all inputs for atleaset 1 input storage contains items
     * @return true is ANY input has items
     */
    public boolean inputHasItems(){

        boolean outcome = false;

        for(int i = 0; i<InputStorage.size(); i++){
            if(InputStorage.get(i).amount > 0){ 
                outcome = true;
            }
        }
        return outcome;
    }

    /**
     * Checks all outputs for atlease 1 output with space
     * @return true is ANY output still has space.
     */
    public boolean outputHasSpace(){
        boolean outcome = false;
        for(int i = 0; i<OutputStorage.size(); i++){
            if(OutputStorage.get(i).amount < OutputStorage.get(i).getCapacity()){
                outcome = true;
            }
        }
        return outcome;
    }


}
