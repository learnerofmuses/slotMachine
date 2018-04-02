import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;

/**
 * This class contains the Memory Management methods called by the Simulator.
 * 
 * Currently, this class implements the FIFO page replacement algorithm.
 * Modify this class with your page replacement algorithm.
 * 
 * @author Adam Fischbach
 * @version Fall 2013
 *
 */
public class MemoryManagerFIFO implements MemoryManager {
	
	private PageTable table;			// Reference to the page table
	private Simulator sim;				// Reference to the simulator
	private int location = 0; 			//curent place in copy 
	private int ind = 0; 				//pointer indicator
	private ArrayList<Integer> copy = new ArrayList<Integer>(); //holder

	
	///////////////////////////////////////////////////////////////////
										///////////////////////////////
	private Queue<Integer> q;			// Data structure for FIFO
										///////////////////////////////
	///////////////////////////////////////////////////////////////////
	
	private Queue<Integer> freeList;	// Queue of free frame numbers
	
	/**
	 * Creates a new MemoryManager.  Builds a free list containing all frames.
	 * @param table reference to the page table
	 * @param sim reference to the simulator
	 * @param gui reference to the user interface
	 */
	public MemoryManagerFIFO(PageTable table, Simulator sim) {
		this.table = table;
		this.sim = sim;
		
		///////////////////////////////////////////////////////////////
										///////////////////////////////
		q = new LinkedList<Integer>();	// Create data structure for FIFO
										///////////////////////////////
		///////////////////////////////////////////////////////////////
		
		freeList = new LinkedList<Integer>();
		for(int i=0; i<sim.getNumberFrames(); i++) {
			freeList.add(i);
		}
	}
	
	/**
	 * This method is called by the simulator when a page fault should occur.
	 * The specified page is not currently resident in a frame, so this method
	 * must choose a frame in which to load the page either by finding a free
	 * frame or evicting a resident page.
	 * @param pageNumber page number of page simulator tried to access
	 */
	public void handlePageFault(int pageNumber) {
		int frame;
		if (freeList.isEmpty()) {
			frame = evictPage();			// Evict a page if no frames are free
		} else {
			frame = freeList.remove();		// Pick next free frame from free list
		}
		PTEntry e = table.getEntry(pageNumber);
		
		///////////////////////////////////////////////////////////////////////
											///////////////////////////////////
		q.add(pageNumber);					// Add page to FIFO queue
											///////////////////////////////////
		///////////////////////////////////////////////////////////////////////
		
		e.setValid(true);					// Set page table entry's Valid bit
		e.setFrame(frame);					// Update page table entry's frame number
		sim.loadPage(pageNumber, frame);	// Tell simulator to load page in a frame
	}
	
	/**
	 * This method is called by the simulator whenever a page is accessed.
	 * This method is not needed for all page replacement algorithms.
	 * @param pageNumber number page being accessed
	 */
	public void pageAccessed(int pageNumber) {
		// This method does nothing for FIFO!
	}
	
	/**
	 * This method uses a page replacement algorithm to choose which resident page to evict.
	 * Currently implements the FIFO algorithm.
	 * @return the page to evict
	 */
	private int evictPage() {
		int[] totalAmountPages = sim.getAccesses(); 
		int current = sim.getCurrentAccess();
		int[] simPages = sim.getFrameTable(); 
		if(ind==0){
			for(int a:totalAmountPages){
				copy.add(a);
			}
			ind=1; 
		}
		for(int i=location; i<current; i++){ //this removes the numbers that have been used previously in queue
			copy.remove(0); 
		}
		location=current;
		int pageNumber = 0;
		int max = 0;//evicts farthest page that is currently being used
		for(int i = 0; i<simPages.length && max != -1; i++){
			if(copy.indexOf(simPages[i])>max){ 
				pageNumber = i;
				max=copy.indexOf(simPages[i]);
			}
			if(copy.indexOf(simPages[i])==-1){
				pageNumber=i;
				max=copy.indexOf(simPages[i]);
			}
		}

		
		PTEntry e = table.getEntry(pageNumber);
		e.setValid(false);					// Clear page table entry's Valid bit
		e.setModified(false);
		e.setAccessed(false);
		sim.evict(pageNumber);
		return e.getFrame();
	}
	
}
