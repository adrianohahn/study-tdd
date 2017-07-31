package br.com.adrianohahn.studytdd.java;

public interface Expression {

	Money reduce(Bank bank, String to);

	Expression plus(Expression fiveFrancs);

}
