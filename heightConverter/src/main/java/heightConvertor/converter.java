package heightConvertor;

public class converter {

	private int feet;
	private int inches;
	
	public int converter(int feet, int inches) {
		this.feet = feet;
		this.inches = inches;
		
		int cm = (int) (((feet * 12) + inches) * 2.54);
		return cm;
		
	}
}
