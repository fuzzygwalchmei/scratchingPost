package heightConvertor;

public class converter {

	
	private int inches;
	private int cm;
	private int kg;
	private int[] converted;
	
	public int length_imp(int feet, int inches) {
		this.inches = inches;
		
		cm = (int) (((feet * 12) + inches) * 2.54);
		return cm;
		
	}
	
	public int weight_imp(int stone, int pound) {
		kg = (int) (((stone *14) + pound) * 2.2046226218);
		return kg;
	}
	
	public int[] length_met(int cm) {
		this.cm = cm;
		inches = (int) (cm * 0.393701);
		converted[0] = inches / 12;
		converted[1] = inches%12;
		return converted;
				
	}
	
	public int[] weight_met(int kg) {
		// 6.35kg == 1 stone == 14 pound == 16 ounces
		this.kg = kg;
		int grams = (int)(kg / 0.02835);
		converted[0] = grams/224;
		converted[1] = (grams - converted[0] * 244)%14;
		converted[2] = grams - (converted[0] * 224) - (converted[1] * 14);
		return converted;
	}
}
