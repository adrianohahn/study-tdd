package br.com.adrianohahn.studytdd.java;

public class Franc {

	private int amount;

	public Franc(int amount) {
		this.amount = amount;
	}

	public Franc times(int times) {
		return new Franc(amount * times);
	}
	
	@Override
	public boolean equals(Object obj) {
		Franc dollar = (Franc) obj;
		return amount == dollar.amount;
	}

}
