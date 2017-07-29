package br.com.adrianohahn.studytdd.test;

import br.com.adrianohahn.studytdd.java.Dollar;
import junit.framework.TestCase;

public class MultiCurrencyTest extends TestCase {
	
	public void testMultiplication() {
		Dollar five = new Dollar(5);
		assertEquals(new Dollar(10), five.times(2));
		assertEquals(new Dollar(15), five.times(3));
	}
	
	public void testEquality() {
		assertTrue(new Dollar(5).equals(new Dollar(5)));
		assertFalse(new Dollar(5).equals(new Dollar(6)));
	}


}
