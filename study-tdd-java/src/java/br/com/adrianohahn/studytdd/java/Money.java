package br.com.adrianohahn.studytdd.java;

public class Money {

	protected int amount;
	protected String currency;
	
	public Money(int amount, String currency) {
		this.amount = amount;
		this.currency = currency;
	}

	@Override
	public boolean equals(Object obj) {
		Money money = (Money) obj;
		return amount == money.amount
				&& currency.equals(money.currency);
	}

	public static Money dollar(int amount) {
		return new Dollar(amount, "USD");
	}
	
	public static Money franc(int amount) {
		return new Franc(amount, "CHF");
	}

	public Object times(int amount) {
		return null;
	}

	public String currency() {
		return this.currency;
	}

	@Override
	public String toString() {
		return amount + " " + currency;
	}

}
