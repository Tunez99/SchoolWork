package factorysim.model;

import java.util.List;
import java.util.Map;

/**
 * Class to debug through printing entity States
 * USAGE:
 * Confirmation of correct conenctions
 * Confirmation of correct state over time
 */
public class Print {
    
    /**
     * Prints the current state of storages 
     * @param title defines storage type -> INPUT, OUTPUT
     * @param map -> A list of storages in system
     * 
     * OUTPUTS:
     * Type of storage
     */
    public void printStorageMap(String title, List<Storage> map) {

        System.out.println("\n--- " + title + " ---");

        for (Storage s : map) {

            System.out.println(
                " | item=" + s.itemType()
                + " | amount=" + s.getAmount()
                + " | cap=" + s.getCapacity());
        }
    }

    /**
     * Prints the current state of all belts
     * @param belts A hashmap of all belts
     * 
     * OUTPUTS
     * Belts Name 
     * Item the belt supports
     * The total number of items it's moved
     * Inputs the belt is connected to
     * Outputs the belt is connected to
     */
    public void printBelt(Map<String, Belt> belts) {

        System.out.println("\n================ BELTS ================\n");

        for (Map.Entry<String, Belt> entry : belts.entrySet()) {

            String key = entry.getKey();
            Belt b = entry.getValue();

            System.out.println("\n--- BELT ---");
            System.out.println("Key: " + key);

            if (b == null) {
                System.out.println("NULL BELT");
                continue;
            }
            
            System.out.println("ItemType: " + b.getItemType());
            System.out.println("Total Items: " + b.getTotalItems());
            System.out.println("Inputs:");

            for (Storage s : b.InputStorage) {
                System.out.println(" - " + s.itemType());
            }

            System.out.println("Outputs:");
            for (Storage s : b.OutputStorage) {
                System.out.println(" - " + s.itemType());
            }
        }
    }

    /**
     * Prints the current state of all belts
     * @param machines A hashmap of all machines
     * 
     * OUTPUTS
     * Machines name 
     * The cooldown, and current cooldown state
     * Items its processed
     * Utilisation time
     * Input storages it's connected to
     * Output storages it's connected to
     */
    public void printMachines(Map<String, Machine> machines) {

        System.out.println("\n================ MACHINES ================\n");

        for (Map.Entry<String, Machine> entry : machines.entrySet()) {

            Machine m = entry.getValue();

            System.out.println("\n--- MACHINE ---");
            System.out.println("Key: " + entry.getKey());
            System.out.println("Name: " + m.getMachineName());
            System.out.println("Cooldown: " + m.getCooldown());
            System.out.println("Remaining cooldown: " + m.cooldownTimer);
            System.out.println("Items processed: " + m.itemsProcesses);
            System.out.println("Utilisation time: " + m.utilisationTime);

            System.out.println("Inputs:");
            for (Storage s : m.InputStorage) {
                System.out.println(" - " + s.itemType());
            }

            System.out.println("Outputs:");
            for (Storage s : m.OutputStorage) {
                System.out.println(" - " + s.itemType());
            }
        }
    }

    /**
     * Prints the current state of the sink entity
     * @param sink The sink object
     * 
     * OUTPUTS
     * The total tocks passed -> Time reference
     * The outputs connected to it and the item type
     * NOTE: outputs are recieved by reference so not human readable. 
     * 
     * A list of items the belt has consumed 
     */
    public void printSink(Sink sink) {

        System.out.println("\n================ SINK ================\n");

        if (sink == null) {
            System.out.println("NULL SINK");
            return;
        }

        System.out.println("Total tocks: " + sink.getTotalTocks());

        System.out.println("\n--- SOURCES ---");
        for (OutputSource s : sink.getSources()) {
            System.out.println(
                "Source -> " + s +
                " | item=" + s.itemType()
            );
        }

        System.out.println("\n--- CONSUMED ITEMS ---");
        for (Map.Entry<String, Integer> e : sink.getConsumedItems().entrySet()) {
            System.out.println(e.getKey() + " -> " + e.getValue());
        }
        System.out.println("=======================================");
    }

}