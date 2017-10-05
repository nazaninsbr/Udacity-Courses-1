class main{
	public static void playLyrics(boolean play){
		if(play){
			System.out.println("Music is Playing");
		}else{
			System.out.println("Music is Paused");
		}
	}
	public static void main(String[] args){
		boolean playButton = true;
		playLyrics(playButton);
	}
}