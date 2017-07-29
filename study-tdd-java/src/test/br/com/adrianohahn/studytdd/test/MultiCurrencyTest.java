package br.com.adrianohahn.studytdd.test;

import br.com.adrianohahn.studytdd.java.Dollar;
import junit.framework.TestCase;

public class MultiCurrencyTest extends TestCase {
	
	public void testMultiplication() {
		Dollar five = new Dollar(5);
		five.times(2);
		assertEquals(10, five.amount);
	}

}
