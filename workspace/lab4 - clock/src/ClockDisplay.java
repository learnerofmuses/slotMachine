
/**
 * The ClockDisplay class implements a digital clock display for a
 * European-style 24 hour clock. The clock shows hours, minutes and 
 * seconds. The range of the clock is 00:00:00 (midnight) to 23:59:59
 * (one minute before midnight).
 * 
 * The clock display receives "ticks" (via the timeTick method)
 * and reacts by incrementing the display. This is done in the usual 
 * clock fashion: the hour increments when the minutes roll over to 
 * zero.
 * 
 * @author Michael Kolling and David J. Barnes
 * @version 2008.03.30
 */
public class ClockDisplay
{
    private NumberDisplay seconds;
    private NumberDisplay minutes;
    private NumberDisplay hours;
    private String displayString;    // simulates the actual display
    
    /**
     * Constructor for ClockDisplay objects. This constructor 
     * creates a new clock set at 00:00.
     */
    public ClockDisplay()
    {
        seconds = new NumberDisplay(60);
        minutes = new NumberDisplay(60);
        hours = new NumberDisplay(12);
        updateDisplay();
    }

    /**
     * Constructor for ClockDisplay objects. This constructor
     * creates a new clock set at the time specified by the 
     * parameters.
     */
    public ClockDisplay(int m)
    {
        seconds = new NumberDisplay(60);
        minutes = new NumberDisplay(60);
        hours = new NumberDisplay(12);
        
        setTime(m, 55);
    }

    /**
     * This method makes the clock display go forward one tick.
     */
    public void timeTick()
    {
        seconds.increment();
        if(seconds.getValue() == 0) {  
            minutes.increment();
        }
        else if(minutes.getValue() >= 60) {
        	hours.increment();
        }
        updateDisplay();
    }

    /**
     * Set the time of the display to the specified minute and
     * second.
     */
    public void setTime(int h, int m)
    {
        seconds.setValue(55);
        minutes.setValue(m);
        hours.setValue(h); 
        updateDisplay();
    }

    /**
     * Return the current time of this display in the format MM:SS.
     */
    public String getTime()
    {
        return displayString;
    }
    
    /**
     * Update the internal string that represents the display.
     */
    private void updateDisplay()
    {
        displayString = hours.getDisplayValue() + ":" +
        				minutes.getDisplayValue() + ":" + 
                        seconds.getDisplayValue();
    }
}
