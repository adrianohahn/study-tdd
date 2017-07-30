package br.com.adrianohahn.studytdd.java;

public abstract class Money {

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
				&& getClass().equals(obj.getClass());
	}

	public static Money dollar(int amount) {
		return new Dollar(amount, "USD");
	}
	
	public static Money franc(int amount) {
		return new Franc(amount, "CHF");
	}

	public abstract Object times(int amount);

	public String currency() {
		return this.currency;
	}

	

}
