package br.com.adrianohahn.studytdd.test;

import br.com.adrianohahn.studytdd.java.Dollar;
import junit.framework.TestCase;

public class MultiCurrencyTest extends TestCase {
	
	public void testMultiplication() {
		Dollar five = new Dollar(5);
		Dollar product = five.times(2);
		assertEquals(10, product.amount);
		product = five.times(3);
		assertEquals(15, product.amount);
	}
	
	public void testEquality() {
		assertTrue(new Dollar(5).equals(new Dollar(5)));
		assertFalse(new Dollar(5).equals(new Dollar(6)));
	}


}