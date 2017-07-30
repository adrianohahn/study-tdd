package br.com.adrianohahn.studytdd.java;

import java.util.Hashtable;
import java.util.Map;

public class Bank {

	private class Pair {
		
		private String from;
		
		private String to;
		
		
		
		public Pair(String from, String to) {
			super();
			this.from = from;
			this.to = to;
		}

		@Override
		public boolean equals(Object obj) {
			Pair pair = (Pair) obj;
			return from.equals(pair.from) && to.equals(pair.to);
		}
		
		@Override
		public int hashCode() {
			return 0;
		}

	};

	
	private Map<Pair,Integer> rates = new Hashtable<Pair,Integer>();

	public Money reduce(Expression source, String to) {
		return source.reduce(this, to);
	}

	public int rate(String from, String to) {
		if (from.equals(to)) return 1;
		return rates.get(new Pair(from, to));
	}

	public void addRate(String from, String to, int rate) {
		rates.put(new Pair(from,to), rate);
	}

}
