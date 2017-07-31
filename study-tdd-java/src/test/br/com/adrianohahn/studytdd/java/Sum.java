package br.com.adrianohahn.studytdd.java;

public class Sum implements Expression {

	public Sum(Expression augend, Expression addend) {
		this.augend = augend;
		this.addend = addend;
	}

	public Expression augend;
	
	public Expression addend;

	@Override
	public Money reduce(Bank bank, String to) {
		int amount = augend.reduce(bank, to).amount +
				addend.reduce(bank, to).amount;
		return new Money(amount, to);
	}

	@Override
	public Expression plus(Expression fiveFrancs) {
		// TODO Auto-generated method stub
		return null;
	}
	

}
