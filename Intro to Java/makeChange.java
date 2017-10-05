class main{
	public static double makeChange(double itemCost, double dollarsProvided){
		return dollarsProvided-itemCost;
	}
	public static void main(String[] args){
		System.out.println(makeChange(23.9, 345.87));
	}
}