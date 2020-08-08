class Accounting{
	public double valueOfSupply;
	public double vatRate;
	public double expenseRate;
	
	public void print() {
		System.out.println("Value of supply: " + valueOfSupply);
		System.out.println("VAT: " + getVat());
		System.out.println("Total :" + getTotal());
		System.out.println("Expense :" + getExpense());
		System.out.println("Income: " + getIncome());
		System.out.println("Dividend 1: " + getDividend1());
		System.out.println("Dividend 2: " + getDividend2());
		System.out.println("Dividend 3: " + getDividend3());
	}
	public double getDividend3() {
		return getIncome()* 0.2;
	}

	public double getDividend2() {
		return getIncome()* 0.3;
	}

	public double getDividend1() {
		return getIncome()* 0.5;
	}

	public double getIncome() {
		return valueOfSupply - getExpense();
	}

	public double getExpense() {
		return valueOfSupply*expenseRate;
	}

	public double getTotal() {
		return valueOfSupply + getVat();
	}

	public double getVat() {
		return valueOfSupply*vatRate;
	}
}
public class AccountingClassApp {
	
	public static void main(String[] args) {
		
//		Accounting.valueOfSupply= 10000.0;
//		Accounting.vatRate = 0.1;
//		Accounting.expenseRate = 0.3;
//		// ...
//		Accounting.print();
//		// ...
//		Accounting.valueOfSupply= 20000.0;
//		Accounting.vatRate = 0.05;
//		Accounting.expenseRate = 0.2;
//		// .. 계속 이런 식으로 바뀐다면 오류 뜰 가능성 올라감
		
		Accounting a1 = new Accounting();
		a1.valueOfSupply = 10000.0;
		a1.vatRate = 0.1;
		a1.expenseRate = 0.3;
		a1.print();
		
		Accounting a2 = new Accounting();
		a2.valueOfSupply = 20000.0;
		a2.vatRate = 0.05;
		a2.expenseRate = 0.2;
		a2.print();
		
		
		
	}

}
