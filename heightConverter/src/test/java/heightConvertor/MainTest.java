package heightConvertor;

import static org.junit.Assert.*;

import org.junit.Test;

public class MainTest {

	@Test
	public void test() {
		// fail("Not yet implemented");
		
		converter testing = new converter();
		
		assertEquals(180, testing.length_imp(5, 11));
		assertEquals(182, testing.length_imp(6, 0));	
		
		assertEquals([6,0], testing.length_met(182));
		
	}

}
