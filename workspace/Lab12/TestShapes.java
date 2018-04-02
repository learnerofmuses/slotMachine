
public class TestShapes extends SimpleShape{

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
		
		Triangle t = new Triangle();
		t.makeVisible();
		t.slowMoveVertical(150);
		t.changeColor("orange");
		t.changeSize(60, 80, 100);
		
		Sqaure s = new Sqaure();
		s.makeVisible();
		s.slowMoveHorizontal(80);
		s.changeColor("blue");
		s.changeSize(60, 60);
		
		pentagon p = new pentagon();
		p.makeVisible();
		p.slowMoveDiagonal(75, 5, 5);
		p.changeColor("yellow");
		p.changeSize();
	}

}
