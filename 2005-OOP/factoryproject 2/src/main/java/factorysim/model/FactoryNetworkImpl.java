package factorysim.model;
import factorysim.config.MachineConfig;
import factorysim.config.PortConfig;

import factorysim.stats.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;


/**
 * FactoryNetwork models the overall factory, including connections 
 * between machines, belts, and sinks.
 * Implements the FactoryNetwork interface.
 */
public final class FactoryNetworkImpl implements FactoryNetwork {

    Sink sink;

    int totalTicks = 0;                                     // Tracks time interval
    int totalTocks = 0;                                     // Tracks time interval

    List<Storage> InputStorage  = new ArrayList<>();        // Create list for Input storages
    List<Storage> OutputStorage  = new ArrayList<>();       // Create list for Output storages
    HashMap<String, Belt> belts = new HashMap<>();          // Create hash map (Belt name, Belt object)
    HashMap<String, Machine> machines = new HashMap<>();    // Create hash map (Machine name, Machine object)

    /**
     * Establish a factory network.
     * Most of the logic for this class is in the constructor
     * (though you might find private methods useful to break it up)
     * 
     * @param machineConfigs a list of machine configs from the 
     * configuration file (in the same order they were originally in
     * i.e. machineConfigs.get(0) would have been the first listed machine in the config file)
     * @throws BeltValidationException If the list of machineConfigs tries to wire a sink to a
     * machine input port, or tries to connect a belt to two ports with different types, 
     * the constructor should throw a BeltValidationException with an informative error message.
     */
    public FactoryNetworkImpl(List<MachineConfig> machineConfigs) throws BeltValidationException{

        // The constructor should initialise your factory components (Sink has been initialised for you below). 
        // It should "wire" the components together (i.e. connect machine output ports to belts/sinks etc), 
        // based on the layout specified in the machine configs.
        // It should also check that the provided config doesn't suggest wiring a belt in 
        // an incorrect way (i.e. you can't  wire a sink to a machine input port)
        // a BeltValidationException. You might even find it useful to do this first,
        // It is up to you how to approach this/ what data structures you use.
        
        this.sink = new Sink();                                         // Create sink object

        for(MachineConfig config : machineConfigs){                     // Loop through configs provided from file

            String name = config.getName();                             // Get the machines name
            int cooldown = config.getCooldown();                        // Get the cooldown period

            List<PortConfig> InputPorts = config.getInputConfigs();     // List of port configs for inputs
            List<PortConfig> OutputPorts = config.getOutputConfigs();   // List of port configs for outputs
            
            Machine m = new Machine(name, cooldown);                    // Create a machine
            machines.put(name, m);                                      // Add to hash map for tracking

            for (PortConfig p : InputPorts){                            // Loop through input port configs
                Storage s = new Storage(p.getAmount(), p.getItemName());// Create a storage for that machines input, matching item type
                
                InputStorage.add(s);                                    // Add to an overall list
                
                String beltName = p.getBeltName();                      // From port config, get belt name
                String itemName = p.getItemName();                      // From port config, get item type

                if (beltName.equals(sink.getBeltName())) {              // Make sure sink belt doesn't attach to an input
                    throw new BeltValidationException("Sink cannot be an input");
                }

                m.addInputSource(s);                      // Add the Storage Object to current machine

                Belt b = belts.get(beltName);             // Attemt to get a belt from overall list

                if(b == null){                            // If no belt exists in belt list
                    b = new Belt(beltName, itemName);     // Create a new belt 
                    belts.put(beltName, b);               // Add to the belt list
                } else {
                    b.validateItem(itemName);             // If belt exists, check the item matches port config
                }
            b.addOutputSource(s);                         // Add belt to output of belt
            }
      
            // Outputs
            for (PortConfig p : OutputPorts){             // Same as input ports, loop through output ports

                Storage s = new Storage(p.getAmount(), p.getItemName());

                OutputStorage.add(s);
                
                String beltName = p.getBeltName();
                String itemName = p.getItemName();

                m.addOutputSource(s);                       // Add to output

                Belt b = belts.get(beltName);

                if(beltName.equals(sink.getBeltName())){    // If if a sink belt
                    sink.addSource(s);                      // Connect to sink
                    continue;                               // Skip current iteration -> Make no belt
                }
                
                if (b == null){
                    b = new Belt(beltName, itemName);
                    belts.put(beltName, b);
                } else {
                    b.validateItem(itemName);
                }
                if(b != null){
                    b.addInputSource(s);                    // Add output port to belt input
                }
            }
        }

        // ***** DEBUGGING STATEMENTS -> Check for correctness of initilisation
        //Print pr = new Print();
        //pr.printStorageMap("INPUTS", InputStorage);
        //pr.printStorageMap("OUTPUTS", OutputStorage);
        //pr.printBelt(belts);
        //pr.printMachines(machines);
        //pr.printSink(sink);
    }

