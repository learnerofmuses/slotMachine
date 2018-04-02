
public class TestShapes {

	public static void main(String[] args) {
		Rect r = new Rect();
		r.makeVisible();
		r.slowMoveHorizontal(100);
		r.changeColor("magenta");
		r.changeSize(100, 200);
		Oval o = new Oval();
		o.makeVisible();
		o.slowMoveDiagonal(125, 1, 1);
		o.changeColor("green");
		o.changeSize(80, 160);
	}

}
