package br.com.adrianohahn.studytdd.java;

public class Dollar {

	public int amount;

	public Dollar(int amount) {
		this.amount = amount;
	}

	public void times(int times) {
		amount *= times;
	}

}