    /**
     * Performs tick conditions for ALL machines
     * Tracks the total ticks used
     */
    @Override
    public void tick() {
        for(Machine m : machines.values()){
            m.tick();
        }
        totalTicks++;

        // ***** DEBUGGING STATEMENTS -> Logic control for machines
        //Print pr = new Print();
        //System.out.println("TOTAL TIME ====" + totalTicks);
        //pr.printMachines(machines);
        //pr.printStorageMap("INPUTS ======", InputStorage);
        //pr.printStorageMap("OUTPUTS ======", OutputStorage);
    }

    /**
     * Performs tock conditions for ALL belts and sink
     * Tracks the total tocks used
     */
    @Override
    public void tock() {
        for (Belt b : belts.values()){
            b.tock();
        }
        sink.tock();
        totalTocks++;

        // ***** DEBUGGING STATEMENTS -> Logic control for belt and sink
        //Print pr = new Print();
        //pr.printMachines(machines);
        //pr.printBelt(belts);
        //pr.printSink(sink);
        //pr.printStorageMap("INPUTS ======", InputStorage);
        //pr.printStorageMap("OUTPUTS ======", OutputStorage);

    }

    /**
     * Reset total ticks and tocks used
     * Resets sinks stats
     * Resets ALL machine stats
     * Resets ALL belt stats
     */
    @Override
    public void resetStatistics() {

        totalTicks = 0;
        totalTocks = 0;

        sink.resetStatistics();             // Reset Sink stats

        for(Machine m: machines.values()){  // For each machine reset stats
            m.resetStatistics();
        }

        for(Belt b: belts.values()){        // For each belt reset stats
            b.resetStatistics();
        }
    }

    /**
     * Creates a list of all items the sink has consumed
     * Calculates the average items per minute (APM)
     * @return <type> Sink entry -> item + APM
     */
    @Override
    public List<SinkEntry> getSinkStats() {
        List<SinkEntry> sStats = new ArrayList<>();                     // Create list of sinkEntries
        List<String> itemTypes = sink.getItemTypes();                   // Get a list of all items in sink

        for(int i = 0; i<itemTypes.size(); i++){                        // Iterate over items
            double APM = sink.getAvgItemsPerMinute(itemTypes.get(i));   // Calculate the Average Per Minute of each item
            sStats.add(new SinkEntry(itemTypes.get(i), APM));           // Create entry for item and add to stats list
        }
        return sStats;
    }

    /**
     * Creates a list of all machines and their utilisation
     * Calculates the time the machine in cooldown or working -> Not blocked
     * @return List of Machine Entries -> name + utilisation
     */
    @Override
    public List<MachineStats> getMachineStats() {
        List<MachineStats> mStats = new ArrayList<>();          // Create list of Machine Stats
        
        for(Machine m : machines.values()){                     // Iterate over ALL machines
            String name = m.getMachineName();                   // Get name of machine currently looking at
            
            double utilisation = (totalTicks == 0)              // Calculate the utilisation
                ? 0.0                                           // Avoid division by 0
                : (double) m.utilisationTime/totalTicks;        

            mStats.add(new MachineStats(name, utilisation));    // Add new entry to machine stats list
        }
        return mStats;
    }

    /**
     * Creates a list of all belts and their item type and items per minutes (IPM)
     * Calculates the belts throughput
     * @return Returns a list of belt stats -> beltName + itemName + IPM
     */
    @Override
    public List<BeltStats> getBeltStats() {
        List<BeltStats> bStats = new ArrayList<>();             // Creates new list for belt stats

        for (Belt b : belts.values()){                          // Iterate over all belts
            String beltName = b.getBeltName();                  // Get the belts name
            String itemType = b.getItemType();                  // The item type it supports

            double itemsPerMinute = (totalTicks == 0)           // Calculate items per minute
                ? 0.0                                           // Avoid division by 0
                : (double) b.getTotalItems()/totalTicks * 60;
            
            if (!beltName.equals(sink.getBeltName())){          // Add a new entry to belt stats list
                bStats.add(new BeltStats(beltName, itemType, itemsPerMinute));
            }
        }   
        return bStats;
    }


    // This class should implement the FactoryNetwork specification.
    // You should think about what methods this involves.
    // If you've used a good object oriented design on factory components, these methods might be quite simple.


}
