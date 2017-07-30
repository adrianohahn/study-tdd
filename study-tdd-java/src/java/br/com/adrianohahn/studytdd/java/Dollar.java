package br.com.adrianohahn.studytdd.java;

public class Dollar extends Money {
	
	public Dollar(int amount, String currency) {
		super(amount, currency);
	}

	public Money times(int times) {
		return new Money(amount * times, currency);
	}

}
