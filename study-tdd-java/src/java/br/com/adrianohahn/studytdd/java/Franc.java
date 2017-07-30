
package br.com.adrianohahn.studytdd.java;

public class Franc extends Money {
	
	public Franc(int amount, String currency) {
		super(amount, currency);
	}

	public Money times(int times) {
		return new Money(amount * times, currency);
	}
	

}
