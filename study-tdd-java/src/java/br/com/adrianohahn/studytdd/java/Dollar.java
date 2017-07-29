package br.com.adrianohahn.studytdd.java;

public class Dollar {

	private int amount;

	public Dollar(int amount) {
		this.amount = amount;
	}

	public Dollar times(int times) {
		return new Dollar(amount * times);
	}
	
	@Override
	public boolean equals(Object obj) {
		Dollar dollar = (Dollar) obj;
		return amount == dollar.amount;
	}

}
