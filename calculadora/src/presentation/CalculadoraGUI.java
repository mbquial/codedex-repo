package presentation;

import javax.swing.*;
import java.awt.*;

public class CalculadoraGUI extends JFrame {
	private JButton num1Button, num2Button, num3Button, num4Button, num5Button, num6Button, num7Button, num8Button, num9Button, num0Button, sumaButton, restaButton, divButton, multButton, igualButton, comaButton;
	public CalculadoraGUI() {
		prepareElements();
		prepareActions();
	}

	private void prepareActions() {
		
	}

	private void prepareElements() {
		setTitle("Calculadora de Karla");
		Dimension frame = Toolkit.getDefaultToolkit().getScreenSize();
		int ancho = frame.width/7;
		int alto = frame.height/3;
		setSize(ancho,alto);
		setLocation((frame.width - ancho)/2, (frame.height - alto)/2);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		// Falta poner que se crea la calculadora
		prepareElementsButtons();
		prepareElementsDisplay();
	}

	/*
	 * Método que crea la "pantalla" donde se van a mostrar las operaciones
	 */
	private void prepareElementsDisplay() {
		JLabel pantalla = new JLabel("0");
		add(pantalla, BorderLayout.NORTH);
		
	}

	/*
	 * Método que crea la parte de los botones que maneja todos los botones. Tanto de las operaciones como de los números
	 */
	private void prepareElementsButtons() {
		JPanel numerosPanel = new JPanel();
		numerosPanel.setLayout(new GridLayout(4,4));
		
		num7Button = new JButton("7");
		num8Button = new JButton("8");
		num9Button = new JButton("9");
		divButton = new JButton("/");
		num4Button = new JButton("4");
		num5Button = new JButton("5");
		num6Button = new JButton("6");
		multButton = new JButton("*");
		num1Button = new JButton("1");
		num2Button = new JButton("2");
		num3Button = new JButton("3");
		restaButton = new JButton("-");
		num0Button = new JButton("0");
		comaButton = new JButton(".");
		igualButton = new JButton("=");
		sumaButton = new JButton("+");
		
		numerosPanel.add(num7Button);
		numerosPanel.add(num8Button);
		numerosPanel.add(num9Button);
		numerosPanel.add(divButton);
		numerosPanel.add(num4Button);
		numerosPanel.add(num5Button);
		numerosPanel.add(num6Button);
		numerosPanel.add(multButton);
		numerosPanel.add(num1Button);
		numerosPanel.add(num2Button);
		numerosPanel.add(num3Button);
		numerosPanel.add(restaButton);
		numerosPanel.add(num0Button);
		numerosPanel.add(comaButton);
		numerosPanel.add(igualButton);
		numerosPanel.add(sumaButton);
		add(numerosPanel, BorderLayout.SOUTH);
	}

	public static void main(String[] args) {
		CalculadoraGUI gui = new CalculadoraGUI();
		gui.setVisible(true);
	}
}