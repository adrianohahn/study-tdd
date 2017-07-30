package br.com.adrianohahn.studytdd.java;

public class Dollar extends Money {

	public Dollar(int amount) {
		this.amount = amount;
	}

	public Dollar times(int times) {
		return new Dollar(amount * times);
	}

}
